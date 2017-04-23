FROM python:3

WORKDIR /usr/src/app
RUN mkdir -p /usr/src/app
RUN pip install gunicorn==19.7.1
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app
RUN pip install .

EXPOSE 8000
CMD gunicorn -w 4 -b 0.0.0.0:8000 asnlookup_web:app
