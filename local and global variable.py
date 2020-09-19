
x=10 #global variable
def fun():
    y=20
    global x #decleare x is global for editing privious declerating x
    #otherwise it working with local variable
    x+=1
    global m #declere as global for accessing anywhere
    m=40
    n=32 #local variable......
    return y

print(x)
print(fun())
print(x)
print(m)
#print(n)
#can not access here because n is local variable..

# use of del operation...............

print("Use of del: ")
global_var=20

def show():
    global_var=30
    print(global_var)

show()
del global_var # deleting a global variable
#print(global_var)
# now showing the error for undecleare variable

print("print all in global scope:")
print(globals().keys())
print("print everything in local scope:")
print(locals().keys())
