import asyncio
from concurrent.futures import ThreadPoolExecutor

from server.handler import handler 
from server.worker import worker 
from server.queue import get_queue

queue = get_queue()

async def handlerTCP(reader, writer):
    data = await reader.readline()
    message = data.decode()
    
    got = await handler(message)

    writer.write(got.encode())
    await writer.drain()
    writer.close()

async def main(host, port, count_worker):
    server = await asyncio.start_server(handlerTCP, host, port)

    print(f'Run server on {host}:{port}')
    print(f'Worker: {count_worker}')

    with ThreadPoolExecutor(max_workers=count_worker) as pool:
        await server.get_loop().run_in_executor(pool, worker)

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', default=8888, type=int)
    parser.add_argument('--worker', default=1, type=int)
    args = parser.parse_args()

    asyncio.run(main(args.host, args.port, args.worker))

