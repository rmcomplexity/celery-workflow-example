"""
.. module:: project.settings.celery
   synopsis: Celery settings
"""
CELERY_BROKER_URL = "amqp://user:pwd@rabbitmq:5672/test"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"
CELERY_WORKER_LOG_FORMAT = (
    "[CELERY] $(processName)s %(levelname)s %(asctime)s "
    "%(module)s '%(name)s.%(funcName)s:%(lineno)s: %(message)s"
)
