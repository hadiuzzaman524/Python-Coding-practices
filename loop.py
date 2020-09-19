for i in range(3):
    print(i)
else:
    print("finish for loop")
x=0
while(x<10):
    print(x)
    x+=1
else:
    print("finish while")

# use of pass keyword

for i in range(10):
    if(i==5):
        pass # it just skip this state
    else:
        print(i,end="")