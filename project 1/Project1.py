input ("please enter your pin number")
Balance =600
PIN=1234
CorrectPin =1234
if PIN == CorrectPin:
    print ("welcom to the canso bank" )
    print ("your balance is", Balance)
    print ("do you want to make a withdrawl")
    answer = input ("yes or no")
    if answer == "yes":
        amount = int (input ("how much do you want to withdrawl"))
        if amount > Balance:
            print ("insufficient funds")
        else:
            Balance = Balance - amount
            print ("your new balance is", Balance )
    if answer == "no":
        print ("would you like to make a deposit?")
        if answer == "yes":
            amount = int (input ("how much do you want to deposit"))
            Balance = Balance + amount
            print ("your new balance is", Balance)
