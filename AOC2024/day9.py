# Part One
blockArr = []
currentValue = 0
freeSpace = False
checksum = 0

with open("day9-input.txt","r") as file:
    lineArr = file.readlines()
    lineStr = ''.join(str(char) for char in lineArr)
    for char in lineStr:
        if not freeSpace:
            blockArr.extend([currentValue]*int(char))
            currentValue += 1
            freeSpace = True
        else:
            blockArr.extend(["."]*int(char))
            freeSpace = False
backupBlockArr = blockArr.copy()

while "." in blockArr:
    while blockArr[-1] == ".":
        blockArr.pop()
    while blockArr[-1] != "." and "." in blockArr:
        insertionIndex = blockArr.index(".")
        workingValue = blockArr[-1]
        blockArr[insertionIndex] = workingValue
        blockArr.pop()

for index, value in enumerate(blockArr):
    product = index * value
    checksum += product
print(f"The checksum received when moving one block is {checksum}")


# Part Two
checksum = 0
blockArr = backupBlockArr.copy()
currentValue = 0
numCount = {}
numStart = {0: 0}
numEnd = {}
dotCount = {}
dotStart = {}
swapped = {0: False}

for index, item in enumerate(blockArr): # convert array to only strings
    blockArr[index] = str(item)

for index, item in enumerate(blockArr):
    if item != "." and str(item) != str(currentValue): # if not not and there is a new number
        currentValue += 1
        numStart[currentValue] = index # adds when each new number starts
        swapped[currentValue] = False
    if item != ".":
        if currentValue in numCount:
            numCount[currentValue] += 1 # adds the count of each number in each dot block
        else:
            numCount[currentValue] = 1
    else:
        if index - 1 > 0: # prevents IndexError
            if blockArr[index - 1] != ".": # if there isn't a dot before, that means it's the first dot in dot block
                dotStart[currentValue] = index
        if currentValue in dotCount:
            dotCount[currentValue] += 1
        else:
            dotCount[currentValue] = 1

for numKey in range(len(numCount.keys()) - 1, -1, -1):
    for dotKey in dotCount:
        space = dotCount[dotKey]
        fileSize = numCount[numKey]
        if not swapped[numKey] and space >= fileSize and numStart[numKey] > dotStart[dotKey]:
            startUsedIndex = dotStart[dotKey]
            endUsedIndex = startUsedIndex + fileSize
            blockArr[startUsedIndex:endUsedIndex] = [str(numKey)] * fileSize
            startRemovalIndex = numStart[numKey] # index for where number used to be
            endRemovalIndex = numStart[numKey] + fileSize
            blockArr[startRemovalIndex:endRemovalIndex] = ["."] * fileSize # put spaces where they used to be
            swapped[numKey] = True
            dotCount[dotKey] -= fileSize # remove amount of space from dict
            dotStart[dotKey] += fileSize

for index, value in enumerate(blockArr):
    if value != ".":
        product = index * int(value)
        checksum += product
print(f"The checksum received when moving a whole file is {checksum}")
