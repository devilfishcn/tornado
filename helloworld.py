# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import common
from common import get_args_tuple
from tornado.options import options,define

define("port", default=8888, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.write('begin init!') 
        self.write('\t\n')
    def get(self):
        self.set_header('name', 'value')
        self.write("hello world!")
        self.write('\n')
#         name = self.get_arguments('name')
#         self.write(name)
#         self.write('\n')
#         age = self.get_argument('age','')
#         self.write(age)
#         self.write('\n')
        
        self.name,self.age= get_args_tuple(self,'a',{'name','age'})
        
        print self.name
        print self.age
      
        
def make_app():
    return tornado.web.Application([
        (r"/",MainHandler),
        ])

if __name__=="__main__":
    options.parse_command_line()

    app = make_app()
    HTTP_SERVER = tornado.httpserver.HTTPServer(app, xheaders=True)
    HTTP_SERVER.listen(options.port)
    tornado.ioloop.IOLoop.current().start()