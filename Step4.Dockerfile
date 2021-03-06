FROM python:3.8-slim

WORKDIR /

COPY ./requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /

CMD ["python3", "-m", "miniproblem", "4"]
