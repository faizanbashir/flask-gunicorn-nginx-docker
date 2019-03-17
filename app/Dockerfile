FROM python:3.6.8-alpine3.9

LABEL MAINTAINER="Faizan Bashir <faizan.ibn.bashir@gmail.com"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD app/requirements.txt /var/www/requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Add user for laravel application
RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

# Copy existing application directory contents
#COPY . /var/www

# Copy existing application directory permissions
COPY --chown=www:www . /var/www

# Change current user to www
USER www

#ADD . /var/www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]