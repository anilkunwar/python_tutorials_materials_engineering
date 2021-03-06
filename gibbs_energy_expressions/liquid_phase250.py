#Reference: pythonforundergradengineers.com/sympy-expressions-and-equations.html
#Reference: https://stackoverflow.com/questions/5214578/python-print-string-to-text-file
# This tutorial converts the parabolic gibbs free energy expressions as follow:
# Input : f_liq = A1*(x-xeq)^2+B1*x+C1 [J/mol]
# Output: f_liq = A2*x^2+B2*x+C2 [J/mol]
# Doing this the equilibrium composition can be preserved for further fitting at different temperatures
import sympy as sym
import numpy as np
from sympy import symbols
aliq,x,xeq,bliq,cliq,y = symbols('aliq,x,xeq,bliq,cliq,y')
expr=aliq*y+bliq*x+cliq
aterm=sym.expand(x-0.8617)**2
print('f_liq(J/mol)=',expr)
print('aterm is:',aterm)
expr2=expr.subs(y,aterm).subs(aliq,2.3276E+04).subs(bliq,2.054E+03).subs(cliq,-3.051938E+04)
print('f_liq(J/mol)=',expr2)
#expr3=sym.expand(expr2)
expr3=sym.simplify(expr2)
#expr3=expr2.evalf()
temp=523.15
print('f_liq(J/mol)=',expr3)
np.savetxt('t523k-liq.txt',["f_liq(J/mol)= %s"%expr3],fmt='%s',header='f=Ax^2+Bx+c',footer='T=523.15 K')

