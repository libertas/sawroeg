#!/usr/bin/env python3

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import dictionary


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            start = max(int(self.get_argument("start")), 0)
        except (ValueError, tornado.web.MissingArgumentError):
            start = 0
        try:
            count = max(int(self.get_argument("count")), 1)
            count_ = True
        except (ValueError, tornado.web.MissingArgumentError):
            count = 500
            count_ = False
        try:
            key = self.get_argument("key")
        except tornado.web.MissingArgumentError:
            key = ''
        result = list(dictionary.searchWord(key)) if key else []
        self.render("sawroeg-web.html", key=key, start=start, count=count, count_=count_, result=result[start:start+count], total_count=len(result))


if __name__ == "__main__":
    tornado.options.define("debug", default=False, help="enabling debugging features", type=bool)
    tornado.options.define("port", default=7777, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    app_settings = {
        'gzip': True,
        'debug': tornado.options.options.debug
    }
    application = tornado.web.Application([
        ("/.*", SearchHandler),
    ], **app_settings)
    server = tornado.httpserver.HTTPServer(application)
    server.bind(tornado.options.options.port, 'localhost')
    server.start(1)
    tornado.ioloop.IOLoop.instance().start()
