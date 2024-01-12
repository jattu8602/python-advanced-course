# try
while(True):
    print("press q to quit ")
    a = input("enter a number")
    if a == 'q':
        break
    try:
        print("trying......")
        a = int(a)
        if a>6:
            print("you entered a number gerater than 6")
    except Exception as e:
        print(f"your input resulted an error {e}")        
print("thanks for playing this game")

































