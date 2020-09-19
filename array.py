#Parameter Details
#b Represents signed integer of size 1 byte
#B Represents unsigned integer of size 1 byte
#c Represents character of size 1 byte
#u Represents unicode character of size 2 bytes
#h Represents signed integer of size 2 bytes
#H Represents unsigned integer of size 2 bytes
#i Represents signed integer of size 2 bytes
#I Represents unsigned integer of size 2 bytes
#w Represents unicode character of size 4 bytes
#l Represents signed integer of size 4 bytes
#L Represents unsigned integer of size 4 bytes
#f Represents floating point of size 4 bytes
#d Represents floating point of size 8 bytes
from array import *
myar=array('i',[1,2,3,4,5])
#here first parameter is type and second
#one is the list
print(myar[0])
print("inserting an element in the last index of array")
myar.append(10)
print(myar)
print("Inserting an element in specific index")
myar.insert(0,22)
print(myar)

#extend value of array or marging two array
myar2=array('i',[2,2,2,2])
myar.extend(myar2)
print(myar)
# remove the last element
myar.pop()
print(myar)
#remove 10
myar.remove(10)
print(myar)
#get the index
print(myar.index(5))
#reverse the array
myar.reverse()
print(myar)
