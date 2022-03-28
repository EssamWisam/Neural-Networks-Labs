#Python has no command for declaring a variable.
""" Python ignores strings that are not assigned. This can even be multiline"""

def myfunc():
    global x              #to create/declare a global variable inside a function we need this first.
    x = 5+3j              #The type of this variable is complex.
    #The type can be explicitly specified using the constructor, the same applies to conversions.
    x = str("Hello World")
    x = int(20)	
    x = float(20.5)		
    x = complex(1j)
    x = list(("a", "b", "c"))	    #["a", "b", "c"] ordered, changable
    x = tuple(("a", "b", "c"))	    #("a", "b", "c") ordered and unchangeable
    x = set(("a", "b", "c"))        #{"apple", "banana", "cherry"} no duplicates allowed.
    x = dict(name="John", age=36)	#{"name" : "John", "age" : 36} like JS objects
    x = range(6)	                #sequence from 0 to 5, generally: range(start, stop, step)
    x = frozenset(("a", "b", "c"))  #Pretty much an immutable set
    x = bool(5)	                    #x = "free" in "The best things in life are free!" (x=True), also works with arrays
    x = bytes(5)		           
    x = bytearray(5)		
    x = memoryview(bytes(5))    

def slicing():
    stringo="Every one needs a break."
    a=2
    b=3
    x = stringo[a:b]    #from a to b-1 can also use negative indexing.
    x = stringo[:]     #from 0 to length(stringo)-1
    x = stringo [:-1]  #All elements except the last (till -2 only)
    x.split(" ")       #gives you an array by splitting at space x = ["Every","one", "needs", "a", "break"]
    x.strip()          #removes any whitespace
    x.replace("Every one", "Each one")
    x.upper()
    y = "I want {} pieces of item {} for $20 dollars."
    x = y.format(a, b)
    A = "I have a {carname}, it is a {model}."
    print(A.format(carname = "Ford", model = "Mustang"))
    #There are many string methods, all of them return new values.
    #bool(something) is True unless its an empty data structure, string, 0 or None (False)
    #Unlike x == y, x is y only returns true if x and y are the same object (x=y or y=x was true at some point)
    if a > b: print("Done.")
    print("a") if a > b else print("b")
    #for loops and while loops can be followed up with an else for whenever the condition becomes false.
    #if you break from the loop you don't go to the else.

def listMethods():
    L = ["A", "B", "C"]
    L.append("D")
    L.insert("X",0)                             #L[0]="X" and everything beyond is pushed further by one step.
    L.extend(L)                                 #appending L on itself.
    L.remove("B")
    del L[0]                                    #to remove a specified index, del L deletes the entire list
    L.clear()
    #List comprehension:
    Y = [x for x in L if "A" in x]              # Generally, Y = [f(x) for x in iterable if condition] 
    # Y = [f(x) if B(x) else g(x) for x in L]
   
def my_function(*args):                         #Receiving any number of arguments (tuple of arguments)
  print("The second argument. " + args[2])
#if we pass [1, 2, 3] args[0] = 1 and so on (unpacked
# )
def my_function(**kargs):                       #receiving any number of keyword arguments (dictionary of arguments)
  print("The address is " + kargs["Address"]);
  x = lambda a, b, c : a + b + c
  y = x(5, 6, 2)

#A function returning another
def myfunc(n):
  return lambda a : a * n
x = (myfunc(3))(2)

#Conventially. If a variable is called _ then it's a throwaway variable (not actually used.)
class Dragon:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    #x and y are attributes of any object self is this object.

Jax = Dragon(10, 36)
print(Jax.x) 
print(Jax.y)
del Jax
#Create a child class. It can access the parent's methods.
class ElderDragon(Dragon):
 #The child's init overrides the parent's init by default, unless:
  def __init__(self, x, y,z):
    Dragon.__init__(self, x, y)
    self.z=z
 #Or alternatively
  def __init__(self, x, y,z):
    super().__init__(x, y)
    self.z=z
    #We can use super() to access any of the parent's methods (we can already use the child class as well, except for the constructor)


#Iterators
Stringo = 'Python'       #Iterable object
itr = iter(Stringo)     #iterator
 
while True:
    try:
        # Iterate by calling next
        x = next(itr)
        print(x)
    except StopIteration:
        # exception will happen when iteration will over
        break

import Light as Li       #Seperate python file
Li.emit()                #this is how to use a function from that file.

import numpy
x = dir(numpy)
#lists all defined names belong to numpy (includes all methods)
print(x)
#Python has built in dates.


