d={'jaman':233, 'mantasha':'fucker girl'}
print(d['jaman'])
print(d['mantasha'])

# if not available in dictionary then showing error
# for avoid this error can be use get() method
#print(d['orpi'])
print(d.get('orpi','love u'))
#now remove the error

mydic={'a':5,'b':8,'c':2}

for key in mydic:
    print(key , mydic[key])

#use of item() function
print("Use of item() function:")
for key,value in mydic.items():
    print(key,value)

#assigning a new value in dictionary
mydic['mustarin']='.... you'
print(mydic)

#marging two dictionary....

dict1={'a':1,'b':2,'c':4}
dict2={'d':23,'3':44}

#problem 1:
# input--> 1234
# output --> one two three four

d={1:'one',2:'two',3:'three',4:'four'}
var=input()
for i in var:
    print(d[int(i)])
