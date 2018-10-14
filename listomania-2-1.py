###################################
##|                             |##
##|                             |##
##|        Rocky Vargas         |##
##|                             |##
##|                             |##
###################################

# This function is used to allow the user to input numbers.
def getIntInput(message):
    first = True
    while True:
        try:
            if first:
                return int(input(message))
            else:
                return int(input("Error! Enter a number: "))
        except:
            first = False

# This function allows the user to enter a list of integers.
def getListInput():
    listLength = getIntInput("How many integers would you like within your list? ")
    listNumbers =[]
    for i in range(listLength):
        listNumbers.append(getIntInput("Enter integer number %d: "%(i+1)))
    return listNumbers

# This function allows the user to enter a list a strings.
def getListStringInput():
    listLength = getIntInput("How many items would you like within your list? ")
    listNumbers =[]
    for i in range(listLength):
        listNumbers.append(input("Enter item number %d: "%(i+1)))
    return listNumbers

# This function condenses a list.
def condenseList(numberList):
    for x in range(len(numberList) - 1):
        if numberList[x] == numberList[x + 1]:
            numberList[x] = 'x'
    while 'x' in numberList:
        numberList.remove('x')
    return numberList

# This function checks if a list is sorted and returns true or false.
def sortChecker(numberList):
    for x, item in enumerate(numberList):
        try:
            if item > numberList[x + 1]:
                return False
        except IndexError:
            return True

# This function adds up the list and returns the total.
def sumOfList(numberList):
    return sum(numberList)

# This function reverses the list given.
def reverseList(anyList):
    anyList.reverse()
    return anyList

# This function combines two sorted lists and creates a single sorted list.
def comboList(numberList, number2List):
    x = numberList
    x += number2List
    numberList.sort()
    return numberList

# This function runs all functions.
def ultimateFunction():
    print("This function will condense [1, 1, 2, 3, 3]:")
    print(condenseList([1, 1, 2, 3, 3]))
    print()
    print("This function will check and see if [5, 7, 1, 2, 4] is sorted:")
    print(sortChecker([5, 7, 1, 2, 4]))
    print()
    print("This function will add up the total of [25, 10, 30, 40, 20]:")
    print(sumOfList([25, 10, 30, 40, 20]))
    print()
    print("This function will reverse [5, 7, 9, 'hello', 'world']:")
    print(reverseList([5, 7, 9, 'hello', 'world']))
    print()
    print("This function will combine [2, 3, 10, 25] and [10, 29, 30, 80, 69, 420, 1337, 9001]:")
    print(comboList([2, 3, 10, 25], [10, 29, 30, 80, 69, 420, 1337, 9001]))

# Run Everything.
ultimateFunction()
print("Goodbye!")



