#set
#1)Find the union, intersection, difference (A - B and B - A), and symmetric difference.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union = A.union(B)
#(or) union=A|B
print(union)


intersection = A.intersection(B)
#(or) intersection=A&B
print(intersection)

difference = A.difference(B)
#(or) A-B
print(difference)


difference2=B.difference(A)
#(or) B-A
print(difference2)

#2)Check whether the number 3 is in set A and 6 in set B.
print(3 in A)
print(3 in B)

#3)remove duplicates using a set
values=[1, 2, 2, 3, 4, 4, 5]
print(set(values))

#4)Take a sentence from user input and return a set of unique words (ignoring punctuation and case).
userinput=input("enter anything : ").lower()
print(set(userinput))

#5)Given three sets of students who play football, basketball, and tennis,write a program to find:

#Students who play all three sports

#Students who play only one sport

#Students who play exactly two sports

football={"one","two","three"}
basketball={"two","six","four"}
tennis={"six","one","four"}

all=football|basketball|tennis
print(all)

footballOnly=football-(basketball | tennis)
print(footballOnly)
