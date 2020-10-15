#!python3
# Volume Calculator
# Feel free to rename your variables

Uinput = float()
def title():
    #Spencer
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    while Uinput != Exit:
        print("===================================================================")
        print("                     3D VOLUME Calculator                          ")
        print("                   By: Spencer, Sean and Maya                      ")
        print("===================================================================")
        


    return None

def instructions():
    #Maya
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts

    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements
    
    return measurements

def main():
    #Sean
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()

main()













#2nd test
#this is how mr yang wants it done. main file will only be "main()"
Uin = ""

def title():
    print("===================================================================")
    print("=                    3D VOLUME Calculator                         =")
    print("=                         By: Spencer                             =")
    print("===================================================================")

def CubeVol(lenght):
    answer = lenght ** 3
    return answer

while Uin != "Exit":
    title()
    typeoshape = input("Enter a type of 3D shape. (Cube, Rectangular Prism, Cone or Pyramid )").strip()
    if typeoshape == "Cube":
        CubeSide = float(input("Enter the lenght of the side"))
        ans = CubeVol(CubeSide)
        print(ans)

def main():
    # display title
    # ask them for a shape or instructions
    # 



main()
