from pathlib import Path

TASKS_FILE = Path("tasks.txt")


def add_task(task):
    if not task.strip():
        return "Error: The task name is missing."

    with open(TASKS_FILE, "a", encoding="utf-8") as file:
        file.write(task.strip() + "\n")

    return f'Task added: "{task.strip()}"'


def list_tasks():
    if not TASKS_FILE.exists():
        return "No tasks found."

    tasks = TASKS_FILE.read_text(encoding="utf-8").strip().splitlines()

    if not tasks:
        return "No tasks found."

    result = ["Your tasks:"]
    for number, task in enumerate(tasks, start=1):
        result.append(f"{number}. {task}")

    return "\n".join(result)


def agent(user_input):
    text = user_input.strip()

    # Decision 1: Add a task
    if text.lower().startswith("add "):
        task = text[4:].strip()

        if not task:
            return "Please tell me the task you want to add."

        return add_task(task)

    # Unexpected case: user says only "add" or "add task"
    if text.lower() in ["add", "add task"]:
        return "Please tell me the task you want to add."

    # Decision 2: List tasks
    if text.lower() in ["list", "list tasks", "show tasks"]:
        return list_tasks()

    # Unexpected request
    return (
        "I do not understand that request.\n"
        'Try: "add Finish report" or "list tasks".'
    )


print("Simple Decision Agent")
print('Commands: "add <task>", "list tasks", or "exit"')
print()

while True:
    user_input = input("You: ")

    if user_input.lower().strip() == "exit":
        print("Agent: Goodbye!")
        break

    response = agent(user_input)
    print("Agent:", response)
    print()
