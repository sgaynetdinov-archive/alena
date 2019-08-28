from server import Task

def test_as_json():
    task = Task('reversed string', 'in progress')

    assert task.as_dict() == {'command': 'reversed string', 'status': 'in progress'}


def test_from_json():
   j = {'command': 'reversed string', 'status': 'in progress'}
   task = Task.from_dict(j)

   assert task.command == 'reversed string'
   assert task.status == 'in progress'
 
