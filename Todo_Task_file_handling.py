def load():

    tasks = []

    try:
        with open("tasks.txt","r") as f:
            for line in tasks:
                tasks.append(line.strip())
        print(f"Loaded {len(tasks)} in the List")
    except FileNotFoundError:
        print("File not found Yet!")

def add(tasks):

     print("-"*20)
     n = input("Write Tasks: ")
     tasks.append(n)
     print(f"Task {n} Added!")

def view(tasks):

    if not tasks:
        print("No Tasks Added yet!")
        return
    print("Your List of tasks!")
    print("-"*20)
    for i, task in enumerate(tasks, 1): 
        print(f"{i} . {task}")
    print("-"*20)                

def remove(tasks):

    try:
        r = int(input("Enter Task Number to remove: "))
        if 1 <=  r <= len(tasks):
           removed = tasks.pop(r-1)
           print(f"Removed: {removed}")
        else:
            print("Invalid Task number!")
    except ValueError:
            print("Enter a Number!")

def save(tasks):

    with open("tasks","w") as f:
        for line in tasks:
            f.write(line + "\n")
    print(f"Saved {len(tasks)} tasks to list")

def main():

    tasks = load()

    while True:
        print("\n" + "=" * 20)
        print(" TO-DO LIST")
        print("=" * 20)
        print("1. View All Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save & Exit")
        print("-" * 20)
        
        n = input("Enter Option (1-4): ")  

        if n == "1":
            view(tasks)
        elif n == "2":
            add(tasks)
        elif n == "3":
            remove(tasks)
        elif n == "4":
            save(tasks)
            print("-"*20)
        else:
            print("Invalid choice! Try again!")

if __name__ == "__main__":
    main()                                                           