import os
from celery import Celery
from celery.utils.log import get_task_logger
from kombu import Queue, Exchange

#constants
CELERY_APPS = ["wcelery.tasks","wcelery.low.tasks"]

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

# 1) "67633bb1-1a22-4fa3-89db-4bb1a437ebb0"
# 2) "4d1c0d99-e03b-4524-9cf1-95c870dbaccf"

#celery app
celery = Celery('tasks',include=CELERY_APPS)
celery_log = get_task_logger(__name__)
celery.conf.broker_url = CELERY_BROKER_URL
celery.conf.result_backend = CELERY_RESULT_BACKEND
# celery.conf.task_time_limit=5












# celery.conf.task_routes = {'wcelery.tasks.*': {'queue': 'wcelery_queue'},
#                             'wcelery.low.tasks.*': {'queue': 'wcelery_low_queue'}}

# celery.conf.task_queues = (
#     Queue('wcelery_queue', Exchange('wcelery_queue'), routing_key='wcelery.tasks.*'),
#     Queue('wcelery_low_queue', Exchange('wcelery_low_queue'), routing_key='wcelery.low.tasks.*'))


# celery.config_from_object('wcelery.config') #alternative way to configure celery













# celery -A wcelery.celery inspect 















#celery_log config

# # celery.conf.worker_prefetch_multiplier = 1
# celery.conf.task_acks_late = True
# celery.conf.task_acks_on_failure_or_timeout = False
# celery.conf.task_reject_on_worker_lost = True
# celery.conf.broker_transport_options = {'visibility_timeout': 2}  # 30mins
# celery.conf.broker_transport_options = {'visibility_timeout': 20, 'global_keypreix':'wcelery'}  # 30mins
# celery.conf.result_backend_transport_options = {'visibility_timeout': 20}  # 30mins
# # celery.conf.broker_connection_retry_on_startup = True
# celery.conf.task_default_queue = 'wcelery_queue'



























# from celery.signals import task_postrun ,task_prerun #task_revoked,task_retry,task_failure,task_success,task_unknown,task_rejected,task_revoked,task_sent,task_started,task_received,task_rejected,task_unknown
# #celery signals

# # @task_prerun.connect()
# # def task_prerun(**kwargs): # sent when a task is about to be executed
# #     try:
# #         print(f"celery task started {kwargs}")
# #     except Exception as e:
# #         print(f"error in celery signal {e}")

# # @task_revoked.connect()
# # def task_revoked(**kwargs): # sent when a task is revoked
# #     try:
# #         print(f"celery task revoked {kwargs}")
# #     except Exception as e:
# #             print(f"error in celery signal {e}")

# # @task_retry.connect()
# # def task_retry(**kwargs): # sent when a task is about to be retried
# #     try:
# #         print(f"celery task retry {kwargs}")
# #     except Exception as e:
# #             print(f"error in celery signal {e}")

# @task_postrun.connect()
# def task_postrun(**kwargs): # sent after a task has been executed
#     try:
#         print(f"celery task completed {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")


# # @task_failure.connect()
# # def task_failure(**kwargs): # sent when a task fails
# #     try:
# #         print(f"celery task failure {kwargs}")
# #     except Exception as e:
# #             print(f"error in celery signal {e}")

# # @task_success.connect()
# # def task_success(**kwargs): # sent when a task succeeds
# #     try:
# #         print(f"celery task success {kwargs}")
# #     except Exception as e:
# #             print(f"error in celery signal {e}")

# # @task_unknown.connect()
# # def task_unknown(**kwargs): # sent when a task is not registered.
# #     try:
# #         print(f"celery task unknown {kwargs}")
# #     except Exception as e:
# #             print(f"error in celery signal {e}")

# # @task_rejected.connect()
# # def task_rejected(**kwargs): # sent when a task is rejected by the worker
# #     try:
# #         print(f"celery task rejected {kwargs}")
# #     except Exception as e:
# #             print(f"error in celery signal {e}")

# # @task_sent.connect()
# # def task_sent(**kwargs): # sent when a task message is sent to the broker
# #     try:
# #         print(f"celery task sent {kwargs}")
# #     except Exception as e:
# #             print(f"error in celery signal {e}")

# # @task_started.connect()
# # def task_started(**kwargs): # sent when a task is about to be executed
# #     try:
# #         print(f"celery task started {kwargs}")
# #     except Exception as e:
# #             print(f"error in celery signal {e}")

# # @task_received.connect()
# # def task_received(**kwargs): # sent when a task message is received by a worker
# #     try:
# #         print(f"celery task received {kwargs}")
# #     except Exception as e:
# #             print(f"error in celery signal {e}")





