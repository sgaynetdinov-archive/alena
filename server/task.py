from enum import Enum

class Task:
    def __init__(self, command, status):
        self.command = command
        self.status = status

    def as_dict(self):
        return {'command': self.command, 'status': self.status}

    @classmethod
    def from_dict(cls, task_as_dict):
        return cls(task_as_dict['command'], task_as_dict['status']) 

