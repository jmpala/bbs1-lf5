# list (repeated values) vs set (unique values)
myList = [0,1,2,3,4,5,6,7,8,9]
mySet = {0,1,2,3,4,5,6,7,8,9}

print("List: ", myList)
print("Set: ", mySet)

myList.append(9)
mySet.add(9)

print("Mod-List: ", myList)
print("Mod-Set: ", mySet)