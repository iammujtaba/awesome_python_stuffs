import time
from wcelery.celery import celery
from wredis.cache import RedisCache

cache = RedisCache()

# Basic celery task
@celery.task
def low_priority_sum_task(a, b):
    time.sleep(1)
    print(f"Hi, I am low priority sum of {a} and {b} is {a+b}")
    return a+b
