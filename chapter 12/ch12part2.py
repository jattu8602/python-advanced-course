# handling different exceptions
try:
    a = int(input("enter a number"))
    c = 1/a
    print(c)
except ValueError as e:
    print("please enter a valid value")    
    print(e)
except ZeroDivisionError as e:
    print("make sure u r not dividing by zero")    
    print(e)
print("thanks for using this code!")



































