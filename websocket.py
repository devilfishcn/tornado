import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options  import define,options,parse_command_line

define('port', default=8001, type='int', help='run on the given port')

clients = dict()

class  IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('index.html')
class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self,*args):
        self.id= self.get_argument('id')
        self.stream.set_nodelay(True)
        clients[self.id]={"id":self.id,"object":self}
    def on_message(self,message):
        print "client %s received a message : %s" % (self.id,message)
        
    def on_close(self):
        if self.id in clients:
            del clients[self.id]
            print "client %s is closed" % (self.id)
            
    def check_origin(self,origin):
        return True
    
app = tornado.web.Application([
    (r'/',IndexHandler),
    (r'/websocket',MyWebSocketHandler),
    ])
        
        
import threading
import time

def sendTime():
    import datetime
    while True:
        for key in clients.keys():
            msg = str(datetime.datetime.now())
            clients[key]["object"].write_message(msg)
            print "write to client %s:%s" %(key,msg)
        time.sleep(1)
        
if __name__ == '__main__':
    threading.Thread(target=sendTime).start()
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()