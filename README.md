Vou explicar o código em Python e HTML em mais detalhes:

**Código do servidor WebSocket (server.py):**

1. Importando módulos:
   ```python
   import asyncio
   import websockets
   ```
   Essas são as bibliotecas necessárias para criar um servidor WebSocket em Python. O `asyncio` é usado para trabalhar com tarefas assíncronas, e o `websockets` é uma biblioteca que facilita a implementação de WebSocket em Python.

3. `connected_clients`:
   ```python
   connected_clients = set()
   ```
   Este é um conjunto que será usado para manter o controle de todas as conexões de clientes que se conectam ao servidor WebSocket.

4. Função `chat_server`:
   ```python
   async def chat_server(websocket, path):
   ```
   Esta é uma função assíncrona que lida com a comunicação entre o servidor e os clientes.

5. Adicionar clientes:
   ```python
   connected_clients.add(websocket)
   ```
   Quando um novo cliente se conecta, adicionamos sua conexão ao conjunto `connected_clients`.

6. Loop para receber mensagens:
   ```python
   async for message in websocket:
   ```
   Usamos um loop assíncrono para receber mensagens enviadas pelos clientes.

7. Enviando mensagens para todos os clientes:
   ```python
   for client in connected_clients:
       await client.send(message)
   ```
   Quando uma mensagem é recebida de um cliente, ela é retransmitida para todos os outros clientes conectados ao servidor.

8. Lidando com desconexões:
   ```python
   finally:
       connected_clients.remove(websocket)
   ```
   Se um cliente desconectar, garantimos que sua conexão seja removida da lista de clientes conectados.

10. Iniciar o servidor WebSocket:
    ```python
    start_server = websockets.serve(chat_server, "localhost", 8080)
    ```
    Isso inicia o servidor WebSocket na porta 8080.

11. Executar o loop de eventos:
    ```python
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    ```
    Essas linhas executam o loop de eventos asyncio, permitindo que o servidor WebSocket continue a ouvir conexões e mensagens indefinidamente.

**Código HTML (index.html):**

- A página HTML é simples e contém um campo de entrada de mensagens, um botão "Enviar" e uma área de exibição de mensagens.
- Quando um cliente abre a página, ele cria uma conexão WebSocket com o servidor em `ws://localhost:8080`.
- Quando o cliente envia uma mensagem, a função `sendMessage()` é chamada, que envia a mensagem para o servidor usando o WebSocket.
- Quando o cliente recebe uma mensagem do servidor, a mensagem é adicionada como um novo elemento `<p>` à área de exibição de mensagens.

Espero que isso ajude a entender o funcionamento do código. Se você tiver alguma dúvida específica ou precisar de mais informações sobre alguma parte do código, sinta-se à vontade para perguntar.