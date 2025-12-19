#Creating a Dictionary from Two Lists

keys = ["name","age","location"]
values = ["sama",22,"mansoura"]
dictionary = {}

for i in range (len(keys)):
    dictionary[keys[i]] = values[i]
print(dictionary)    
