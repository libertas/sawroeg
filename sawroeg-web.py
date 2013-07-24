#!/usr/bin/env python3

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import dictionary

def iter_slice(iter_in, start=0, count=500):
    end = start+count
    n = 0
    result = list()
    for i in iter_in:
        if n>=start:
            result.append(i)
            if n >= end-1:
                return result
        n += 1


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
            key = self.get_argument("key")
        except tornado.web.MissingArgumentError:
            pass
        result = iter_slice(dictionary.searchWord(key), start, count)
        template_args = {
            "key": key, "start": start, "count": count,
            "has_count": has_count, "result": result
        }
        self.render("sawroeg-web.html", **template_args)


if __name__ == "__main__":
    tornado.options.define("debug", default=True, help="enabling debugging features", type=bool)
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
