# nginx-auth

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` значению `example.com`.
3. Добавьте `location` блок для пути `/`, который обслуживает файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html)
4. Добавьте `location` блок для пути `/images`, который обслуживает файлы из архива [cats.zip](https://stepik.org/media/attachments/lesson/686238/cats.zip). Установите авторизованный вход для учетки: `design:SteveJobs1955`, т.е. логин `design`, пароль `SteveJobs1955`.
5. Добавьте `location` блок для пути `/gifs`, который обслуживает файлы из архива [gifs.zip](https://stepik.org/media/attachments/lesson/686238/gifs.zip). Установите авторизованный вход для учетки: `marketing:marketingP@ssword`.
6. Учетка `design` не должна иметь доступ на другие пути, тоже самое касается других учеток.

---
server{
    listen 8080;
    server_name example.com;
    location / {
        root /var/www/example.com;
        index index.html;
    }
    location /images {
        root /var/www/example.com;
        satisfy any;
        allow 127.0.0.1;
        deny all;
        auth_basic "Restricted content";
        auth_basic_user_file /etc/nginx/./htpasswd_design;
    }
    location /gifs {
        root /var/www/example.com;
        satisfy any;
        allow 127.0.0.1;
        deny all;
        auth_basic "Restricted content";
        auth_basic_user_file /etc/nginx/./htpasswd_marketing;
    }
}