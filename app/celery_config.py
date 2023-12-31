from celery import Celery
from kombu import Exchange, Queue
from celery.schedules import crontab

broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'

celery = Celery(
    'app.tasks',
    broker=broker_url,
    include=['app.tasks.email_tasks']
)

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'
enable_utc = True

task_queues = [
    Queue('default', Exchange('default'), routing_key='default'),
]
task_default_queue = 'default'
task_default_exchange_type = 'direct'
task_default_routing_key = 'default'

celery.conf.beat_schedule = {
    'send-confirmation-email-task': {
        'task': 'app.tasks.email_tasks.send_confirmation_email',
        'schedule': 10.0,
        'options': {
            'queue': 'celery',
        }
    },
}