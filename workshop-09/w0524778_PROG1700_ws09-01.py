def is_positive(num):
    return num > 0

def is_integer(value):
    return value.isdigit()



#Use input() to get a user number or string.
#Call validation functions before continuing.
#Print feedback if the data is invalid.
#Use a while loop to re-prompt until valid input is given.



def getUserInput():
    try:
        userinput = float(input("Enter a number or string: "))
        print("You have entered a number")
        print(f"{userinput}")
    except ValueError:
        print("You have entered a string")
        print(f"{userinput}")

# main program
getUserInput()
