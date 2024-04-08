#                                            Python  Practice


# Boolean and Logical Operators

my_str="Byomkesh123"

print(my_str.isalnum()) #check if all char are numbers

my_str.isalpha()   #check if all char are in the string are alphabetic

print(my_str.istitle())

str_ex="Hello world"

my_str.isalpha() or str_ex.isalnum()

# Lists

### A list is a data structure in python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square bracket [ ].

lst_example=[]

type(lst_example)

lst=['Math', 'CHem', 12, 34, 540]

len(lst)

## Append

# Append is used to add items in the list
lst.append("History")

lst

lst.append(['Bio',"Geo"])

## Indexing in list
lst[3]

lst[5]

lst[:]

lst[2:]

lst[:2]

lst[2:5]

lst*5

## Insert

lst.insert(2,"Evs")

lst

## Extend

lst1=[2,3,4,5,6,7]

lst1.extend([8,9])

lst1

## Various operations that we can perform in list

lst2=[3,4,6,7,9]

sum(lst2)

## Pop( ) Method

lst2.pop()

lst2

lst2.pop(0)

lst2

## count( ) : Calculate total occurance of given element of list

lst3=[3,3,3,5,7,88,9,99,9,88,65,3]

lst3.count(3)

# Length : calculates total length of list
len(lst3)

# index() : returns the index of first occurance. Start and end index are not neccessary parameters
lst3.index(3,0,2)

# Min & Max
min(lst3)

max(lst3)

## Sets
### A set is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python's set class represents the mathematical notion of a set. This is based on a data structure known as a hash table. Set doesn't support indexing.

## Designing an empty set
set_var = set()
print(set_var)
print(type(set_var))

set_var={"Avengers", "Ironman", "Thor"}
print(set_var)
type(set_var)

set_var1={1,2,3,4,2,3,5}
set_var1

## inbuilt functions of set
set_var.add("Hulk")
set_var

## interception
set1={"Avengers", "Ironman", "Thor"}
set2={"Avengers", "Ironman", "Thor","Black Panther"}
set2.intersection(set1)

## intersection update
set2.intersection_update(set1)
set2

## difference
set1={"Avengers", "Ironman", "Thor"}
set2={"Avengers", "Ironman", "Thor","Black Panther"}
set2.difference(set1)

## difference update
set2.difference_update(set1)
set2

## Dictionaries
### A Dictionary is a collection of data type which is unordered, changeable and indexed. In python, It is written with curl brackets and they have keys and values.

## lets create a dict
my_dict = {"Car1" : "Marcedes", "Bike1" : "Apache","Car2" : "BMW", "Bike2" : "PULSAR"}
my_dict

## Access the item values using keys
my_dict["Car"]

my_dict["Bike"]

## We can even throughout the dictionary keys
for x in my_dict:
    print(x)

## We can even throughout the dictionary values
for x in my_dict.values():
    print(x)

## We can even throughout the dictionary keys and values
for x in my_dict.items():
    print(x)

## adding items in dictionary
my_dict["Car3"]="Audi"
my_dict["Bike3"]="KTM"
my_dict

## Nested Dictionary

car1_model={"Marcedes" : 1960}
car2_model={"BMW" : 1985} 
car3_model={"Ferrari" : 1956}
car_type = {"car1" : car1_model, "car2" : car2_model, "car3" : car3_model}
car_type

## accessing the items in the dictionary
print(car_type["car2"])

print(car_type["car1"]["Marcedes"])

## Tuples
### Tuples are immutable. It is used within round braces. It doesn't support item assignment. It is only used to define an item for one time.

my_tuple = ("Byomkesh", "Sayan", "Arnab")
my_tuple[0]

print(type(my_tuple))

## inbuilt functions
my_tuple.count("Byomkesh")

my_tuple.index("Sayan")


# Libraries

## 1. Numpy
### Numpy is a general-purpose array processing package. It provides a high performance multidimentional array object, and tools for working with these array. It's the fundamental package for scientific computing with python.

## What is an Array ?
### An array is a data structure that stores values of same data type. In python, this is the main difference b/w arrays and lists. While python lists can obtain values corresponding to different data types, arrays in python can only contain values corresponding to same data type.

## initially let's import numpy
import numpy as np

my_lst4=[1,2,3,4,5]
arr=np.array(my_lst4)
arr

type(arr)

print(arr)

## inbuilt function to find how many row and columns are there
arr.shape

my_lst4=[1,2,3,4,5]
my_lst5=[2,5,8,9,1]
my_lst6=[1,9,8,4,7]
arr1=np.array([my_lst4,my_lst5,my_lst6])
arr1

arr1.shape

arr1.reshape(5,3)  ##make sure the number of elements are not changed

## Indexing

## Accessing the array elements
arr2=np.array([1,2,3,4,5])

arr2[2]

my_lst4=[1,2,3,4,5]
my_lst5=[2,5,8,9,1]
my_lst6=[1,9,8,4,7]
arr1=np.array([my_lst4,my_lst5,my_lst6])

arr1[1:,3:]

arr1[0:2,1:3]

arr1[1:,2:4]

arr1[1:2,1:4]

arr1=np.arange(0,10)

arr1

arr1=np.arange(0,10,step=2)
arr1

np.linspace(1,10,50)

## Copy() Function And Brodcastng
arr2=arr1
arr2[3:]=100
arr2

arr1

arr2=arr1.copy() ## Copy() function is basically creating an another memory space for arr2
print(arr1)
arr2[3:]=500
print(arr2)

print(arr1)

## Some conditions are very useful in exploratory data analysis
val=2
arr1[arr1<2]

arr1*2

## create arrays and reshape
np.arange(0,10).reshape(5,2)

## random distribution
np.random.rand(3,3)

np.random.randn(4,4)

np.random.randint(0,100,8).reshape(4,2)

np.random.random_sample((1,5))

