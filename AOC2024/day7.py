# Disclaimer: This algorithm is not designed to be optimised
# It has an exponential order which makes it computationally expensive
# The design of this algorithm prioritises simplicity of coding over efficiency
import itertools

# Part One
operators = "*+|"
totalCalibrations = 0

with open("day7-input.txt","r") as file:
    for line in file:
        answerProductArr = line.split(":")
        answer = answerProductArr[0]
        productStr = answerProductArr[1].strip()
        productArr = productStr.split(" ")
        operatorCombos = [''.join(operator) for operator in itertools.product(operators, repeat=len(productArr)-1)]
        for operatorArr in operatorCombos: # iterates over each operator in the combination
            calculationArr = []
            for i in range(len(productArr)-1):
                calculationArr.append("(")
            for j, operator in enumerate(operatorArr):
                calculationArr.append(productArr[j])
                if j != 0:
                    calculationArr.append(")")
                calculationArr.append(operator)
                if j == len(operatorArr)-1:
                    calculationArr.append(productArr[j+1])
                    calculationArr.append(")")
            calculationStr = ''.join(str(char) for char in calculationArr)
            calculation = eval(calculationStr)
            if calculation == int(answer):
                totalCalibrations += calculation
                break
print(f"The total number of calibrations without concatenation operator is: {totalCalibrations}")

# Part Two
operators = "*+|" # AoC says concatenation operator is || but we make it | for simplicity
totalCalibrations = 0

with open("day7-input.txt","r") as file:
    for line in file:
        answerProductArr = line.split(":")
        answer = answerProductArr[0]
        productStr = answerProductArr[1].strip()
        productArr = productStr.split(" ")
        operatorCombos = [''.join(operator) for operator in itertools.product(operators, repeat=len(productArr)-1)]
        for operatorArr in operatorCombos:
            calculationArr = []
            for i, operator in enumerate(operatorArr):
                calculationArr.append(productArr[i])
                calculationArr.append(operator)
                if i == len(operatorArr)-1:
                    calculationArr.append(productArr[i+1])
            while len(calculationArr) != 1:
                numOne = calculationArr[0]
                currentOperator = calculationArr[1]
                numTwo = calculationArr[2]
                if currentOperator == "*":
                    ansNum = str(int(numOne)*int(numTwo))
                elif currentOperator == "+":
                    ansNum = str(int(numOne)+int(numTwo))
                else:
                    ansNum = numOne+numTwo
                del calculationArr[:3]
                calculationArr.insert(0,ansNum)
            calcInt = int(calculationArr[0])
            if calcInt == int(answer):
                totalCalibrations += calcInt
                break
print(f"The total number of calibrations with concatenation operator is: {totalCalibrations}")
