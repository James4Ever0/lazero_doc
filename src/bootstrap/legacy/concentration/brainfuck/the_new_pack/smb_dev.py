# import sympy
# d=dir(sympy.calculus)
from sympy import * # this is horrible.
# about to put something into the matrix.
# things will go nasty.
x, y = symbols("x y")
expr = x**2+2*y+y**3
print("expression:{}".format(expr))
df = Derivative(expr, x)
# diff is a function here.
print("derivative with respect of x:{}".format(df.doit()))
print("derivative with respect of x:{}".format(df))
# i, always hate math symbols.
# print(d)
# how to take partial derivative?
# how to put variable into matrix?
