FROM python:3.10.11-alpine
EXPOSE 8000
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app/
RUN python listener.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]