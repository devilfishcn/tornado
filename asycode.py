import tornado.ioloop
import tornado.web
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
       http = tornado.httpclient.AsyncHTTPClient()
       http.fetch('http://muxiulin.cn', callback=self.on_response)
       
    def on_response(self,response):
        self.write(str(response.code))
        self.finish()
        
def make_app():
    return tornado.web.Application([
        (r"/",MainHandler),
        ])

if __name__=="__main__":
    app=make_app()
    app.listen(8001,'127.0.0.1')
    tornado.ioloop.IOLoop.current().start()