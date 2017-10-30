import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,name=None):
        self.write("hello world!\n")
        self.write(name)
        
def make_app():
    return tornado.web.Application([
        (r"/",MainHandler),
        (r"/name=(\S+)&age=",MainHandler),
        ])
    
    
if __name__=="__main__":
    app=make_app()
    app.listen(8001,'127.0.0.1')
    tornado.ioloop.IOLoop.current().start()