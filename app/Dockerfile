FROM pypy:3

WORKDIR /usr/src/app

COPY . .
RUN pip3 install -r requirements.txt

CMD [ "pypy3", "main.py" ]