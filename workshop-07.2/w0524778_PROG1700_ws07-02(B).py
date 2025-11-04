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
    if marks.lower()=="exit":       #add a thing that only allows up %100
        break
    grades.append(marks)
#print(grades)

for i in range(len(students)):
    print(f"{students[i]} → {grades[i]}")
    

