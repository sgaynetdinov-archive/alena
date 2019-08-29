from enum import Enum

class Task:
    def __init__(self, command, status, result=None, uuid=None):
        self.command = command
        self.status = status
        self.result = result 
        self.uuid = uuid 

    def as_dict(self):
        return {
                'command': self.command,
                'status': self.status,
                'result': self.result,
                'uuid': self.uuid
        }

    @classmethod
    def from_dict(cls, task_as_dict):
        return cls(**task_as_dict) 

