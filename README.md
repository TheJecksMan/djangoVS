# Изучение
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/1200px-Django_logo.svg.png" width = 250 height = 100>


Первый проект для изучения framework'a Django

#### Установка зависимостей через командую строку
```
pip install -r requirements.txt 
```
#### Настройка nginx для deploy
```
server {
        listen 80;
        listen [::]:80;

        root /var/www/getlocationwifi_ngix;

        index index.html index.htm

        server_name <имя> www.<имя>;

        location /{
                proxy_pass http://127.0.0.1:8001;
                proxy_set_header X-Forwarded-Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
                add_header Access-Control-Allow-Origin *;
        }

        location /static/{
                alias <path to static files>;
        }

}
```

### Скрипт sh для запуска gunicorn
Основной скрипт для запуска проекта без лишних команд
```bash
#!/bin/bash
source <path to venv>/bin/activate
exec gunicorn -c "<path to project>/mysite/mysite/gunicorn_config.py" <custom name>.wsgi
```

### gunicorn_config.py
Конфигурация gunicorn для запуска проекта
```python
command = '<path to venv>/bin/gunicorn'
pythonpath = '<path to project>/mysite/mysite'
bind = '127.0.0.1:8001'
workers = 5 #Количество ядер * 2 + 1
user = 'ubuntu'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTING_MODULE=mysite.settings'
```

