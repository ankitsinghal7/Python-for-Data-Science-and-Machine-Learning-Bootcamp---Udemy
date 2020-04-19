"""
Ankit Singhal - as.ankitsinghal.7@gmail.com
Python for Data Science and Machine Learning Bootcamp - Udemy
Lecture 26: Series
"""
import numpy as np
import pandas as pd
#importing numpy and pandas library

labels = ['a','b','c']
my_data = [10,20,30]
#2 lists: labels and my_data

array = np.array(my_data)
#converting list into array

d = {'a':10,'b':20,'c':30}
#dictionary d with labels a,b,c & corresponding values 10,20&30

print(pd.Series(data = my_data))
"""
It will print the list (my_data) as a series along with the indexes.
Output:
0    10
1    20
2    30
dtype: int64
"""

"""
Now, we can specify our indexes also. For example we want a,b,c as our indexes.
For that, we can write:
"""
print(pd.Series(data=my_data,index=labels))
"""
Output:
a    10
b    20
c    30
dtype: int64
"""

"""
We can obtain the same output without writing "data" and "index" specifically as
shown below:
"""
print(pd.Series(my_data,labels))
"""
Output:
a    10
b    20
c    30
dtype: int64
"""

"""
We can also use NumPy arrays instead of python lists to obtain the series.
"""
print(pd.Series(array,labels))
"""
Output:
a    10
b    20
c    30
dtype: int32
"""

"""
Along with python lists and NumPy arrays, we can also use dictionary to obtain
lists. In case of dictionary, we need not to mention index seperately. It will
use the dictionary keys as index.
"""
print(pd.Series(d))
"""
Output:
a    10
b    20
c    30
dtype: int64
"""

"""
Various types of data can be stored in a pandas series as shown below:
"""
print(pd.Series(data=labels))
"""
Output:
0    a
1    b
2    c
dtype: object
"""
print(pd.Series([sum,print,len]))
"""
Output:
0      <built-in function sum>
1    <built-in function print>
2      <built-in function len>
dtype: object
"""

"""
The key to using a Series is understanding its index. Pandas makes use of these
index names or numbers by allowing for fast look ups of information (works like
a hash table or dictionary).Let's see some examples of how to grab information
from a Series:
"""
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
print(ser1)
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])
print(ser2)
"""
ser1:
USA        1
Germany    2
USSR       3
Japan      4
dtype: int64

ser2:
USA        1
Germany    2
Italy      5
Japan      4
dtype: int64
"""

print(ser1['USA'])
"""
It will give the value stored corresponding to the index - 'USA'.
Output: 1
"""

print(ser1 + ser2)
"""
It will add the values from ser1 and ser2 which have same corresonding index.
Output:
Germany    4.0
Italy      NaN
Japan      8.0
USA        2.0
USSR       NaN
dtype: float64
Since USSR is not there in ser2 and Italy is not there in ser1, we have NaN
corresponding to them in the output. Also, after additon the values are converted
to float data type.
"""
