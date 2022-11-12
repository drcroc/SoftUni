# from task import Task
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'

        return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str):
        for t in self.tasks:
            if t.name == task_name:
                t.completed = True
                return f'Completed task {task_name}'

        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        completed_tasks = 0

        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                completed_tasks += 1

        return f'Cleared {completed_tasks} tasks.'

    def view_section(self):
        result = [f'Section {self.name}']
        [result.append(t.details()) for t in self.tasks]

        return '\n'.join(result)
