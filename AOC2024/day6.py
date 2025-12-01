import numpy as np

# Part One
def indexSearch(matrix):
    for rowIndex, row in enumerate(matrix):
        for colIndex, element in enumerate(row):
            if element == "^":
                return(colIndex, rowIndex)

matrixCreated = False
angle = 0 # 0=N, 90=E, 180=S, 270=W
distinctPositions = 1
visited = set()

with open("day6-input.txt","r") as file: 
    for line in file:
        line = line.strip()
        row = [str(char) for char in line]
        if matrixCreated:
            matrix = np.vstack((matrix, row))
        else:
            matrix = np.array(row)
            matrixCreated = True

x,y = indexSearch(matrix) # start position
visited.add((x,y))

while 0 <= x <= len(matrix)-1 and 0 <= y <= len(matrix)-1:
    if angle == 0:
        if y - 1 >= 0:
            item = matrix[y-1][x]
            if item == "." and (x,y-1) not in visited:
                visited.add((x,y-1))
            if item != "#":
                y -= 1
            else:
                angle = (angle + 90) % 360
        else:
            break
    elif angle == 90:
        if x + 1 <= len(matrix) - 1:
            item = matrix[y][x+1]
            if item == "." and (x+1,y) not in visited:
                visited.add((x+1,y))
            if item != "#":
                x += 1
            else:
                angle = (angle + 90) % 360
        else:
            break
    elif angle == 180:
        if y + 1 <= len(matrix) - 1:
            item = matrix[y+1][x]
            if item == "." and (x,y+1) not in visited:
                visited.add((x,y+1))
            if item != "#":
                y += 1
            else:
                angle = (angle + 90) % 360
        else:
            break
    elif angle == 270:
        if x - 1 >= 0:
            item = matrix[y][x-1]
            if item == "." and (x-1,y) not in visited:
                visited.add((x-1,y))
            if item != "#":
                x -= 1
            else:
                angle = (angle + 90) % 360
        else:
            break
print(f"The number of distinct positions will the guard visit before leaving the mapped area is {len(visited)}")

# Part Two

# Disclaimer: This algorithm prioritizes simplicity over efficiency.
# The time complexity is high (O(n^4)), but the implementation is straightforward.
angle = 0
loopsCount = 0
visited = set()
x,y = indexSearch(matrix) # start position
for rowIndex in range(len(matrix)):
    for columnIndex in range(len(matrix)):
        if matrix[rowIndex][columnIndex] == ".":
            visited = set()
            angle = 0
            x,y = indexSearch(matrix)
            newMatrix = matrix.copy()
            newMatrix[rowIndex][columnIndex] = "#"
            while 0 <= x <= len(newMatrix)-1 and 0 <= y <= len(newMatrix)-1:
                if angle == 0:
                    if y - 1 >= 0:
                        item = newMatrix[y-1][x]
                        if item == ".":
                            if (x,y-1,angle) not in visited:
                                visited.add((x,y-1,angle))
                            else:
                                loopsCount += 1
                                break
                        if item != "#":
                            y -= 1
                        else:
                            angle = (angle + 90) % 360
                    else:
                        break
                elif angle == 90:
                    if x + 1 <= len(newMatrix) - 1:
                        item = newMatrix[y][x+1]
                        if item == ".":
                            if (x+1,y,angle) not in visited:
                                visited.add((x+1,y,angle))
                            else:
                                loopsCount += 1
                                break
                        if item != "#":
                            x += 1
                        else:
                            angle = (angle + 90) % 360
                    else:
                        break
                elif angle == 180:
                    if y + 1 <= len(newMatrix) - 1:
                        item = newMatrix[y+1][x]
                        if item == ".":
                            if (x,y+1,angle) not in visited:
                                visited.add((x,y+1,angle))
                            else:
                                loopsCount += 1
                                break
                        if item != "#":
                            y += 1
                        else:
                            angle = (angle + 90) % 360
                    else:
                        break
                elif angle == 270:
                    if x - 1 >= 0:
                        item = newMatrix[y][x-1]
                        if item == ".":
                            if (x-1,y,angle) not in visited:
                                visited.add((x-1,y,angle))
                            else:
                                loopsCount += 1
                                break
                        if item != "#":
                            x -= 1
                        else:
                            angle = (angle + 90) % 360
                    else:
                        break
print(f"The amount of loops found when a new obstacle was placed was {loopsCount}")
