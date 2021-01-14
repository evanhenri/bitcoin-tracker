#!/usr/bin/env bash

set -e

mkdir -p /var/log/supervisor/{celery,celery_beat,gunicorn}

python /app/manage.py prepare_app --collectstatic
python /app/manage.py prepare_app --migrate

exec supervisord -c /etc/supervisor/supervisord.conf
