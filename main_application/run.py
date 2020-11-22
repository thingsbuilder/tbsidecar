from time import sleep

import grpc

import app.greet_pb2 as greet_pb2
import app.greet_pb2_grpc as greet_pb2_grpc
from app.settings.settings import Settings

PORT = Settings().GRPC_PORT

while True:
    try:
        with grpc.insecure_channel(f"127.0.0.1:{PORT}") as channel:
            stub = greet_pb2_grpc.GreeterStub(channel)
            response = stub.SayHello(greet_pb2.HelloRequest(name='Wonderful Person'))
            print("Greeter client received: " + response.message)
    except:
        pass
    sleep(5)
