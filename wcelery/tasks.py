import time
from wcelery.celery import celery
from wredis.cache import RedisCache
from celery import group, chain


cache = RedisCache()

# Basic celery task
@celery.task
def sum_of_two_number(a, b):
    # time.sleep(10)
    print(f"sum of {a} and {b} is {a+b}")
    return a+b

@celery.task
def mul_of_two_number(a, b):
    print(f"multiplication of {a} and {b} is {a*b}")
    return a*b

# result = sum_of_two_number.delay(1,2)
# result = sum_of_two_number.apply_async(args=[3,4],countdown=10)

# check if result is ready or not? 
# result.ready()
# result.get(propagate=False) #propagate exception


# call using delay and apply_async
# result = sum_of_two_number.delay(1,2)
# sum_of_two_number.apply_async(args=[3,4],countdown=10)

# grouping and chaining the link
group(sum_of_two_number.s(i, i) for i in range(10))().get()
res = chain(sum_of_two_number.s(4, 4) | mul_of_two_number.s(8) | sum_of_two_number.s(6))().get()
# res.parent.get() # res.parent.parent.get() # res.parent.parent.parent.get()


# task dependencies a->b->c

# sum_of_two_number.apply_async((2, 2), link=mul_of_two_number.s(16))

@celery.task
def visibility_timeout_test(key):
    # change visibility timeout to 1 seconds
    val = cache.get(key) or 0
    val = int(val) + 1
    cache.set("hello", val)
    if val == 5:
        return
    print(f"key: {key} val: {val}")
    time.sleep(60)
