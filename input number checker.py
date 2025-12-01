while True:
    selection = input("\nEnter a valid number (1-26). 0 to exit: ")
 
    if selection == '0':
        print("Exiting program.")
        break
 
    if selection.isdigit() and 1 <= int(selection) <= 26:
        print("Valid number:", selection)
        continue
 
    print("Invalid input.")