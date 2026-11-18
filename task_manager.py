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
    
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Task '{removed['title']}' deleted!")
        else:
            print("Invalid task index.")
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task index.")
            
    def add_task(self, title):
        if not title.strip():
            print("Error: Task title cannot be empty!")
            return False
        self.tasks.append({"title": title, "completed": False})
        print(f"Task '{title}' added.")
        return True
