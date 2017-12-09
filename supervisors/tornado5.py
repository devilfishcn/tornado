# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import common
from common import get_args_tuple
class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.write('begin init!') 
        self.write('\t\n')
    def get(self):
        self.set_header('name', 'value')
        self.write("hello world!")
        self.write('\n')
def make_app():
    return tornado.web.Application([
        (r"/",MainHandler),
        ])

if __name__=="__main__":
    app=make_app()
    app.listen(8005,'127.0.0.1')
    tornado.ioloop.IOLoop.current().start()