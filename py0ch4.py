'''py0ch4 2,2,3
control flow
control flow is something we can use as an algorythim
if statement 4.1
ex IF this,then that,ELSE-do this
the action must be a tab(4 spaces) behind a conditional'''
a=1
b=2
if a>b:#conditional
    print("1 is greater than 2")#action
else:
    print("2 is greater than 1")
'''in operations we can use <= for less than or equal to and >= for greater than or equal to.    
we can use ELIF statements if there are more than on outcomes
elifs and else 4.2'''
c=input("what is your age")
if c==100:
    print("you are old")
elif c==0:
#we use double equals signs if we are checking if it's equal to something.
    print("you are young")
else:
    print("that is something.")

# try and except 4.2
# if we want to peform a function, but are not sure if it will work, we can use try, and except
# these functions can recognize when something is wrong and wont give you an error if it is
password = input("give a number password")
try:
    a = int(password)  # it will "try" to turn the password into an integer,
    print(a)
except:
    print("invalid password")  # if the password contains a string charachter,it will return this instead of an error

