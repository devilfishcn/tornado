import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.write('begin init!') 
        self.write('\t\n')
    def get(self):
        self.set_header('name', 'value')
        self.write("hello world!")
        self.write('\n')
        name = self.get_argument('name')
        self.write(name)
        self.write('\n')
        age = self.get_argument('age')
        self.write(age)
        self.write('\n')
        address={'xiaoqu':'shanyucheng'}
        self.redirect('http://tornado.muxiulin.cn/static/template.html', address)
def make_app():
    return tornado.web.Application([
        (r"/",MainHandler),
        (r"/?name=(\S+)&age=",MainHandler),
        ],
        static_path='/root/github/tornado')
if __name__=="__main__":
    app=make_app()
    app.listen(8001,'127.0.0.1')
    tornado.ioloop.IOLoop.current().start()