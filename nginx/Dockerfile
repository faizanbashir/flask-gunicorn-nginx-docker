FROM faizanbashir/alpine:latest
LABEL MAINTAINER="Faizan Bashir <faizan.ibn.bashir@gmail.com>"

RUN apk --update add nginx && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    mkdir /etc/nginx/sites-enabled/ && \
    mkdir -p /etc/letsencrypt/webrootauth && \
    mkdir -p /run/nginx && \
    rm -rf /var/www/* && \
    rm -rf /etc/nginx/conf.d/default.conf && \
    touch /var/www/favicon.ico && \
    rm -rf /var/cache/apk/*

#COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/app.conf /etc/nginx/conf.d/app.conf

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]