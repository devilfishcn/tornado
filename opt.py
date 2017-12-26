
from tornado.options import options,define

define("port", default=8888, help="run on the given port", type=int)
options.parse_command_line()
print(options.port)