#find numbers which are divisible by 7 and multiples of 5, between 1500 and 2700

result = []
for num in range(1500,2700):
  if num % 7 == 0 and num % 5 ==0:
    result.append(str(num))
print(result)
