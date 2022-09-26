def addNumberTo(list):
    list.append(10)
    print("Inside Func:", list)

numbers = [ 1, 2, 3, 4, 5]

addNumberTo(numbers)
print("Outside Func:", numbers)


