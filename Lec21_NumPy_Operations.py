"""
Ankit Singhal - as.ankitsinghal.7@gmail.com
Python for Data Science and Machine Learning Bootcamp - Udemy
Lecture 21: NumPy Operations
"""
import numpy as np
array = np.arange(0,11)
print(array)
"""
array = [ 0  1  2  3  4  5  6  7  8  9 10]
"""

print(array + array)
"""
Output: [ 0  2  4  6  8 10 12 14 16 18 20]
Addition of 2 arrays (element by element)
"""

print(array - array)
"""
Output: [0 0 0 0 0 0 0 0 0 0 0]
Subtraction of 2 arrays (element by element)
"""

print(array * array)
"""
Output: [  0   1   4   9  16  25  36  49  64  81 100]
Multiplication of 2 arrays (element by element)
"""

print(array + 100)
"""
Output: [100 101 102 103 104 105 106 107 108 109 110]
Addition of a scalar value (100) to all the elements of the array.
"""

print(array - 100)
"""
Output: [-100  -99  -98  -97  -96  -95  -94  -93  -92  -91  -90]
Subtraction of a scalar value (100) from all the elements of the array.
"""

print(array * 100)
"""
Output: [   0  100  200  300  400  500  600  700  800  900 1000]
Multiplication of a scalar value (100) with all the elements of the array.
"""

print(array / 100)
"""
Output: [0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.1 ]
Division of a scalar value (100) with all the elements of the array.
"""

print(array**2)
"""
Output: [  0   1   4   9  16  25  36  49  64  81 100]
All the elements of the array raised to the power 2.
"""

print(array/array)
"""
Output: [nan  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
nan = No Object
Since, the first element of array was 0. So, 0/0 doesn't mean anything.
NumPy doesn't give a error, it gives a Runtime Warning instead.
Warning (from warnings module):
  File "C:/Users/ankit/Desktop/Lec21_NumPy_Operations.py", line 61
    print(array/array)
RuntimeWarning: invalid value encountered in true_divide
"""

print(1/array)
"""
Output: [       inf 1.         0.5        0.33333333 0.25       0.2
 0.16666667 0.14285714 0.125      0.11111111 0.1       ]
inf = Infinity
Since, the first element of array was 0. So, 1/0 becomes infinity.
NumPy doesn't give a error, it gives a Runtime Warning instead.
Warning (from warnings module):
  File "C:/Users/ankit/Desktop/Lec21_NumPy_Operations.py", line 73
    print(1/array)
RuntimeWarning: divide by zero encountered in true_divide
"""

print(np.sqrt(array))
"""
Gives square root of all the elements of the array.
Output: [0.         1.         1.41421356 1.73205081 2.         2.23606798
 2.44948974 2.64575131 2.82842712 3.         3.16227766]
"""

print(np.exp(array))
"""
Gives exponential of all the elements of the array.
Output:
[1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01
 5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03
 2.98095799e+03 8.10308393e+03 2.20264658e+04]
"""

print(np.max(array))
"""
Prints the largest element present in the array.
Same as array.max()
Output: 10
"""

print(np.min(array))
"""
Prints the smallest element present in the array.
Same as array.min()
Output: 0
"""

print(np.sin(array))
"""
Prints the sine of all the elements present in the array.
Output:
[ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
 -0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
"""

print(np.log(array))
"""
Prints the log of all the elements present in the array.
Since log(0) is not defined, it prints -inf and gives a Runtime Warning.
Warning (from warnings module):
  File "C:/Users/ankit/Desktop/Lec21_NumPy_Operations.py", line 122
    print(np.log(array))
RuntimeWarning: divide by zero encountered in log
Output:
[      -inf 0.         0.69314718 1.09861229 1.38629436 1.60943791
 1.79175947 1.94591015 2.07944154 2.19722458 2.30258509]
"""

"""
There are a lot of functions in NumPy like these. These functions can be referred
from:
https://docs.scipy.org/doc/numpy/reference/ufuncs.html
"""
