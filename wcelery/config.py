import os
broker_url = os.environ.get("CELERY_BROKER_URL","redis://localhost:6379/0")
result_backend = os.environ.get("CELERY_RESULT_BACKEND","redis://localhost:6379/0")
# task_time_limit=10