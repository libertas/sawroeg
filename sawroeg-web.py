#!/usr/bin/env python3

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import dictionary


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        start = 0
        try:
            start = max(int(self.get_argument("start")), 0)
        except (ValueError, tornado.web.MissingArgumentError):
            pass
        has_count = False
        count = 500
        try:
            count = max(int(self.get_argument("count")), 1)
            has_count = True
        except (ValueError, tornado.web.MissingArgumentError):
            pass
        key = ''
        try:
            key = self.get_argument("q")
        except tornado.web.MissingArgumentError:
            pass
        result = list(dictionary.searchWord(key)) if key else []
        template_args = {
            "key": key, "start": start, "count": count, "has_count": has_count,
            "total_count": len(result), "result": result[start:start+count]
        }
        self.render("sawroeg-web.html", **template_args)


if __name__ == "__main__":
    tornado.options.define("debug", default=False, help="enabling debugging features", type=bool)
    tornado.options.define("port", default=7777, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    app_settings = {
        'gzip': True,
        'debug': tornado.options.options.debug,
        'static_path': 'sawroeg-web-static'
    }
    application = tornado.web.Application([
        ("/sawroeg", SearchHandler),
        ("/.*", tornado.web.RedirectHandler, {'url': '/sawroeg'})
    ], **app_settings)
    server = tornado.httpserver.HTTPServer(application)
    server.bind(tornado.options.options.port, 'localhost')
    server.start(1)
    tornado.ioloop.IOLoop.instance().start()
