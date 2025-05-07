#1) List of movies
movies=["bahubali","court","kgf","endgame","rrr"]
print("first: ",movies[0])
print("last: ",movies[-1])

#2)Add a new movie to the list.Change the third movie to something else.

movies.append("chennai express")
movies[2]="sachin:a billion dreams"

#3)Sort the list alphabetically.Use append(), insert(), remove(), pop(), and reverse() on a sample list.
list1=["c","a","b","e","d"]
list1.sort()
print(list1)

list1.append("f")
list1.insert(0,"1")
list1.pop()
list1.reverse()
print(list1)

#4)Print each element in the list using a for loop.Print only the movies that start with the letter “S”.
for item in movies:
    print(item)

for item in movies:
    if item[0]=="s":
        print(item)

#5)Create a list of squares for numbers from 1 to 10.From a list of numbers, create a new list that contains only even numbers.
list2=[i**2 for i in range(1,11)]
print(list2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [num for num in numbers if num % 2 == 0]
print(even)