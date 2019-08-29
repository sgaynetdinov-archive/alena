from server.task import Task

def test_as_json():
    task = Task('reversed string', 'in progress')

    assert task.as_dict() == {'command': 'reversed string', 'status': 'in progress', 'result': None, 'uuid': None}


def test_from_json():
   j = {'command': 'reversed string', 'status': 'in progress', 'result': '100'}
   task = Task.from_dict(j)

   assert task.command == 'reversed string'
   assert task.status == 'in progress'
   assert task.result == '100'
   assert task.uuid == None
 
