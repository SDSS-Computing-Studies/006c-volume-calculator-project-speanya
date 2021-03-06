#!python3
# Volume Calculator
# Feel free to rename your variables
def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Spencer
    # Modified: Maya, Sean 
    print("===================================================================")
    print("=                    3D VOLUME Calculator                         =")
    print("=                 By: Sean, Spencer and Maya                      =")
    print("===================================================================")
def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Maya 
    # Modified: n/a

    print("==============")
    print("Instructions:")
    print("-This program is able to calculate the volume of a cube, cone, pyramid, or rectangle.")
    print("-The program will begin by asking the user to input a shape.")
    print("-The user will then be asked to enter the dimensions of the shape.")
    print("-The program will then calculate the volume of the shape entered by the user.")
    print("-Once the volume has been calculated, the program will repeat unless the user chooses to quit the program.")
    print('-To quit the program, enter "exit" when prompeted.')
    print("Example:")
    print("Enter a shape:'rectangle'")
    print("Enter length:'3'")
    print("Enter width:'4'")
    print("Enter height:'5'")
    print("The volume of the rectangle you entered is 60.")
    print("Quit program?:'exit'")
    print("==============")
def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    #Author: Maya
    #Modified: Spencer
    
    
    if shape == "rectangle":
        
        qlist = ["Enter the length:","Enter the width:","Enter the height:"]
        
    elif shape == "cone":
        
        qlist = ["Enter radius:","Enter height:"]
        
    elif shape == "pyramid":
        
        qlist = ["Enter length:","Enter width:","Enter height:"]
        
    elif shape == "cube":
        qlist = ["Enter length:"]
        
    return qlist
def getInputs(shape,qlist):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    # use questions list, ask each question in the list and then get a number for each one
    # and add that number to measurements list
    #Author: Sean
    #Modified: Spencer
    if shape == "rectangle":
        lengthRec = float(input(qlist[0]))
        widthRec = float(input(qlist[1]))
        heightRec = float(input(qlist[2]))
        measurments = [lengthRec,widthRec,heightRec]
    elif shape == "cone":
        radiusCone = float(input(qlist[0]))
        heightCone = float(input(qlist[1]))
        measurments = [radiusCone,heightCone]
        
    elif shape == "pyramid":
        lengthPyra = float(input(qlist[0]))
        widthPyra = float(input(qlist[1]))
        heightPyra = float(input(qlist[2]))
        measurments = [lengthPyra,widthPyra,heightPyra]
        
    elif shape == "cube":
        
        lengthCube = float(input(qlist[0]))
        measurments = [lengthCube]
        
    return measurments
def calculations(shape,measurments):
    #To calculate the volume for the inputed shape 
    #Author: Spencer
    #Modified: Maya 
    import math 
    if shape == "rectangle":
        
        answer = str(measurments[0] * measurments[1] * measurments[2])
        answer = ("The volume for the shape you entered is"+" "+answer+".")
    #Rectangle V = L * H * W
    
    elif shape == "cone":
        
        answer = str((1/3) * measurments[1] * math.pi * (measurments[0] ** 2))
        answer = ("The volume for the shape you entered is"+ " "+answer+".")
    #Cone V=1/3hπr²
    #answer=str(math.pi*(measurments[0])
    elif shape == "pyramid":
        
        answer = str(((measurments[0] * measurments[1]) * measurments[2]) * (1/3))
        answer = ("The volume for the shape you entered is"+ " "+answer+".")
    #Pyramid (base*height)/(1/3)
    if shape == "cube":
        
        answer = str(measurments[0] ** 3)
        answer = ("The volume for the shape you entered is"+ " "+answer+".")
    #Cube**3
    return answer
def main():
    # Run program
    #Author: Sean 
    #Modified: Spencer, Maya 
    continoo = ""

    while continoo != "exit":
        title()
        hm = input("Would you like to see the instructions? yes or no.")
        if hm == "yes":
            instructions()
            shape = input("Enter a shape:")
            questions=getParams(shape)
            x=getInputs(shape,questions)
            print(calculations(shape,x))
            continoo = str(input("Would you like to continue or exit the program? If you want to exit, type 'exit'. If not, type anything else. "))
        else: 

            shape = input("Enter a shape:")
            questions=getParams(shape)
            x=getInputs(shape,questions)
            print(calculations(shape,x))
            continoo = str(input("Would you like to continue or exit the program? If you want to exit, type 'exit'. If not, type anything else. "))

main()

# main block of code that will run your program and control program flow
# You will need to include a while loop to keep repeating the commands until
# the user chooses to exit
#Cone V=1/3hπr²
#Pyramid (base*height)/(1/3)
#Cube**3
#Rectangle V = L * H * W


