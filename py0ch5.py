'''py0ch5 2,2,1
loops
loops are functions you can use to repeat a task
the two loops you can use are while loops and for loops.
WHILE loops carry out an action as long as a certain requirment is met
all loops must have a tab on the action, similar to control flow'''
#while loops 5.1
a=0
while a<=5:#as long as a<=5,a will keep getting bigger
    print(a)
    a+=1
#"a+=1" is the fancy way of saying "a=a+1" or "add 1 to a"
#while loops can be used for other things like "while n is true" or "while type==str"
print("new loop")

#for loops 5.2
#the next type of loop is for loop
#for loops are useful for going through cycles like this:
for num in range(0,11):#0 is where ot starts, so11 is the limit, so it wont meet or exceed 11
    print(num)
#if you want to try different for loop variations: try this method:(start,stop,step)
print("new loop")
for i in range(0,11,2):#the 'step' is 2, so it counts by 2 each iteration stopping at 10
    print(i)
