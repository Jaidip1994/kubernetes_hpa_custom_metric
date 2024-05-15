FROM python:slim
WORKDIR /app
COPY * ./
RUN apt-get update && \
    apt-get install -y gcc && \
    pip install flask prometheus_client && \
    apt-get remove -y gcc && \
    apt-get autoremove -y
CMD [ "python", "main.py" ]
