FROM python:3.8-slim


WORKDIR /sidecar

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE ${SIDECAR_GRPC_PORT}

CMD ["/usr/local/bin/python3","-u", "/sidecar/run.py"]
