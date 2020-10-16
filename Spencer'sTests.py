#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("===================================================================")
    print("=                    3D VOLUME Calculator                         =")
    print("=                 By: Sean, Spencer and Maya                      =")
    print("===================================================================")



def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Maya 
    # Modified:
    print("==============")
    print("Instructions:")
    print("-This program is able to calculate the volume of a cube, cone, pyramid, or rectangle.")
    print("-The program will begin by asking the user to input a shape.")
    print("-The user will then be asked to enter the dimensions of the shape.")
    print("-The program will then calculate the volume of the shape entered by the user.")
    print("-Once the volume has been calculated, the program will repeat unless the user chooses to quit the program.")
    print('-To quit the program, enter "quit" when prompeted.')
    print("Example:")
    print("Enter a shape:'rectangle'")
    print("Enter length:'3'")
    print("Enter width:'4'")
    print("Enter height:'5'")
    print("The volume of the rectangle you entered is 60.")
    print("Quit program?:'quit'")
    print("==============")
    return

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]

    shape = input("Enter a shape:")

    if shape == "rectangle":
        dimension_list = ["Enter the length:","Enter the width:","Enter the height:"]

    elif shape == "cone":
        dimension_list = ["Enter radius:","Enter height:"]

    elif shape == "pyramid":
        dimension_list = ["Enter length:","Enter width:","Enter height:"]

    elif shape == "cube":
        dimension_list = ["Enter length:"]

    return(dimension_list)




def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    # use questions list, ask each question in the list and then get a number for each one
    # and add that number to measurements list
    if shape == "rectangle":
        lengthRec = float(input(dimension_list[0]))
        widthRec = float(input(dimension_list[1]))
        heightRec = float(input(dimension_list[2]))
        measurments = [lengthRec,widthRec,heightRec]

    elif shape == "cone":
        radiusCone = float(input(dimension_list[0]))
        heightCone = float(input(dimension_list[1]))
        measurments = [radiusCone,heightCone]

    elif shape == "pyramid":
        lengthPyra = float(input(dimension_list[0]))
        widthPyra = float(input(dimension_list[1]))
        heightPyra = float(input(dimension_list[2]))
        measurments = [lengthPyra,widthPyra,heightPyra]

    elif shape == "cube":
        lengthCube = float(input(dimension_list[0]))
        measurments = [lengthCube]

    return measurments




def calculations():
    if shape == "rectangle":
        answer = float(measurments[0] * measurments[1] * measurments[2])
    #Rectangle V = L * H * W

    elif shape == "cone":
        answer = float((1/3) * measurments[1] * math.pi * (measurments[0] * 2))
    #Cone V=1/3hπr²

    elif shape == "pyramid":
        answer = float(((measurments[0] * measurments[1]) * measurments[2]) / (1/3))
    #Pyramid (base*height)/(1/3)

    if shape == "cube":
        answer = float(measurments[0] ** 3)
    #Cube**3



def main():
    # Run program
    continoo = ""
    while continoo != "Exit":
        title()
        instructions()
        getParams()
        getInputs()
        calculations()
        continoo = float(input("Would youu like to Continue or Exit the program?"))

main()


# main block of code that will run your program and control program flow
# You will need to include a while loop to keep repeating the commands until
# the user chooses to exit










#Cone V=1/3hπr²
#Pyramid (base*height)/(1/3)
#Cube**3
#Rectangle V = L * H * W