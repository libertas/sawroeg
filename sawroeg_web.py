#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import os

import info
import users
import userdb
from new_search import newSearch
from enviroment import *

from platform import python_version
if python_version().startswith('2'):
    str = unicode

try:
    tornado.web.MissingArgumentError
except AttributeError:
    tornado.web.MissingArgumentError = tornado.web.HTTPError

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

try:
    IsADirectoryError
except NameError:
    class IsADirectoryError(Exception):
        def __str__(self):
            return repr("IsADirectoryError")

class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        start = 0
        try:
            start = max(int(self.get_argument("start")), 0)
        except (ValueError, tornado.web.MissingArgumentError):
            pass
        has_count = False
        count = SEARCHING_LIMIT
        try:
            count = max(int(self.get_argument("count")), 1)
            has_count = True
        except (ValueError, tornado.web.MissingArgumentError):
            pass

        new_engine = "on"

        key = ''
        try:
            key = self.get_argument("q")
        except tornado.web.MissingArgumentError:
            new_engine = "on"

        result_generator = newSearch(key, "Saw", new_engine)
        template_args = {
            "key": key, "start": start, "count": count, "has_count": has_count,
            "result": result_generator, "version": info.version,
            "new_engine": new_engine, 
            "downloadPageName": DOWNLOADPAGENAME
        }
        self.render("sawroeg.html", **template_args)


class DownloadHandler(tornado.web.RequestHandler):
    def get(self,  filename = ""):
        mimes = {
            '.apk': 'application/vnd.android', 
            '.zip': 'application/zip', 
            '.doc': 'application/msword'
        }
        xb = ["B",  "K",  "M"]
        if filename.endswith("/"):
            filename = filename[:-1]
        try:
            if filename == "" or os.path.isdir(DOWNLOAD_PATH + filename):
                raise IsADirectoryError
            raw = open(DOWNLOAD_PATH + filename, 'rb').read()
            mime = mimes[filename[-4:]]
            self.set_header('Content-Type', mime)
            self.write(raw)
        except FileNotFoundError:
            self.write("Error")
        except IsADirectoryError:
            files_tmp = os.listdir(DOWNLOAD_PATH + filename)
            files = []
            size = ""
            for i in files_tmp:
                if filename != "":
                    i = filename + "/" + i
                size = os.path.getsize(DOWNLOAD_PATH + i)
                count = 1
                while count < len(xb) and size >= 1024:
                    count += 1
                    size /= 1024.0
                size = str(round(size,  1)) + xb[count - 1]
                if os.path.isdir(DOWNLOAD_PATH  + i):
                    i += "/"
                    size = ""
                files.append((i,  size))
            template_args = {
                "path": filename,
                "files": files
            }
            self.render("sawroeg-download.html",  **template_args)


class SecureHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_secure_cookie("user")
        if user == None:
            return None
        else:
            return user.decode("utf-8")


class LoginHandler(SecureHandler):
    def get(self):
        if self.get_current_user() in users.users.keys():
            self.redirect("/admin")
        else:
            self.render("sawroeg-login.html")
    
    def post(self):
        user = self.get_argument("user")
        if user in users.users.keys():
            password = self.get_argument("password")
            if password == users.users[user]:
                self.set_secure_cookie("user", user)
                self.redirect("/admin")
            else:
                self.redirect("/login")
        else:
            self.redirect("/login")


class AdminHandler(SecureHandler):
    def get(self):
        if  not self.get_current_user() in users.users.keys():
            self.redirect("/login")
        else:
            user_dict = newSearch(key="", dbpath=USER_DB_PATH)
            self.render("sawroeg-admin.html",  user_dict=user_dict)
    
    def post(self):
        if  not self.get_current_user() in users.users.keys():
            self.redirect("/login")
        else:
            word= self.get_argument("entry")
            word = word.split(" ",  1)
            try:
                word[1]
            except IndexError:
                word.append("")
            if self.get_argument("command") == "add":
                # add the word selected by the admin to NEW_DB and DB
                # NEW_DB is used to backup the word,while DB can be used by the software
                userdb.add(word[0], word[1],  NEW_DB_PATH)
                userdb.add(word[0], word[1],  DB_PATH)
            elif self.get_argument("command") == "del":
                userdb.delete(word[0], word[1], USER_DB_PATH)
            self.redirect("/admin")


class ComposeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("sawroeg-compose.html", message="")

    def post(self):
        key = self.get_argument("entry")
        discription = self.get_argument("discription")
        if key != "" and discription != "":
            userdb.add(key, discription, USER_DB_PATH)
            self.render("sawroeg-compose.html", message="Gya haeuj bae liux,cingj caj bouxguenj ma yawj.")
        else:
            self.render("sawroeg-compose.html", message="Cingj raiz doh bae.")


if __name__ == "__main__":
    tornado.options.define(
        "debug", default=False,
        help="enabling debugging features", type=bool
        )
    tornado.options.define(
        "port", default=7777,
        help="run on the given port", type=int
        )
    tornado.options.define(
        "direct", default=False,
        help="can be visited directly by outside world", type=bool
        )
    tornado.options.define(
        'ip', default='localhost',
        help="the ip addres you want to bind", type=str
        )
    tornado.options.parse_command_line()
    app_settings = {
        'gzip': True,
        'debug': tornado.options.options.debug,
        'template_path': 'sawroeg-web-template',
        'static_path': 'sawroeg-web-static', 
        'cookie_secret': users.secret
    }
    application = tornado.web.Application([
        ("/sawroeg", SearchHandler),
        ("/download",  DownloadHandler),
        ("/download/(.*)",  DownloadHandler),
         ("/login",  LoginHandler),
         ("/admin",  AdminHandler), 
         ("/raiz",  ComposeHandler), 
         ("/raiz/",  ComposeHandler), 
        ("/.*", tornado.web.RedirectHandler, {'url': '/sawroeg'})
    ], **app_settings)
    if tornado.options.options.direct:
        application.listen(tornado.options.options.port)
    else:
        server = tornado.httpserver.HTTPServer(application)
        server.bind(tornado.options.options.port, tornado.options.options.ip)
        server.start(1)
    tornado.ioloop.IOLoop.instance().start()
