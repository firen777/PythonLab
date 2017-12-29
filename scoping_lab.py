"""
Scoping Lab
"""

def docStringTest(a,b,c,d):
    """
    VSCode docstring rendering test.

    - markdown test1
    - test2
    - test3

    [link test](https://www.google.com)
    
    [description]
    
    Arguments:
    a: {[type]} -- [description]
    b: {[type]} -- [description]
    c: {[type]} -- [description]
    d: {[type]} -- [description]
    
    Returns:
    [type] -- [description]
    """
    
    return a*b*c*d


x = 100


def someFunc():
    """
    scoping test.

    Returns:
        [type] -- x, which is defined outside of the scope
    
    """
    return x


var1 = someFunc()
print(var1)  # print 100

x = 200
print(var1)  # pass by value, print 100

var1 = someFunc()  # reassign var1 to 200
print(var1)  # print 200


def lambdaFunc(f):
    """
    Scoping lab with lambda.
    
    Arguments:
        f {[type]} -- function that accept one param
    
    Returns:
        [type] -- ()->f(x), where x is defined outside the scope
    """
    
    return lambda: f(x)


def fFunc1(n):
    """
    @param n: number
    @return: n+1
    """
    return n + 1
