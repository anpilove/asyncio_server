import asyncio


async def run_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    message = 'Hello, world'

    writer.write(message.encode())
    await writer.drain()
    while True:
        data = await reader.read(100)
        if not data:
            raise Exception("socket closed")

        print(f"Received {data.decode()!r}")


if  __name__ == '__main__':
    asyncio.run(run_client('127.0.0.1', 8888))

