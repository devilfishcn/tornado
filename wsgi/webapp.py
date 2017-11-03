from wsgiref.simple_server import make_server

def application(environ,start_response):
    start_response('200 OK',[('Content-type','text/html')])
    return '<b>hello world!</b>'

server=make_server('', 8080, application)
server.serve_forever()