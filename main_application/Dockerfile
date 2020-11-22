FROM python:3.8-slim


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install --upgrade protobuf

COPY . .

EXPOSE ${SIDECAR_GRPC_PORT}

CMD ["/usr/local/bin/python3","-u", "/app/run.py"]
