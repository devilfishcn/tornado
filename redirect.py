import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name')
        self.write(name)
        self.write('\n')
        age = self.get_argument('age')
        self.write(age)
        self.write('\n')
        self.redirect('/maint')

class MaintHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('maint\n')
                
def make_app():
    return tornado.web.Application([
        (r"/maint",MaintHandler),
        (r"/?name=(\S+)&age=",MainHandler),
        ])

if __name__=="__main__":
    app=make_app()
    app.listen(8001,'127.0.0.1')
    tornado.ioloop.IOLoop.current().start()