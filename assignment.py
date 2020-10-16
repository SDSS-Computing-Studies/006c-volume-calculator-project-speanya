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
    print("n/ n/")



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
    return None
    pass

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    
    
    if shape=="rectangle":
        dimension_list=["Enter the length:","Enter the width:","Enter the height:"]
        
    elif shape=="cone":
        dimension_list=["Enter radius:","Enter slant height:","Enter height:"]
        
    elif shape=="pyramid":
        dimension_list=["Enter length:","Enter width:","Enter height:"]
        
    elif shape=="cube":
        dimension_list=["Enter length:"]
        
    prompts=dimenion_list
    return prompts




def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements = []
    # use questions list, ask each question in the list and then get a number for each one
    # and add that number to measurements list
     if shape == "rectangle":
        lengthRec = float(input(dimension_list[0]))
        widthRec = float(input(dimension_list[1]))
        heightRec = float(input(dimension_list[2]))
        measurments = [lengthRec,widthRec,heightRec]

    elif shape == "cone":
        radiusCone = float(input(dimension_list[0]))
        heightCone = float(input(conelist[1]))
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
    
def main():
    # Run program
    continued= ''
    continued2= ''
    continued3= ''
    x= 1
    while continued != "Yes" or continued != "No":
        continued= input("Would you like to enter a different set of numbers? Yes or No: ")
        if continued == "Yes":
            getInputs(questions)
        if continued == "No":
            x=2
            break
        else:
            print("Error")
            
    if x == 2:
        while continued3 != "Yes":
            continued2= input("Would you like to pick a different shape to calculate? Yes or No: ")
            if continued2 == "Yes":
                getParams(shape)
            if continued2 == "No":
                continued3= input("Would you like to quit? Yes or No: ")
                if continued3 == "Yes":
                    break
                    title()
                else:
                    print("Error")

main()


# main block of code that will run your program and control program flow
# You will need to include a while loop to keep repeating the commands until
# the user chooses to exit










#Cone V=1/3hπr²
#Pyramid (base*height)/(1/3)
#Cube**3
#Rectangle V = L * H * W