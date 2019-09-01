import argparse
import sys
import time
import socket

def send(command, param, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(f'{command} {param}\n'.encode())
        got = sock.recv(1024)

    return got

def create_task_batch(command, params, host, port):
    task_uuid_items = []

    for param in params:
        task_uuid = send(command, param, host, port).decode()
        print(f'{task_uuid} - {command} {param}')
        task_uuid_items.append(task_uuid)

    while len(task_uuid_items):
        for task_uuid in task_uuid_items:
            status = send('status_task', task_uuid, host, port).decode()
            print(f'{task_uuid} - {status}')

            if status == 'выполнено':
                task_uuid_items.remove(task_uuid)
                got = send('result_task', task_uuid, host, port).decode()
                print(f'{task_uuid} - {got}')

            time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', default=8888, type=int)

    subparsers = parser.add_subparsers(title='commands', dest='command', metavar='')

    create_task_parser = subparsers.add_parser('create_task', help='Create task')
    create_task_parser.add_argument('command', help='Command: `reversed_string` or `transposition`')
    create_task_parser.add_argument('param', nargs='+')
    create_task_parser.add_argument('--batch', action='store_true')


    status_task_parser = subparsers.add_parser('status_task', help='Status task')
    status_task_parser.add_argument('uuid', help='Task uuid')

    result_task_parser = subparsers.add_parser('result_task', help='Result task')
    result_task_parser.add_argument('uuid', help='Task uuid')

    args = parser.parse_args()

    if 'create_task' == sys.argv[1]:
        command = f'create_task {args.command}'
        if args.batch:
            create_task_batch(command, args.param, args.host, args.port)
        else:
            param = args.param[0]
            print(send(command, param, args.host, args.port).decode())
    else:
        command = args.command
        param = args.uuid
        print(send(command, param, args.host, args.port).decode())

