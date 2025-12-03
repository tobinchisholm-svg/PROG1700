def read_grades(file_path):
    grades = {}
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines[1:]: 
            if line.strip() == "":
                continue
            name, grade = line.strip().split(",")
            grades[name] = int(grade)
    return grades

def write_grades_to_txt_and_maths(grades, output):

    total = 0
    highest = None
    lowest = None

    with open(output, "w") as f:
        for name, grade in grades.items():
            f.write(f"{name}: {grade}\n")
            total += grade
            if highest is None or grade > highest:
                highest = grade
            if lowest is None or grade < lowest:
                lowest = grade

        avg = total / len(grades)
        f.write(f"Average: {avg:.2f}\n")
        f.write(f"Highest grade: {highest}\n")
        f.write(f"Lowest grade: {lowest}\n")


def main():
    grades_dict = read_grades("grades.csv")
    write_grades_to_txt_and_maths(grades_dict, "report.txt")
    print("The report can be found in report.txt")

if __name__ == "__main__":
    main()
