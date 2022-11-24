import asyncio


async def connection_server(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    """Server works with client"""
    addr = writer.get_extra_info("peername")  # give address of client

    print(f"Server accept connection from {addr}")
    msg = 1
    while not msg:
        data = await reader.read(1024)
        msg = data.decode()
        print(f"Message from {addr}:{port}: {msg}")

        writer.write(data)  # send back info
        await writer.drain()  # make clear that msg send

    writer.close()
    await writer.wait_closed()


async def run_server(host, port):
    """Server, waiting connection"""
    print("Server starts, waiting for connections")
    work_server = await asyncio.start_server(connection_server, host, port)
    await work_server.serve_forever()


if __name__ == '__main__':
    host = 'localhost'
    port = 7673
    asyncio.run(run_server(host, port))
