#!/bin/bash
source <path to venv>/bin/activate
exec gunicorn -c "<path to project>/mysite/mysite/gunicorn_config.py" <custom name>.wsgi