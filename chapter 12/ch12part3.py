# raising exceptions
def increment(num):
    try:
        return int(num) + 1 
    except:
        raise ValueError("this is not good jatin")    

a = increment("45")
print(a)































