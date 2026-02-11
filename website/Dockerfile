FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY ./website/nginx.conf /etc/nginx/conf.d/default.conf
COPY ./website/ /usr/share/nginx/html/
