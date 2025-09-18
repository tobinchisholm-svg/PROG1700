name = input("Enter your name: ")
age_text = input("Enter your age: ")
if age_text.isdigit():
    age = int(age_text)
    print(f"In 5 years you will be {age + 5}.")
else:
    print("That doesn't look like a number.")