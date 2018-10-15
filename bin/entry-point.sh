#!/usr/bin/dumb-init /bin/sh
python3.6 /srv/www/project/project/manage.py runserver 0.0.0.0:8000 2>&1 &
celery -A project.celery_app:app --workdir=/srv/www/project/project worker --loglevel=debug

