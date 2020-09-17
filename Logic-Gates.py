'''
This program will allow the user to choose from a logical operator, then
ask for two inputs A and B to compare. It will then output the result of
the logical operation. Lastly it will run until the user enter anything other than Y.
'''

# Function getA will ask the user for an A value of either 0 or 1, returning the value that will be used in the operation
def getA():
    A = input("Please enter a value for A (0 or 1): ")
    # This while loop validates for any user input that is not 0 or 1, asking for the user to enter a value of 0 or 1
    while A != "1" and A != "0":
        A = input("Please enter a value for A (0 or 1): ")
    return A

def getB():
    B = input("Please enter a value for B (0 or 1): ")
# FIXME will converting to strings after validating work?
    while B != "1" and B != "0":
        B = input("Please enter a value for B (0 or 1): ")
    return B

'''
The following functions perform operations on logical gates. They are designed so that the least amount of operations
that return either TRUE or FALSE are created  as a boolean compound. For example AND will only return TRUE for both
inputs as 1 in that case it would return TRUE otherwise returning FALSE
'''
def AND(A, B):
    if A == "1" and B == "1":
        return f"AND ({A}, {B}) = 1 (TRUE)"
    return f"AND ({A}, {B}) = 0 (FALSE)"

def OR(A, B):
    if A == "1" or B == "1":
        return f"OR ({A}, {B}) = 1 (TRUE)"
    return f"OR ({A}, {B}) = 0 (FALSE)"

def NOT(A):
    if A == "1":
        return f"Not ({A}) = 0 (FALSE)"
    return f"Not ({A}) = 1  (TRUE)"


def NAND(A, B):
    if A == "1" and B == "1":
        return f"NAND ({A}, {B}) = 0 (FLASE)"
    return f"NAND ({A}, {B}) = 1 (TRUE)"

def NOR(A, B):
    if A  == "0" and B == "0":
        return f"NOR ({A}, {B}) = 1 (TURE)"
    return f"NOR ({A}, {B}) = 0 (FALSE)"

def XOR(A, B):
    if (A == "1" and B == "0") or (A == "0" and B == "1"):
        return f"XOR ({A}, {B}) = 1 (TURE)"
    return f"XOR ({A}, {B}) = 0 (FALSE)"

def XNOR(A, B):
    if A == B:
        return f"XNOR ({A}, {B}) = 1 (TRUE)"
    return f"XNOR ({A}, {B}) = 0 (FALSE)"

# This function asks the user for the type of gate they want to perform operation on, and will
# return their choice of gate or inputting any other key will suggest they want to terminate the program
def operator_choice():
    user_choice = input("Type the name of the operator to test, or press any key to quit \n")
    return user_choice



if __name__ == "__main__":

    print("Select one of the following Operators: AND, OR, NOT, NAND, NOR, XOR, XNOR\n")

# This first 2 lines of code are the setting a loop so that the program will keep running until the user wants
# by default I set run_again to Y in order to begin the first loop
    run_again = "Y"
    while run_again == "Y":

        # This line call the operator choice function and assigns it to the variable gate_choice
        gate_choice = operator_choice()

        #The following conditional statements take what was assigned by the variable gate_choice in order to decide  what gate
        #to operate then printing that choice, calling functions A and B to assign and print their inputs. Lastly calling
        #the gate function in this case AND to run the operations otherwise quits the program.

        if gate_choice == "AND":
            print(f"{gate_choice} operator selected.\n")
            A = int(getA())
            B = int(getB())
            # Spacing and f print statement are used to create a more structured layout when printing
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " + AND(A, B))

        elif gate_choice == "OR":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            B = getB()
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " + OR(A, B))

        # NOT is only takes in input because it will negate the users input
        elif gate_choice == "NOT":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            print(f"       Inputs: A = {A}")
            print("       " + NOT(A))

        elif gate_choice == "NAND":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            B = getB()
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " + NAND(A, B))

        elif gate_choice == "NOR":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            B = getB()
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " + NOR(A, B))

        elif gate_choice == "XOR":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            B = getB()
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " + XOR(A, B))

        elif gate_choice == "XNOR":
            print(f"{gate_choice} operator selected.\n")
            A = getA()
            B = getB()
            print(f"       Inputs: A = {A}, B = {B}")
            print("       " + XNOR(A, B))
        else:
            break


        run_again = input("\nEnter Y to run the program again! ")


    print("BYE :)")






