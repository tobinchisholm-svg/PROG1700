raining = input("Is it raining? (yes/no): ")
cold = input("Is it cold outside? (yes/no): ")
windy = input("Is it windy? (yes/no): ")

if windy == "yes":
    print("its super windy sta inside.")
if raining == "yes" and cold == "yes":
    print("Wear a raincoat and warm clothes.")
elif raining == "yes" and cold == "no":
    print("Take an umbrella.")
elif raining == "no" and cold == "yes":
    print("Wear a jacket.")
else:
    print("Enjoy the nice weather!")