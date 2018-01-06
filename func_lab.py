#keyword argument/named param and stuff

def kwArg(x=1, y=2, z=3):
    """key word argument example
    
    Arguments:
    x: {int} -- [description] (default: {1})
    y: {int} -- [description] (default: {2})
    z: {int} -- [description] (default: {3})
    Returns:
    x+y+z
    """ 
    return x+y+z

print(kwArg())

print(kwArg(x=10, y=21))
print(kwArg(y=211, z=1))


def flex_arg(*args):
    """[summary]
    
    [description]
    
    Arguments:
        *args {[type]} -- [description]
    """
    print(args)
    ans = ""
    for e in args:
        ans = ans + str(e)
    return ans

print(flex_arg(1,2,3,4.4,5.5))

