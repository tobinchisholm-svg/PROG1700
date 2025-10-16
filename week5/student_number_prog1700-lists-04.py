tasks = [] 

 

while True: 

    print("\n1. Add") 

    print("2. View") 

    print("3. Remove") 

    print("4. Exit") 

    choice = input("Choose: ") 

    if choice == '1': 

        task = input("Enter a task: ") 

        tasks.append(task) 

    elif choice == '2': 

        for i, task in enumerate(tasks, 1): 

            print(f"{i}. {task}") 

     

    if choice == '3': 

        task = input("Enter a task to remove: ") 

        if task in tasks: 

            tasks.remove(task) 

        else: 

            print("Task not found.") 

    elif choice == '4': 

        print("Exiting...") 



# Reflection:
# 1. What is one real-world use of lists you can think of in your life or work?
#if you need to get groceries you can make a list of items you need to buy.

# 2. Which list operation (Create, Read, Update, Delete) do you find easiest or hardest, and why?
# I find reading the easiest because it just involves accessing the list and displaying its contents.

# 3. How would you explain the concept of indexing to someone new to Python?
# Think of a list like a row of boxes. Each box has a number starting from 0, 
# If you want to get something from a box, you use its number — that number is the index."