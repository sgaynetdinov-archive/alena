import argparse
import socket

def send(command, param, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(f'{command} {param}\n'.encode())
        got = sock.recv(1024)

    return got

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('param')
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', default=8888, type=int)

    args = parser.parse_args()

    print(send(args.command, args.param, args.host, args.port).decode())

