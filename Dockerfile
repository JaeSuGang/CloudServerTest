FROM python:3.9

WORKDIR /app

RUN sudo apt update

COPY requirements.txt

RUN sudo pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]