#Tuple
#1)Write a Python program to create a tuple containing five different data types:
# integer, string, float, list, and another tuple.
tuple1=(1,"two",3.0,[4,7],(5,3))
print(tuple1)

#2)write Python code to:Print the second element.,Print the third element’s second item.

my_tuple = ('apple', [10, 20], (1, 2, 3), 4.5, 'banana')
print(my_tuple[1])
print(my_tuple[2][1])

#3)Explain why the following code produces an error and correct it:
my_tuple1 = (1, 2, 3)
my_tuple1[1] = 4

# here we are trying to insert 4 at 1st index position in to a tuple. as tuples are immutable, insertion is not possible.

#4)Unpack the tuple
coordinates = (45.4215, -75.6972)
(lattitude, longitude) = coordinates
print(lattitude, longitude)

#5)Write a function that takes two tuples of integers and returns a new tuple with the element-wise sum.
def func(tuple2,tuple3):

   return tuple(tuple2[i]+tuple3[i] for i in range(len(tuple2)))

newtuple=func((1,2,3),(4,5,6))
print(newtuple)
