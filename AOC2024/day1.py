# Imports
import bisect # binary search algorithm

# Part One
list1 = []
list2 = []
distanceSum = 0

with open("day1-input.txt","r") as twoLists:
    for line in twoLists:
        lineArray = line.split("   ") # splits line into two elements
        list1.append(int(lineArray[0]))
        list2.append(int(lineArray[1].strip()))
list1.sort()
list2.sort()

for i in range(len(list1)):
    distance = list1[i] - list2[i]
    distanceSum += abs(distance)
print(f"Sum of distances is: {distanceSum}")

# Part Two
totalSimilarityScore = 0

for i in range(len(list1)):
    startIndex = bisect.bisect_left(list2, list1[i])
    endIndex = bisect.bisect_right(list2, list1[i])
    occurences = endIndex - startIndex
    similarityScore = list1[i] * occurences
    totalSimilarityScore += similarityScore
print(f"The similarity score is: {totalSimilarityScore}")
