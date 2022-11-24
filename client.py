import asyncio


async def client(host,port):
    reader, writer = await asyncio.open_connection(host, port)
    print(f"Connected to server {host} {port} ")
    writer.write(input("Print text to send").encode())
    await writer.drain()

    while True:
        data = await reader.read(1024)

        if not data:
            raise Exception("Server close")

        print(f"Received {data.decode()}")


# async def run_client():

if __name__ == '__main__':
    asyncio.run(client('localhost',7673))