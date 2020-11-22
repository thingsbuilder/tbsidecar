from concurrent import futures
import logging

import grpc

import app.greet_pb2
import app.greet_pb2_grpc


class Greeter(app.greet_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return app.greet_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    print ("Starting Python Sidecar...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    app.greet_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
