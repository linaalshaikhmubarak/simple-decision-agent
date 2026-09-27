# Simple Decision Agent

This is a very small Python project for learning how an Agent:

1. Receives user input
2. Decides what action to take
3. Executes the action
4. Handles unexpected or incomplete requests

## Files

- `agent.py` - the Agent
- `tasks.txt` - the file the Agent reads from and writes to

## Run the project

Open the project folder in Visual Studio Code.

Open the terminal and run:

```bash
python3 agent.py
```

## Test examples

### Add a task

```text
add Finish report
```

The Agent decides to use the **Add Task** action and saves the task in `tasks.txt`.

### List tasks

```text
list tasks
```

The Agent reads `tasks.txt` and shows the saved tasks.

### Missing information

```text
add task
```

The Agent detects that the task name is missing and asks for more information.

### Unknown request

```text
hello
```

The Agent explains that it does not understand the request and shows valid examples.

## Main idea

User Input -> Decide -> Check -> Execute -> Respond
