#Finding Common Elements in Two Lists

list1 = [10,20,30,40,50]
list2 = [20,40,60,80,100]
common_elements = []

for item in list1:
    if item in list2:
        common_elements.append(item)

print("common elements:", common_elements )        
