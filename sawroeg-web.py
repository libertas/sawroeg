#! /usr/bin/env python3
import tornado.ioloop
import tornado.web
import dictionary

class Search(tornado.web.RequestHandler):
	def get(self,url):
		try:
			key=self.get_argument("key")
			items=dictionary.newSearch(key,"ABC").rsplit("\n")
		except:
			items=list()
		self.render("sawroeg-web.html",items=items)

application = tornado.web.Application([
	("/(.*)",Search),
	])

if __name__ == "__main__":
	application.listen(7777)
	tornado.ioloop.IOLoop.instance().start()
