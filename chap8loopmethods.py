#py0ch7 4,2,2,2
#nesting loops,break and continue
#in python, if we want to use 2 loops at the same time,there is a way to do that.
#the most common way is to nest loops.
#ex:
for i in range(1,4):
    for j in range(1,3):
        print("hip")
    print("hooray")
print("new loop")
#in case we have an infinite loop, but we need some way to break out of it, we can use the 'break'command
apples=0
print("an apple is 2 dollars")
while True:
    b=input("take another apple? y/n ")
    if b=="y":
        apples+=1
        print("you have",apples,"apples")
    elif b=="n":
        print("you have",apples,"apples. ")
        print("you have to pay",apples*2,"dollars")
        break
    else:
        print("invalid answer")
        continue


