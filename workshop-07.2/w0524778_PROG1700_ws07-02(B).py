students = ["Ava", "Noah", "Liam"] 
grades = [88, 92, 79]

while True:
    name =input("Enter your name: or next for grades  ")
    if name.lower()=="next":
        break
    students.append(name)
#print(students)
next
while True:
    marks =input("enter your grade or exit  ")
    if marks.lower()=="exit":       #added a thing that only allows up %100
        break

    if marks.isdigit():  # check if input is a number
            marks = int(marks)
            if 0 <= marks <= 100:  # validate range
                grades.append(marks)
            else:
                print("Grade must be between 0 and 100.")
    else:
            print("Please enter a valid number.")

if grades:  
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    print("\nResults:")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
   
   #this isnt right has of right now, please make sure you have this done for tmr.
                              highest= 90
                                    if grades> 90:
                                           print("congrats youve made the honour roll")



for i in range(len(students)):
    print(f"{students[i]} → {grades[i]}")
    
