import asyncio


async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    data = None
    while True:
        data = await reader.read(256)
        message = data.decode()
        addr, port = writer.get_extra_info("peernmae")
        print((f"Message from {addr}:{port}: {message!r}"))

        writer.write(data)
        await writer.drain()

        writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

if  __name__ == '__main__':
    asyncio.run(main())