tasks = []

#CREATE TASK
def add_task(task):
    tasks.append(task)
    print(f"Task {task} is added successfully")

#UPDATE TASK
def update_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index] = new_task
        print("Task updated successfully.")
    else:
        print("Invalid index.")

#READ TASK
def view_tasks():
    print("Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# DELETE
def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed}' deleted.")
    else:
        print("Invalid index.")

# Demo
add_task("Learn Python")
add_task("Build a project")
view_tasks()
update_task(0, "Learn Python CRUD")
delete_task(1)
view_tasks()
add_task("Learn Python again")
view_tasks()