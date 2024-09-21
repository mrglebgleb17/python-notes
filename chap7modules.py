'''py0ch10 2,2,2,2
modules
when using python using only lists and loops can be a little limiting,even though they are very useful
modules allow us to make GUIs with buttons, draw shapes,roll dice, and even acsess the internet!
what excactly is a module? a module is a small package of functions that can help you with a specific topic
to use a module,you first have to import it like this:
import modulename
'''
#webbrowser module 9.1
#to start this lesson off with some fun,lets start off with the webbrowser module!
#this is a simple program that just opens the python webpage
import webbrowser
webbrowser.open('https://python.org/')

#random module 9.2
#the second module we will learn is random
# we can use random in the following example that you should to run\
import random
a=["red","green","blue","yellow"]
b=random.choice(a)#this should give us a random item on the list
print(b)
#other funtions are:
print(random.randint(1,6))

#stats module 9.3
#if you want to perform more complex statistical functions in python, the statistics module is for you
import statistics
q=[1,2,3,4,5]
a=[1,6,2,9,3]
b=statistics.mean(q)#calculates the average of the items in "q"
c=statistics.median(a)#shows the median(middle number) of the items in a
print(b)
print(c)

#datetime module 9.4
#the datetime module is exactly how it sounds,it helps you with date and time functions
#the datetime module also has harder syntax than other modules
import datetime
a=datetime.date.today()#gives you today's date
b=datetime.datetime.now()#gives you today's date and time
print(a)
print(b)

