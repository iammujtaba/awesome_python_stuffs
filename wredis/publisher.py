# Python code for publishing data
import time
import redis
import json

redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

for i in range(1, 100):
    redis_client.publish(
        'nfos',
        str(
            {
                "event": "new_fund_added",
                "fund_name": "Paisa banane wala fund",
                "isin": f"what_{i}",
                "scheme_code": f"leave_it_{i}",
            }
        ),
    )
    time.sleep(2)
