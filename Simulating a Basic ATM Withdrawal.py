#Simulating a Basic ATM Withdrawal

balance = 10000

while balance > 0:
    withdrawal = int(input("Enter amount:"))
    if withdrawal <= balance:
        balance -= withdrawal
        print("Withdrawal successful,Remaining Balance:", balance)
    else:
        print("Insufficient balance")
    if balance == 0:
        print("Balance is zero")
        break
