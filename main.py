tasks = []


def add_task(title):
    """
    Add a new task to the task list.
    Args:
        title (str): The title of the task.
    """
    tasks.append({
        "title": title,
        "completed": False
    })


def list_tasks():
    """
    Display all tasks in the task list.
    Shows the completion status of each task.
    """
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['title']} [{status}]")

def complete_task(index):
    """
    Mark the specified task as completed.
    Args:
        index (int): The index of the task to mark as completed.
    Prints an error if the index is not an integer, or if it is negative or out of range.
    """
    if not isinstance(index, int):
        print("Error: index must be an integer")
        return
    
    if index < 0:
        print("Error: index cannot be negative")
        return
    
    if index >= len(tasks):
        print("Error: index out of range")
        return
    
    tasks[index]["completed"] = True
    print(f"Task '{tasks[index]['title']}' marked as completed.")
