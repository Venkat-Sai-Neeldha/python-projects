#Dictionary
#1). Task: Write a function that takes a string and returns a dictionary with word counts.
def functon(string):
    list1=string.split(" ")
    dict = {}
    for char in list1:
        dict[char] = dict.get(char, 0) + 1
    return dict

dictionary=functon( "apple banana apple orange banana apple")
print(dictionary)

#2)Write a function to merge two dictionaries. If a key exists in both, sum their values.
dict1 = {'a': 5, 'b': 3}
dict2 = {'b': 2, 'c': 7}
for key, value in dict1.items():
    if key in dict2.keys():
        dict2[key] = value + dict2[key]
    else:
        dict2[key] = value
print(dict2)

#3)Invert a dictionary
dict3={'a': 1, 'b': 2, 'c': 1}
def function(dictionary):
    dict4={}
    for key, value in dictionary.items():
        if value in dict4:
            dict4[value].append(key)
        else:
            dict4[value]=[key]
    return dict4

print(function(dict1))

#4)Most Frequent Value
dict5={'Alice': 25, 'Bob': 30, 'Charlie': 25, 'David': 30, 'Eva': 25}
dict6 = {}
maxvalue=0
maxnumber=0
for char in dict5.values():
    dict6[char] = dict6.get(char, 0) + 1

for k, v in dict6.items():
    if v > maxvalue:
        maxvalue = v
        maxnumber = k
print(maxnumber)

# Write a function that takes two lists and creates a dictionary using elements from one as keys and the other as values.
def function1(list3,list4):
    dict7={}
    for i in range(len(list3)):
        dict7[list3[i]]=list4[i]
    return dict7

print(function1(['name', 'age', 'city'],['Alice', 25, 'New York']))




