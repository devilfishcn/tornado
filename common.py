

def get_args_tuple(request,*args):
    _=[]
    for i in range(len(args)):
        _.append(request.get_argument(args[i],'')) 
    return tuple(_)