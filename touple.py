#One of the main differences between lists and tuples in Python is that tuples are immutable, that is, one cannot
#add or modify items once the tuple is initialized. For example

a=()
print(type(a))

m=tuple('mantasha')
print(type(m))

t=tuple('lupins')
print(t)
print(tuple(range(4)))

# tuple are immutable that's why it can not be change

t=(1,2,3)
#t[0]=3   # Can not modify this element...
print(t)

# Joining tuple
print("Joining two tuple: ")
tp=(1,2,3)
qt=tp
tp+=(5,6)
print(tp)

print(tp[2])

# Various built in function in tuple...
print("max: ", max(tp))
print("Min: ",min(tp))
print("Sum: ",sum(tp))
print("Length: ",len(tp))

# reversing the tuple
print("Printing the tuple in reverse order:")
rev=tuple(reversed(tp))
print(rev)

s=lambda x,y:x+y

print(s(5,4))