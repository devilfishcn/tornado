

def get_args_tuple(request,default=None,*args):
    _=[]
    for i in range(len(args)):
        _.append(request.get_argument(args[i], '' if default is None else default).strip()) 
    return tuple(_)