'''
This program will allow the user to choose from a logical operator, then
ask for two inputs A and B to compare. It will then output the result of
the logical operation. Lastly it will run until the user enter anything other than Y.
'''

# Function getA will ask the user for an A value of either 0 or 1
def getA():
    A = int(input("Please eneter a value for A (0 or 1): "))
# FIXME validate for non integers
    while A != 1 and A != 0:
        A = int(input("Please enter a value for A (0 or 1): "))
    return A

def getB():
    B = int(input("Please eneter a value for B (0 or 1): "))
# FIXME will converting to strings after validating work?
    while B != 1 and B !=0:
        B = int(input("Please enter a value for B (0 or 1): "))
    return B

# Functions that preform the operation of every gate
def AND(A, B):
    if A == 1 and B == 1:
        return f"AND ({A}, {B}) = 1 (TRUE)"
    return f"AND ({A}, {B}) = 0 (FALSE)"

def OR(A, B):
    if A == 1 or B == 1:
        return f"OR ({A}, {B}) = 1 (TRUE)"
    return f"OR ({A}, {B}) = 0 (FALSE)"

def NOT(A):
    if A == 1:
        return f"Not ({A}) = 0 (FALSE)"
    return f"Not ({A}) = 1  (TRUE)"


def NAND(A, B):
    if A == 1 and B == 1:
        return f"NAND ({A}, {B}) = 0 (FLASE)"
    return f"NAND ({A}, {B}) = 1 (TRUE)"

def NOR(A, B):
    if A  == 0 and B == 0:
        return f"NOR ({A}, {B}) = 1 (TURE)"
    return f"NOR ({A}, {B}) = 0 (FALSE)"

def XOR(A, B):
    if (A == 1 and B ==0) or (A == 0 and B == 1):
        return f"XOR ({A}, {B}) = 1 (TURE)"
    return f"XOR ({A}, {B}) = 0 (FALSE)"

def XNOR(A, B):
    if A == B:
        return f"XNOR ({A}, {B}) = 1 (TRUE)"
    return f"XNOR ({A}, {B}) = 0 (FALSE)"

# Menu that the user will choose the operator with or quit the program
# Fixme: Too much going on in here change this to a print menu that will store their choice 

def operator_choice():
    user_choice = input("Type the name of the operator to test, or press any key to quit \n")
    return user_choice



if __name__ == "__main__":

    print("Logic gates project")

# FIXME Loop the progam till the user wants
    run_again = "Y"
    while run_again == "Y":
        gate_choice = operator_choice()


        if gate_choice == "AND":
            print(f"{gate_choice} operator selected.\n")
            A = int(getA())
            B = int(getB())
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " + AND(A, B))

        elif gate_choice == "OR":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            B = getB()
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " +OR(A, B))

        elif gate_choice == "NOT":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            print(f"       Inputs: A = {A}")
            print("       " +NOT(A))

        elif gate_choice == "NAND":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            B = getB()
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " +NAND(A, B))

        elif gate_choice == "NOR":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            B = getB()
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " +NOR(A, B))

        elif gate_choice == "XOR":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            B = getB()
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " +XOR(A, B))

        elif gate_choice == "XNOR":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            B = getB()
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " +"     " + XNOR(A, B))
        else:
            break


        run_again = input("\nEnter Y to run the program again! ")


    print("BYE :)")






