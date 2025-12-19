#Finding the Maximum Value in a List

List = [10,20,30,40,50]
max_num = List[0]

for num in List:
    if num > max_num:
        max_num = num
print("The maximum number is:" , max_num)        