import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
#Now it's a dictionary
print(y["age"])
#Back to JSON:
x = json.dumps(y)


#Exception Handling:
try:                                                           
  f = open("demo.txt")
  f.write("Lorum Ipsum")
except:                                                        #If an error was raised (can have multiple excepts with specifying the triggering error)
  print("Something went wrong when writing to the file")
else:                                                          #If no errors were raised.
  print("Success")
finally:                                                       #Do this anyway.
  f.close()                                                    #Even if an error occurs in excpt this runs. Or even if the except include a return statement.
  x = -1
  #if x < 0: raise Exception("Sorry, no numbers below zero")   #To raise an exception.

#Numpy
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#Each ],[ breaks the line
print(arr.ndim)             #no. of dimensions in an array.
print(arr.shape)            #(2,2,3)
#Dimension
print(arr[0, 1, 2]) #Outside in (6).
#Slicing: 
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])                                    #0:2 means whole outer array, 1:4 slices each inner array.
print(arr(...,-1))                                   #printing the last column. The ... mean as many :, :, : as necessary (useful for accessing the innermost dimension)
print(arr(...,[-1]))                                 #printing the innermost dim as a column (not as a row)
 #Copy vs View
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()          #change x changes arr and vice versa
y = arr.copy()          #y and arr are independent
#Reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)                               #Need that 2x3x2=12. Returns a view. 
newarr = arr.reshape(2, 2, -1)                              #-1 means Numpy will calculate the value for us to make the rshape possible.
newarr = arr.reshape(-1)                                    #makes it flat

#Instead of nesting n loop layers for n dimensions:
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))       #concatenate (merge)
arr = np.vstack((arr1, arr2))       #each is a row

Q = np.random.randn(4, 3)           #random matrix (standard normal; moslty near zero) of dimensions y 4x3
Z = np.dot(x, y)                    #If x and y are two matrices then it multiplies them. If they are 1D vectors 

import random
mylist = [1, 2, 3]
random.shuffle(mylist)            #shuffles the original list.

#More notes
#Looping on two arrays simultaneously.
A = [1, 2, 3]
B = [2, 5, 7] 
z = [x+y for x, y in zip(A, B)]

#np.argmax(A) returns the index with the largest no. (as if the array was flat)
A = np.matrix([[1,2,3,33],[4,5,6,66],[7,8,9,99]])
np.argmax(A)

#In Python, a backslash ( \ ) is a continuation character

#String formatting (Python 3.6+)
x = 3
y = f"Why just {x}?"

#Unpacking
tup = (1, 2, 3, 4, 5)
a, b, c, d, e = tup #a = 1, b = 2 and etcetra
# doing this with a dictionary gives you the keys.
# dic.values for the values and dic.items for tuples including both.
#popular use x, y = coordinates

#Multiple assignments:
a, b = 20, 30
#inline swap
a, b =b, a

#can nest loops to produce one collection (e.g. list)
#2D list comprehension:
x = [i for i in range(3) for j in range(2)]
#[[0, 1, 2], [0, 1, 2]]
#Dictionary Comprehension
sentence = "GGWP"
x = {char: sentence.count(char) for char in set(sentence)}
#each letter against it's no. of appearances
#dict_variable = {key:value for (key,value) in dictonary.items()}


#multiplying collections/strings by a scalar n repeats content inside n times.

names = ["John", "Jax", "Sam"]
ages = [993, 238, 450]
jobs = ["Dr", "Eng", "Vet"]
info = list(zip(names, ages, jobs)) #converting the zip object into a list.
#each element in info is a tuple e.g. ("John", 993, "Dr")
#can be also used with unpacking and list comprehension. Or alternatively use range on both.

#while/for else. If they break they don't trigger it (otherways they do >> not found)

#custom sort
lst.sort(key = sortFun) #sortFun returns some manipulation of x (element in lst)
#it will be sorted ascendingly w.r.t what sortFun returns for each element xinn lst.

#chain lists or accumulate a list using itertools

#zip and range use lazy evaluation in python 3.x (return lazy iterables)
#either use list() or list comprehension to see eveythingß



#with:
#The with statement is used to wrap the execution of a block with methods defined by a context manager
#e.g. make a file be automatically closed when outside the with block/exception arises.
with open('file_path', 'w') as file:
    file.write('hello world !')
#automatically closed.


#free counter while looping:
values = ["a", "b", "c", "d", "e"]
for count, value in enumerate(values):
  print(count, value)