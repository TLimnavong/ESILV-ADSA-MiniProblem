FROM python:3.6

WORKDIR /

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT ['python3', '-m', 'miniproblem']

CMD ['-u', 'miniproblem']
