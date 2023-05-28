FROM rabbitmq:3.8
EXPOSE 4369 5671 5672 15672
RUN rabbitmq-plugins enable --offline rabbitmq_management
CMD ["rabbitmq-server"]

FROM python:3.10.11-alpine
# EXPOSE 8002
WORKDIR /app
COPY requirements.txt requirements.txt
COPY consumer.py consumer.py
RUN pip3 install -r requirements.txt
COPY . /app/
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]
CMD ["python3", "consumer.py"]