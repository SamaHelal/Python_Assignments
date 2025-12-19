#Validating User Input with While Loop
while True:
    username=input("Enter a username:")
    if len(username) >= 4:
        print("username accepted")
        break
    else:
        print("Please try again")
        
