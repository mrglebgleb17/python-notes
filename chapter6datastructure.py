'''py0ch6 2.5,3,2
data structures
there are many ways we can store more than one values of data, let's start with lists...
a list can be indicated using brackets like these []'''
fruits=["apple","banana","kiwi","blueberry"]#it's helpful to use a plural,like "cars" instead of "car"
'''in a list, each item is seperated by a comma
the position an item is in the list is called the index.
the index starts with zero, so "apple" would have an index of 0,"banana" would have an index of 1, and so on
you can access a value in the list based on it's index
ex:'''

#lists 6.1
print(fruits[1])#banana is index #1,so it will print banana
a=fruits.index("apple")#this can print the index of an item in the list,however if you do this with an item that
#is not in the list, then there is an error
print(a)
#we can add an item to the list with the .append() function
fruits.append("orange")
print(fruits)
#we can delete an item wiht the .remove() function
fruits.remove("orange")
print(fruits)

#dictionaries 6.2
#dictionaries are like lists but they store 2 items in a slot
#examples of this could be item:price
items={"ice cream":3,"apples":2,"candy":1}
print(items["ice cream"])#this code ask for the key(ice cream) and then shows the value(price)
#this could be useful for storing IDs and passcodes
users={"tim":"Password_1","person123":"123456"}
print(users["person123"])

#sets 6.3
#a set is a data structure that has no odrer,and can't have duplicates
set_example={"banana","orange","orange","apple"}
print(set_example)
#in sets, instead of .append(),we use .add()
#we can combine two sets using union:
#set1.union(set2)
