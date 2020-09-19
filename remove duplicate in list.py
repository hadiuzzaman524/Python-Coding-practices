numbers=[1,2,2,2,3,4,5,6,6]
num=[]
for i in numbers:
    if i not in num:
        num.append(i)

print(num)
#another way to inserting a list into set
print(set(numbers))

#Unpacking the list item
print("Unpacking list: ")
num=[1,2,3,4]
a,b,c,d=num
print(a,b,c,d)
