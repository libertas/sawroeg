#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode


import json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import dictionary,info

try:
    tornado.web.MissingArgumentError
except AttributeError:
    tornado.web.MissingArgumentError = tornado.web.HTTPError

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
            "total_count": len(result), "result": result[start:start+count],
            "version": info.version
        }
        self.render("sawroeg.html", **template_args)


class ApiHandler(tornado.web.RequestHandler):
    def get(self):
        # I think it is better to copy it twice rather than make it in a func.
        start = 0
        try:
            start = max(int(self.get_argument("start")), 0)
        except (ValueError, tornado.web.MissingArgumentError):
            pass
        count = None
        try:
            count = max(int(self.get_argument("count")), 1)
        except (ValueError, tornado.web.MissingArgumentError):
            pass
        api_type = 'xml'
        try:
            api_type = self.get_argument("type")
        except tornado.web.MissingArgumentError:
            pass
        if api_type not in ('xml', 'json'):
            self.set_status(400)
            self.set_header("Content-Type", "text/plain; charset=utf-8")
            self.render("sawroeg-api-help.html")
            return
        try:
            key = self.get_argument("q")
        except tornado.web.MissingArgumentError:
            self.set_status(400)
            self.set_header("Content-Type", "text/plain; charset=utf-8")
            self.render("sawroeg-api-help.html")
            return
        result = list(dictionary.searchWord(key)) if key else []
        if count is None:
            have_more = False
            del result[:start]
        else:
            have_more = len(result)>start+count
            result = result[start:start+count]
        if api_type == 'xml':
            self.set_header("Content-Type", "text/xml; charset=utf-8")
            template_args = {
                "key": key, "start": start, "count": count,
                "result": result, "have_more": have_more
            }
            self.render("sawroeg-api-xml.html", **template_args)
        elif api_type == 'json':
            self.set_header("Content-Type", "text/json; charset=utf-8")
            if have_more:
                result.append(('...', []))
            self.write(json.dumps(result))
        else:
            raise RuntimeError('program should not reach here')


if __name__ == "__main__":
    tornado.options.define("debug", default=False, help="enabling debugging features", type=bool)
    tornado.options.define("port", default=7777, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    app_settings = {
        'gzip': True,
        'debug': tornado.options.options.debug,
        'template_path': 'sawroeg-web-template',
        'static_path': 'sawroeg-web-static'
    }
    application = tornado.web.Application([
        ("/sawroeg", SearchHandler),
        ("/api", ApiHandler),
        ("/.*", tornado.web.RedirectHandler, {'url': '/sawroeg'})
    ], **app_settings)
    server = tornado.httpserver.HTTPServer(application)
    server.bind(tornado.options.options.port, 'localhost')
    server.start(1)
    tornado.ioloop.IOLoop.instance().start()
