#Generating a Fibonacci Sequence

n=10
a=0
b=1
fib_seq=[]

while len(fib_seq) < n :
    fib_seq.append(a)

    next_number = a + b
    a = b
    b = next_number

print("Fibonacci Sequence:", fib_seq)    
    
