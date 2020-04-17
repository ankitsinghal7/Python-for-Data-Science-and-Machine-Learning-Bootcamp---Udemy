"""
Ankit Singhal - as.ankitsinghal.7@gmail.com
Python for Data Science and Machine Learning Bootcamp - Udemy
Lecture 18: NumPy Arrays
"""

my_list = [1,2,3]
print(my_list) #Prints [1, 2, 3]

#This is how we import NumPy library in python:
import numpy as np

#Casting python list as an array
arr = np.array(my_list)
print(arr) #Prints [1 2 3]

#For two-dimensional array:
my_list_2d = [[1,2,3],[4,5,6],[7,8,9]]
print(my_list_2d) #Prints [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr_2d = np.array(my_list_2d)
print(arr_2d)
"""
Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
2 sets of square bracket shows it is a 2-D Array/Matrix.
"""

print(np.arange(1,10))
"""
prints all the numbers starting from 1 upto 10 (not including 10) as a 1-D array
Output: [1 2 3 4 5 6 7 8 9]
"""

print(np.arange(1,10,2))
"""
prints all the numbers starting from 1 upto 10 (not including 10) with a step 2
as a 1-D array. Output: [1 3 5 7 9]
"""

print(np.zeros(5))
#prints a row of 5 zeros. Output: [0. 0. 0. 0. 0.]

print(np.zeros((3,4)))
"""
prints a 3*4 matrix with all the elements zero.
Output:
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""

print(np.ones(5))
#prints a row of 5 ones. Output: [1. 1. 1. 1. 1.]

print(np.ones((3,4)))
"""
prints a 3*4 matrix with all the elements one.
Output:
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
"""

print(np.linspace(0,5,10))
"""
prints 10 equally spaced numbers from 0 to 5 (both included)
Output:
[0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
 3.33333333 3.88888889 4.44444444 5.        ]
this function should not be confused with the arange function. Arange function
takes the third argument as the step size we want while the linspace function
takes the third argument as the number of numbers we want.
"""

print(np.eye(5))
"""
prints an identity matrix of dimensions 5*5.
Output:
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
"""

print(np.random.rand(5))
"""
prints 5 random numbers between 0 and 1.
Output:
[0.06885574 0.20491631 0.97446361 0.46280142 0.61586674]
Since, these are random numbers, we will get different set of numbers everytime
we run this command.
"""

print(np.random.rand(5,5))
"""
prints a 5*5 matrix having all the elements as some random numbers from 0 to 1.
Output:
[[0.93271189 0.10722422 0.13473093 0.28957934 0.79124808]
 [0.49874656 0.31485533 0.93051113 0.79310541 0.15304503]
 [0.93498244 0.40213935 0.58407065 0.00678348 0.64117537]
 [0.63692714 0.10764385 0.88536142 0.92182486 0.28065379]
 [0.55958992 0.50153797 0.02865784 0.71533145 0.52597996]]
"""

print(np.random.randn(5))
"""
prints 5 random numbers from a standard normal distribution centered around 0.
Output:
[-0.47884409 -0.03327672  0.17893226  1.04298643 -0.7958744 ]
"""

print(np.random.randn(5,5))
"""
prints a 5*5 matrix having all the elements as some random numbers from a
standard normal distribution centered around 0.
Output:
[[-0.38726371  0.59938003  0.38993535  0.4663299  -0.3150126 ]
 [-0.49304185  1.49578812 -0.5220242  -0.44238278 -2.03591059]
 [ 0.31286986 -0.53184095  0.45761281  0.52892968  1.35675602]
 [ 0.73141656  0.17486465  1.40827274 -1.02935511  0.99532912]
 [-1.04819895 -0.54835624 -0.03638653 -0.24571394  0.54512626]]
"""

print(np.random.randint(1,100,10))
"""
prints 10 random numbers between 1 and 100. (Including 1 and Excluding 100)
Output:
[84 61 70 35 26 51 40 57 21 39]
"""

array = np.arange(25)
print(array)
"""
arr = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]
"""
reshaped_array = array.reshape(5,5)
print(reshaped_array)
"""
This command reshapes the array into a matrix of dimensions 5*5.
Output:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
However, at all times we must make sure that the dimensions specified in the
reshape command satisfy the number of elements.
"""

random_array = np.random.randint(1,100,15)
print(random_array)
"""
random_array = [49 54 32 32 11  9 83 28 62 58 81  1 99 75 64]
"""
print(random_array.max())
# prints the maximum element present in random_array = 99
print(random_array.min())
# prints the minimum element present in random_array = 1
print(random_array.argmax())
# prints the index where maximum element is present = 12
print(random_array.argmin())
# prints the index where minimum element is present = 11

array = np.arange(25)
print(array)
"""
arr = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]
"""
print(array.shape)
# prints the dimensions of array = (25,). Single Array of 25 columns.
reshaped_array1 = array.reshape(25,1)
print(reshaped_array1)
"""
reshaped_array1:
[[ 0]
 [ 1]
 [ 2]
 [ 3]
 [ 4]
 [ 5]
 [ 6]
 [ 7]
 [ 8]
 [ 9]
 [10]
 [11]
 [12]
 [13]
 [14]
 [15]
 [16]
 [17]
 [18]
 [19]
 [20]
 [21]
 [22]
 [23]
 [24]]
"""
print(reshaped_array1.shape)
# prints the dimensions of reshaped_array1 = (25, 1).
# Single Column Array with 25 rows.
reshaped_array = array.reshape(5,5)
print(reshaped_array)
"""
reshaped_array:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
"""
print(reshaped_array.shape)
# prints the dimensions of reshaped_array = (5, 5). 5 rows and 5 columns

new_array = np.arange(5)
print(new_array)
#new_array = [0 1 2 3 4]
print(new_array.dtype)
#prints data type of the new_array = int32 (integer).









