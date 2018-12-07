FROM python:3.6-alpine

LABEL MAINTAINER="Faizan Bashir <faizan.ibn.bashir@gmail.com"

WORKDIR /var/www/

ADD requirements.txt /var/www/requirements.txt
RUN pip install -r requirements.txt

ADD . /var/www

EXPOSE 5000

CMD [ "python", "app.py" ]