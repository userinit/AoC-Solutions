import re #For RegEx

# Task 1
total = 0
regex = r"mul\(\d+,\d+\)"

with open("day3-input.txt","r") as file:
    for line in file:
        regexArr = re.findall(regex, line)
        for item in regexArr:
            strippedItem = re.sub(r"[^0-9,]", "", item)
            splitItemArr = strippedItem.split(",")
            num1 = int(splitItemArr[0])
            num2 = int(splitItemArr[1])
            total += num1 * num2
print(total)

# Task 2
total = 0
regex = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
mulActivated = True

with open("day3-input.txt","r") as file:
    for line in file:
        regexArr = re.findall(regex, line)
        for item in regexArr:
            if item[0:3] == "mul" and mulActivated:
                strippedItem = re.sub(r"[^0-9,]", "", item)
                splitItemArr = strippedItem.split(",")
                num1 = int(splitItemArr[0])
                num2 = int(splitItemArr[1])
                total += num1 * num2
            elif item[0:4] == "do()":
                mulActivated = True
            elif item[0:7] == "don't()":
                mulActivated = False
print(total)
