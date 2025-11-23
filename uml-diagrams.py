""" This is a script to make simple ASCII-art UML-diagrams
@author: Karturbis """
version = 1.1


# returns the classname as a String
def get_classname():

    classname = input("Please type in the classname: ")
    return classname

# returns the variables as a list of Strings
def get_variables():

    variables = [""]

    # Asks for the first variable
    variables[0] = input("Please type in your variables amd press enter after each: ")

    # Loop, to ask for variables, until the user gives no input
    while True:

        x = input("Please input the next variable. Leave blank to finish: ")

        if x == "":
            break

        else:
            variables.append(x)

    return variables

# returns the methods in a list of strings
def get_methods():

    methods = [""]

    # Asks for the first method
    methods[0] = input("Please type in your methods amd press enter after each: ")

    # Loop, to ask for mehtods, until the user submits a blank input
    while True:

        x = input("Please input the next method. Leave blank to finish: ")

        if x == "":
            break

        else:
            methods.append(x)

    return methods

# returns the length of the longest string, the user typed in earlier
def get_len_uml(classname, variables, methods):

    len_uml = 0

    if len(classname) > len_uml:
        len_uml = len(classname) +1

    for i in variables:
        if len(i) > len_uml:
            len_uml = len(i)

    for i in methods:
        if len(i) > len_uml:
            len_uml = len(i)

    return len_uml


# prints the uml diagram
def print_UML(classname, variables, methods):

    len_uml = get_len_uml(classname, variables, methods)
    x = len_uml + 6

    # sets the string cb to as many spaces, as needed, to have the pipe at the end of the diagram all in one row
    cb = (len_uml - len(classname)) * " "

    # prints the top line of the diagram
    print(x * "–")

    # prints the classname into the topmost section of the diagram
    print("|   " + classname + cb + " |")

    # prints the dividing line between the topmost and the middle part of the diagram
    print(x * "–")

    # prints the variables into the middle section of the diagram
    for i in variables:
        b = (len_uml - len(i)) * " "
        print("|  " + i + b + "  |")

    # prints the dividing line, between the middle and the bottom section of the diagram
    print(x * "–")

    # prints the methods into the bottom section of the diagram
    for i in methods:
        b = (len_uml - len(i)) * " "
        print("|  " + i + b + "  |")

    # prints the bottom line of the diagram
    print(x * "–")


# the main method
if __name__ == "__main__":

    #describes the sript to the user
    print("This is a script, to make ASCII-art UML-diagrams!\nVersion: " + str(version) + "\nwritten by Karturbis\n")

    # first gets all values (with the get methods) and then creates a ASCII art UML diagram from it (with the print_UML method)
    print_UML(get_classname(), get_variables(), get_methods())
