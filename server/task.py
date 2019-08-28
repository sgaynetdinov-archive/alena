from enum import Enum

class Task:
    def __init__(self, command, status, result=None):
        self.command = command
        self.status = status
        self.result = result 

    def as_dict(self):
        return {'command': self.command, 'status': self.status, 'result': self.result}

    @classmethod
    def from_dict(cls, task_as_dict):
        return cls(task_as_dict['command'], task_as_dict['status'], task_as_dict['result']) 

