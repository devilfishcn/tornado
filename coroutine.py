import tornado.ioloop
import tornado.web
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
       http = tornado.httpclient.AsyncHTTPClient()
       response = yield http.fetch('http://muxiulin.cn', callback=self.on_response)
       self.write(str(response.code))
   
def make_app():
    return tornado.web.Application([
        (r"/",MainHandler),
        ])

if __name__=="__main__":
    app=make_app()
    app.listen(8001,'127.0.0.1')
    tornado.ioloop.IOLoop.current().start()