# Part One
safeReports = 0
isIncreasing = ""

with open("day2-input.txt", "r") as allReports:
    for report in allReports:
        safe = True
        isIncreasing = ""
        levelArray = report.strip().split(" ") # each report is made into levels
        for i in range(len(levelArray) - 1):
            if safe:
                a = int(levelArray[i])
                b = int(levelArray[i+1])
                if isIncreasing == "":
                    if a < b:
                        isIncreasing = True
                    elif a > b:
                        isIncreasing = False
                    else:
                        safe = False
                        # Value is repeated on the very first number
                if isIncreasing:
                    if a > b or b - a > 3:
                        safe = False
                else:
                    if a < b or a - b > 3:
                        safe = False
                if a == b:
                    safe = False
        if safe:
            safeReports += 1
print(f"Safe reports before removing level: {safeReports}")

# Part Two
safeReports = 0
safe = True

with open("day2-input.txt", "r") as allReports:
    for report in allReports:
        levelArray = list(map(int, report.strip().split(" ")))
        isIncreasingArr = [False, True]
        for isIncreasing in isIncreasingArr:
            for removalIndex in range(len(levelArray)):
                testArray = levelArray[:removalIndex] + levelArray[removalIndex + 1:]
                safe = True
                for i in range(len(testArray)-1):
                    a = testArray[i]
                    b = testArray[i+1]
                    if isIncreasing and (a >= b or b - a > 3):
                        safe = False
                        break
                    if not isIncreasing and (a <= b or a - b > 3):
                        safe = False
                        break
                if safe:
                    break
            if safe:
                safeReports += 1
print(f"Safe reports after removing level: {safeReports}")
