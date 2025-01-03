FROM python:3.11

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python setup.py install

ENTRYPOINT [ "ShieldCipher" ]
