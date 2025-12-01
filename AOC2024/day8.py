import numpy as np

matrixCreated = False
frequencies = []
validAntinodes = 0
antinodeCoordinates = set()

# Part One
with open("day8-input.txt","r") as file:
    for line in file:
        line = line.strip()
        row = [str(char) for char in line]
        if matrixCreated:
            matrix = np.vstack((matrix, row))
        else:
            matrix = np.array(row)
            matrixCreated = True
for row in matrix:
    for item in row:
        if item != "." and item not in frequencies:
            frequencies.append(item)
for item in frequencies:
    antennaPositions = []
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == item:
                antennaPositions.append((x,y))
    for i in range(len(antennaPositions)):
        for j in range(i+1,len(antennaPositions)):
            a = antennaPositions[i] # first point
            b = antennaPositions[j] # second point
            dx = b[0]-a[0] # change in x from a->b
            dy = b[1]-a[1] # change in y from a->b
            pointBefore = (a[0]-dx,a[1]-dy) # point c where c->a->b
            pointAfter = (b[0]+dx,b[1]+dy) # point d where a->b->d
            if 0 <= pointBefore[0] <= len(matrix) - 1 and 0 <= pointBefore[1] <= len(matrix[0]) - 1 and pointBefore not in antinodeCoordinates:
                validAntinodes += 1
                antinodeCoordinates.add(pointBefore)
            if 0 <= pointAfter[0] <= len(matrix) - 1 and 0 <= pointAfter[1] <= len(matrix[0]) - 1 and pointAfter not in antinodeCoordinates:
                validAntinodes += 1
                antinodeCoordinates.add(pointAfter)
print(f"The amount of antinodes with limited distance is {validAntinodes}")

# Part Two
antinodeCoordinates = set()
validAntinodes = 0

for item in frequencies:
    antennaPositions = []
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == item:
                antennaPositions.append((x,y))
    for i in range(len(antennaPositions)):
        for j in range(i+1,len(antennaPositions)):
            a = antennaPositions[i] # first point
            b = antennaPositions[j] # second point
            dx = b[0]-a[0]
            dy = b[1]-a[1]
            if a not in antinodeCoordinates:
                antinodeCoordinates.add(a)
                validAntinodes += 1
            if b not in antinodeCoordinates:
                antinodeCoordinates.add(b)
                validAntinodes += 1
            currenta = a
            currentb = b
            while True:
                nexta = (currenta[0]-dx,currenta[1]-dy)
                if 0 <= nexta[0] <= len(matrix) - 1 and 0 <= nexta[1] <= len(matrix[0]) - 1:
                    if nexta not in antinodeCoordinates:
                        validAntinodes += 1
                        antinodeCoordinates.add(nexta)
                    currenta = nexta
                else:
                    break
            while True:
                nextb = (currentb[0]+dx,currentb[1]+dy)
                if 0 <= nextb[0] <= len(matrix) - 1 and 0 <= nextb[1] <= len(matrix[0]) - 1:
                    if nextb not in antinodeCoordinates:
                        validAntinodes += 1
                        antinodeCoordinates.add(nextb)
                    currentb = nextb
                else:
                    break
print(f"The amount of antinodes with infinite distance is {validAntinodes}")
