#handle single error...
try:
    age=int(input("Enter your age: "))
    print(age)
except ValueError:
    print("handle")

#handle multiple error

#input adfsd
#input 0
try:
    num=int(input("Enter any number:"))
    result=100/num
    print(result)
except ValueError:
    print("Value handle")
except ZeroDivisionError:
    print("zero division handle")

