FROM python:3.6-alpine

LABEL MAINTAINER="Faizan Bashir <faizan.ibn.bashir@gmail.com"

WORKDIR /var/www/

ADD app/requirements.txt /var/www/requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

ADD . /var/www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]