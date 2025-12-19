#Generating a Multiplication Table for a Given Number

num=int(input("Enter a number:"))
limit=12

for i in range(1 , limit + 1):
    print(f"{num} X {i} = {num * i}")
