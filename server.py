import asyncio
import websockets

# Dicionário para manter as conexões dos clientes
connected_clients = set()

async def chat_server(websocket, path):
    # Adicionar o novo cliente à lista de conexões
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            # Enviar a mensagem recebida para todos os clientes conectados
            for client in connected_clients:
                await client.send(message)
    finally:
        # Remover o cliente quando ele desconectar
        connected_clients.remove(websocket)

# Iniciar o servidor WebSocket na porta 8080
start_server = websockets.serve(chat_server, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
