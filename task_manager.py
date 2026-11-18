# task_manager.py
class TaskManager:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for i, task in enumerate(self.tasks):
            status = "[x]" if task.get('completed') else "[ ]"
            print(f"{i}. {status} {task['title']}")
    
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task index.")