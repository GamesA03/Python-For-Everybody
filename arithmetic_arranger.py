from pickle import FALSE


def arithemtic_arranger(problems, answer = FALSE):
    if len(problems) > 5:
        return "Error: too manty problems"
 #tables created for the first and second numbers as well as the operator between them   
    first_number = []
    second_number = []
    operator = []

    for problem in problems:
        pieces = problem.split()
        first_number.append(pieces[0])
        operator.append(pieces[1])
        second_number.append(pieces[2])
    #checks operators. Program does not accept multiplication or division problems in this stage. May be modified later on
    if operator == "*" or operator == "/" :
        return "Error, operator must be addition or subtraction"
    
    #checks if inputs are digits or not
    for i in range(first_number):
        if not(first_number[i].isdigit or second_number[i].isdigit) :
            return "Error, values must be integers"
    #sets limit for number size
    for i in range(first_number):
        if first_number[i] > 4 or second_number[i] > 4:
            return "Error, values must be 4 numbers or less"

    #Creates tables establishing the different lines of the equation being constructued
    # including the first number, second number, the operator for those numbers, as well as the bottom where the answer presents itself   
    firstLine = []
    secondLine = []
    thirdLine = []
    fourthLine = []

    #Sets the formatting for the first line, including spacing to align the first number
    for i in range(len(first_number)):
            firstLine.append(" "*2 + first_number[i])

    #Sets the formatting for the second number, including spacing between the operator and the second number so they align correctly with the third number
    for i in range(len(second_number)):
            secondLine.append(operator[i] + " " + second_number[i])

    #Sets the amount of line space needed based off of which of the two numbers in the equation is the largest
    for i in range(len(first_number)):
        thirdLine.append("-"*(max(len(first_number[i]), len(second_number[i])) + 2))

    if answer:
        for i in range(len(first_number)):
            if operator[i] == "+":
                ans = str(int(first_number[i]) + int(second_number[i]))
            else:
                ans = str(int(first_number[i]) - int(second_number[i]))
        arranged_problems = "    ".join(firstLine) + "\n" + "    ".join(secondLine) + "\n" + "    ".join(thirdLine) + "\n" + "    ".join(fourthLine)
    else:
        arranged_problems = "    ".join(firstLine) + "\n" + "    ".join(secondLine) + "\n" + "    ".join(thirdLine)
    return arranged_problems