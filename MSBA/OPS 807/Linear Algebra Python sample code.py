# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 18:23:10 2019

Linear algebra examples in Numpy

@author: jg
"""

# matrix addition

import numpy as np

a = np.array([[6,1,1], [4, -2, 5], [2,8,7]])
b = np.array([[1,5,7], [2,3.5,14], [-4, -5, 12]])

# array addition

c = a + b
print(f'addition of matrix a =\n {a} \nplus b =\n {b} \nis equal to \n {c}' )
# array subtraction
d = a - b
print(f'matrix a =\n {a} \nminus b =\n {b} \nis equal to \n {d}' )
# array multiplication. Make sure that the inner dimension of two matrices are the same
# remember that * corresponds to element-wise multiplication. You can also use the dot operator
e = a @ b
e1 = a.dot(b)
np.allclose(e,e1)
print(f'multiplication of matrix a =\n {a} \nby b =\n {b} \nis equal to \n {e}' )
# transpose
aT = a.T
print(f'The transpose of matrix a =\n {a} \nis \n {aT}' )

# determinant 2X2
import numpy as np
a = np.array([[1,2], [3,4]]) 
print(np.linalg.det(a))

# determinant 3X3
print(b) 
print(np.linalg.det(b)) 
print(6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2))

# cofactors using sympy
from sympy import *
A = Matrix([[6,1,1], [4, -2, 5], [2,8,7]])
A.adjugate().T

# cofactors using numpy
a_cofac = np.linalg.inv(a).T * np.linalg.det(a)
print(a_cofac)


# adjugate
a_adjugate = np.linalg.inv(a) * np.linalg.det(a)
print(a_adjugate)

# adjoint or adjugate using sympy
A.adjoint() # just gives you the transpose
A.adjugate() # this gives you transpose of cofactor matrix



# Matrix Inverse

a_inv = np.linalg.inv(a)
print(a_inv)
print(a)
np.allclose(np.dot(a, a_inv), np.eye(3))
# check based on the definition of inverse
idnty = a_inv @ a 
print(idnty)
# solve a system of linear equation
'''
solve the following linear system
A_mat X = B_mat

2X1 + 3X2 = 24
4X1 + 2X2 = 36

A_mat = | 2  3|
        | 4  2|
        
B_mat = |24|
        |36|        

'''
A_mat = np.array([[2,3], [4,2]])
B_mat = np.array([24,36])
x = np.linalg.solve(A_mat, B_mat)
x

# check A_mat X = B_mat
np.allclose(np.dot(A_mat, x), B_mat)
