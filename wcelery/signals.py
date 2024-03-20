
# from celery.signals import task_postrun,task_prerun,task_revoked,task_retry,task_failure,task_success,task_unknown,task_rejected,task_revoked,task_sent,task_started,task_received,task_rejected,task_unknown

# @task_prerun.connect()
# def task_prerun(**kwargs): # sent when a task is about to be executed
#     try:
#         print(f"celery task started {kwargs}")
#     except Exception as e:
#         print(f"error in celery signal {e}")

# @task_revoked.connect()
# def task_revoked(**kwargs): # sent when a task is revoked
#     try:
#         print(f"celery task revoked {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")

# @task_retry.connect()
# def task_retry(**kwargs): # sent when a task is about to be retried
#     try:
#         print(f"celery task retry {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")

# @task_postrun.connect()
# def task_postrun(**kwargs): # sent after a task has been executed
#     try:
#         print(f"celery task completed {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")


# @task_failure.connect()
# def task_failure(**kwargs): # sent when a task fails
#     try:
#         print(f"celery task failure {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")

# @task_success.connect()
# def task_success(**kwargs): # sent when a task succeeds
#     try:
#         print(f"celery task success {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")

# @task_unknown.connect()
# def task_unknown(**kwargs): # sent when a task is not registered.
#     try:
#         print(f"celery task unknown {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")

# @task_rejected.connect()
# def task_rejected(**kwargs): # sent when a task is rejected by the worker
#     try:
#         print(f"celery task rejected {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")

# @task_sent.connect()
# def task_sent(**kwargs): # sent when a task message is sent to the broker
#     try:
#         print(f"celery task sent {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")

# @task_started.connect()
# def task_started(**kwargs): # sent when a task is about to be executed
#     try:
#         print(f"celery task started {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")

# @task_received.connect()
# def task_received(**kwargs): # sent when a task message is received by a worker
#     try:
#         print(f"celery task received {kwargs}")
#     except Exception as e:
#             print(f"error in celery signal {e}")
