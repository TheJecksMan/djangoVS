command = '<path to venv>/bin/gunicorn'
pythonpath = '<path to project>/mysite/mysite'
bind = '127.0.0.1:8001'
workers = 5  # Количество ядер * 2 + 1
user = 'ubuntu'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTING_MODULE=mysite.settings'
