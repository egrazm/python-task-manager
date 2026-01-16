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
    tasks[index]["completed"] = True