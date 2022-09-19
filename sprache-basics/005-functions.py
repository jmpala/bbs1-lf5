num = 2
myList = [0,1,2,3,4,5]

def duplicateNum(num):
    return num * 2

def addSomething(list):
    list.append('something')


print("Num: ", num)
print("List: ", myList)

res = duplicateNum(num)
print("Res: ", res)
print("Num: ", num)

addSomething(myList)
print("Mod-List: ", myList)