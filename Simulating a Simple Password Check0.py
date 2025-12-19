#Simulating a Simple Password Check0
correct_password = "samahelal"
attempts = 3

while attempts > 0:
    password = input("Enter a password")
    if password == correct_password:
        print("correct password")
        break
    else:
        attempts -= 1
        print(f"incorrect password, You have {attempts} attempts left ")
else:
    print("Access denied, You have used all attempts")
    
    
