a={1,2,3,4,5}
b={6,7,8,9,5}

uni=set(a.union(b))
print("Union of two sets: ",uni)
inte=set(a.intersection(b))
print("Intersection of two sets: ",inte)
print("Set difference",a.difference(b))
print("Subset: ",a.issubset(b))
print("Disjoint; ",a.isdisjoint(b))

print(a&b) #intersection
print(a|b) #union
print(a-b) #set difference

A={1,2,3}
A.add(5) # add new element on the set
print(A)
A.discard(2) #remove a new element
print(A)
A.remove(3) #also remove a element
print(A)

A.update({4,6}) # update set to another set
print(A)

#set inside set

B={ frozenset({2,3}), frozenset({4,5})}
print(B)

#Method Operator
#a.intersection(b) a & b
#a.union(b) a|b
#a.difference(b) a - b
#a.symmetric_difference(b) a ^ b
#a.issubset(b) a <= b
#a.issuperset(b) a >= b

#check the set is empty or not
C={1,2,3}
D={4,5,6}
print(C&D==set()) # check the intersection of two set is empty or not
print(C|D==0) #also same working..
print(2 in C) # Check 2 is in C or not
print(len(C)) #return the len of C

from collections import Counter
A=Counter(['a','b','b','b','c',1])
#the Counter function return how many same element are there and count them into a set

print(A)

