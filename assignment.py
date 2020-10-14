#!python3
# Volume Calculator
# Feel free to rename your variables

x=1
def title():
    if x==2:
        print("Yes")
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    pass
    
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None
    pass

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts
    pass

    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements
    pass
    
    return measurements

def main(exit):
    pass
    # Run program

    if x==2:
        while continued != "Yes" or continued != "No":
            continued= input("Would you like to enter a different set of numbers? Yes or No")
            if continued == "Yes":
                #Go to repeat code for that shape
                # x=1 will activate getParams
                # getParams will then delete 1 to activate this
           # elif continued == "No":
        else:
            print("Error")


                while continued3 == "No":
                    continued2= input("Would you like to pick a different shape to calculate? Yes or No")
                    if continued2 == "Yes":
                        #Go to choose shape page
                    elif continued2 == "No":
                            continued3= input("Would you like to quit? Yes or No")
                            if continued3 == "Yes":
                                break
                                #Go to title



    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit


main()







#Cone V=1/3hπr²
#Pyramid (base*height)/(1/3)
#Cube**3
#Rectangle V = L * H * W