# FROM rabbitmq:3.8
# EXPOSE 4369 5671 5672 15672
# RUN rabbitmq-plugins enable --offline rabbitmq_management
# CMD ["rabbitmq-server"]

FROM python:3.10.11-alpine
EXPOSE 8003
WORKDIR /app
COPY requirements.txt requirements.txt
COPY consumer.py consumer.py
COPY installreq.py installreq.py
RUN pip3 install -r requirements.txt
RUN pip3 install requests
RUN python3 installreq.py
COPY . /app/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8003"]
# CMD ["python3", "consumer.py"]