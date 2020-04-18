"""
Ankit Singhal - as.ankitsinghal.7@gmail.com
Python for Data Science and Machine Learning Bootcamp - Udemy
Lecture 20: NumPy Array Indexing
"""
import numpy as np
array = np.arange(0,11)
print(array)
"""
array = [ 0  1  2  3  4  5  6  7  8  9 10]
"""

print(array[8])
#It will print the number present at index 8 i.e., 8.

print(array[1:5])
"""
Prints all the elements starting from index 1 upto index 5 (not including 5)
Output: [1 2 3 4]
"""

print(array[:6])
"""
Prints all the elements upto index 6. (not including 6)
Output: [0 1 2 3 4 5]
"""

print(array[5:])
"""
Prints all the elements starting from index 5.
Output: [ 5  6  7  8  9 10]
"""

print(array[:])
"""
Prints all the elements of the array.
Output: [ 0  1  2  3  4  5  6  7  8  9 10]
"""

array[:7] = 700;
print(array)
"""
Changes the value of all the elements upto index 7 (not including 7) to 700;
Output: [700 700 700 700 700 700 700   7   8   9  10]
"""

array = np.arange(0,11);
#Very Important Concept:
slice_of_array = array[1:8]
print(slice_of_array)
"""
slice_of_array = [1 2 3 4 5 6 7]
"""
slice_of_array[:] = 100;
print(slice_of_array);
print(array);
"""
slice_of_array = [100 100 100 100 100 100 100]
array = [  0 100 100 100 100 100 100 100   8   9  10]

So, any change in slice_of_array is also creating a change in the original array.
This is happening because slice_of_array is just a viewing option of the original
array. slice_of_array is not a different entity. That's why any change in
slice_of_array will also create the same change in original array.
"""

array = np.arange(0,11);
#To overcome this, we can use the copy function.
array_copy = array.copy()
print(array_copy)
"""
Output: [ 0  1  2  3  4  5  6  7  8  9 10]
"""
array_copy[:] = 700;
print(array_copy)
print(array)
"""
Output:
array_copy = [700 700 700 700 700 700 700 700 700 700 700]
array = [ 0  1  2  3  4  5  6  7  8  9 10]
Clearly, making changes in the array_copy doesn't affect the original array at all.
"""

array_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(array_2d)
"""
array_2d =
[[ 5 10 15]
 [20 25 30]
 [35 40 45]]
"""

element = array_2d[0][1]
print(element)
"""
This is double bracket notation for accessing elements from a matix.
It will print the element present at 0th row and 1st column of array_2d
Output: 10
"""

row = array_2d[2]
print(row)
"""
It will print the 2nd row of array_2d
Output: [35 40 45]
"""

element = array_2d[1,1]
print(element)
"""
This is single bracket notation for accessing elements from a matix.
It will print the element present at 1st row and 1st column of array_2d
Output: 25
"""

subMatrix = array_2d[:2,1:]
print(subMatrix)
"""
It will grab zeroth and first rows & 1st and 2nd columns of array_2d.
:2 means all the rows upto row 2 (not including row 2).
1: means all the columns starting from column 1.
Output:
[[10 15]
 [25 30]]
"""

subMatrix = array_2d[:2]
print(subMatrix)
"""
It will grab zeroth and first rows & all the columns.
:2 means all the rows upto row 2 (not including row 2).
Output:
[[ 5 10 15]
 [20 25 30]]
"""

subMatrix = array_2d[1:,0:2]
print(subMatrix)
"""
It will grab first and second rows & zeroth and first columns.
1: means all the rows starting from row 1.
0:2 means zeroth and first columns.
Output:
[[20 25]
 [35 40]]
"""

array = np.arange(1,11)
print(array)
"""
array = [ 1  2  3  4  5  6  7  8  9 10]
"""
bool_array = array>5
print(bool_array)
"""
bool_array will give an array of boolean values according to the condition.
since first five elements are not greater than true, first five boolean values
are false and last five boolean values are true.
bool_array = [False False False False False  True  True  True  True  True]
"""

print(array[bool_array])
"""
prints all the elements of array which were true according to the condition of
bool_array.
"""

print(array[array<5])
"""
prints all the elements of the array which are less than 5.
Output = [1 2 3 4]
"""

array1 = np.arange(26)
print(array1)
"""
array1 = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25]
"""

print(array1[array1>=10])
"""
prints all the elements of array1 which are greater than or equal to 10.
Output: [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25]
"""
