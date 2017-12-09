from wsgiref.simple_server import make_server
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi


def application(environ,start_response):
    start_response('200 OK',[('Content-type','text/html')])
    return '<b>hello world!</b>'

# server=make_server('', 8080, application)
# server.serve_forever()


container = tornado.wsgi.WSGIContainer(application)
http_server = tornado.httpserver.HTTPServer(container)
http_server.listen(8888)
tornado.ioloop.IOLoop.current().start()