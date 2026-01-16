tasks = []


def add_task(title):
    tasks.append({
        "title": title,
        "completed": False
    })


def list_tasks():
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['title']} [{status}]")

def complete_task(index):
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
