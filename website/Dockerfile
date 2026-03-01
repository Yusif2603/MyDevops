FROM nginx:alpine

# Копируем файлы сайта
COPY . /usr/share/nginx/html

# Копируем твой конфиг (который мы создали шагом ранее)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Проверяем, что папки для сертификатов существуют (чтобы Nginx не ругался)
RUN mkdir -p /etc/letsencrypt
