import re
import numpy as np

# Task 1

lineArr = []
matrixCreated = False
totalInstances = 0

with open("day4-input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        lineArr.append(line)
        forwards = len(re.findall("XMAS", line))
        reverse = len(re.findall("SAMX", line))
        totalInstances += forwards + reverse

        # construct matrix (for diagonal operations)
        charlist = [char for char in line]
        newRow = np.array(charlist)
        if matrixCreated:
            matrix = np.vstack((matrix, newRow))
        else:
            matrix = np.array(newRow)
            matrixCreated = True
    
flippedMatrixLR = np.fliplr(matrix) # matrix flipped left to right
transposedMatrix = matrix.T

def countDiagonals(inputtedMatrix):
    totalDiagonals = 0
    for i in range(-len(inputtedMatrix), len(inputtedMatrix)): # This is a square matrix so no IndexError
        diagonalMatrix = np.diag(inputtedMatrix, k=i)
        diagonalString = ''.join(str(item) for item in diagonalMatrix)
        forwardDiagonals = len(re.findall("XMAS", diagonalString))
        backwardDiagonals = len(re.findall("SAMX", diagonalString))
        totalDiagonals += forwardDiagonals + backwardDiagonals
    return totalDiagonals

def countVerticals(inputtedMatrix):
    totalVerticals = 0
    for columnArr in inputtedMatrix:
        column = ''.join(str(item) for item in columnArr)
        downs = len(re.findall("XMAS", column))
        ups = len(re.findall("SAMX", column))
        totalVerticals += ups + downs
    return totalVerticals

print(len(matrix))
totalInstances += countVerticals(transposedMatrix)
totalInstances += countDiagonals(matrix) + countDiagonals(flippedMatrixLR)

print(f"The amount of times \"XMAS\" was found in the wordsearch was {totalInstances}")

# Task 2

totalInstances = 0
def findxmas(matrix):
    xmas = 0
    for x in range(len(matrix)): # iterate over rows
        for y in range(len(matrix)): # iterate over cols
            if matrix[x,y] == "A":
                if x-1 >= 0 and x+1 <= len(matrix) - 1 and y-1 >= 0 and y+1 <= len(matrix) - 1: # square matrix so y can be compared to horizontal length
                    if ((matrix[x-1,y+1] == "S" and matrix[x+1,y-1] == "M") or (matrix[x-1, y+1] == "M" and matrix[x+1,y-1] == "S")) and ((matrix[x+1,y+1] == "S" and matrix[x-1,y-1] == "M") or (matrix[x+1,y+1] == "M" and matrix[x-1,y-1] == "S")):
                        xmas += 1
    return xmas

print(f"The amount of times an X-\"MAS\" was found in the wordsearch was {findxmas(matrix)}")
