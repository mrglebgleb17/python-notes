'''
intermediate data structures
in python there are many ways we can go above and beyond using data structures
first,lets learn how to manipulate data structues'''
#intermediate lists 8.1
#when it comes to lists and dictionaries,there are a lot more we can do than just add and remove
#the first method is the copy function wich can copy a whole list
#this is useful when you have shared items on a list
#ex
fruits=['apple','banana','blueberry']
fruits_at_home=fruits.copy()
fruits_at_home.remove("banana")
print(fruits,fruits_at_home)
#count function
#the count function can be used to count items in a list
a=fruits.count("apple")
print(a)
a=fruits.count("soda")#it should be an error,but to not be anoyying python would just output 0
print(a)
#extend funtion
#the extend function can add a list to another list, and even put a list inside a list!
more_fruits=["orange","grape"]
fruits.extend(more_fruits)
print(fruits)
#intermediate dictionaries 8.2
#if we want to acess all the keys or values in a dictionary, we can use the keys or values function
items={"ice cream":3,"apples":2,"candy":1}
a=items.keys()
b=items.values()
print(a,b)
