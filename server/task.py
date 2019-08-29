import json

class Task:
    def __init__(self, command, status, result=None, uuid=None):
        self.command = command
        self.status = status
        self.result = result 
        self.uuid = uuid 

    def as_json(self):
        data = {
                'command': self.command,
                'status': self.status,
                'result': self.result,
                'uuid': self.uuid
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, task_as_json):
        task_as_dict = json.loads(task_as_json)
        return cls(**task_as_dict) 

