#py0ch11
#defining functions,lambda functions, args and kwargs
#in python,we use functions like print,input,if and else, but what if we made our own functions?
#using the define function,we can!
#ex:
#what if we wanted to make a function the asks for a number and counts up to that number?
import time
def numcount():#to define a function we have to make a name for it. This functions name is numcount.
    a=int(input("input a number for the counter"))
    b=1
    while b<=a:#this is a simple counting function that we learned in chapter 5.
        print(b)
        b+=1
        time.sleep(1)#I added this snippet just for you to see some more modules at work!
        #the code above basically says "wait one second after each number counted"
        
numcount()#this is called calling a function. If we don't call it,the above code will be useless and nothing will happen
'''
overall,functions are used if there is a piece of code you need to use a lot.
instead of writing that code over and over, you could just put it into a function and call the function when you need to use it!

another interesting part about functions is local variables.
a local variable is a variable that is inside of a function
a local variable cannot be called outside of a function
for example,
print(a) would give us an error because a is a local variable, and therefore is not accessible on the global scale
in a function, we can acctually declare a global variable
to do this, we put the word global before the variable we want to change'''
#taking arguments in a function
#when it comes to functions, somtimes they need to take a value in to output a result
#ex:
a=int(input("enter a number"))
b=int(input("enter a number"))
def sum_of_nums(num1,num2):
    print(num1+num2)#num1 and num2 are imaginary variables, and something will have to take the place of it
    
sum_of_nums(a,b)#a and b are sort of 'substituting' for num1 and num2.

