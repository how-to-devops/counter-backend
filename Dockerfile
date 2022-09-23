FROM python:3.10-alpine

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY app/main.py /app/main.py

CMD ["python3", "main.py"]