from .abstract_sender import AbstractSender
import websockets
import asyncio
import json

class RubyCOPSender(AbstractSender):
    def __init__(self, ip, port):
        super().__init__(ip, port)

    async def send_measures(self, message):
        async with websockets.connect(f"ws://{self.ip}:{self.port}") as websocket:
            message_json = json.dumps(message)
            await websocket.send(message_json)
            await websocket.close()

    def send_data(self, data):
        try:
            asyncio.run(self.send_measures(data))
            print(f"The data was successfully sent it to {self.ip}:{self.port} !")
        except ValueError as e:
            print(f"ValueError: {e}")