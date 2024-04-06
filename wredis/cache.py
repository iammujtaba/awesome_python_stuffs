import os
import redis

REDIS_CACHE_CLIENT_URL = os.environ.get("REDIS_CACHE_CLIENT_URL","redis://localhost:6379/0")


class RedisCache:
    def __init__(self, timeout = 60*60*1,total_nodes=3,service_key="aps", decode_responses=False):
        self.timeout = timeout
        self.total_nodes = total_nodes
        self.service_key = service_key
        self.decode_responses = decode_responses
        self.client = self.get_cluster_client()

    def get_cluster_client(self):
        return redis.from_url(REDIS_CACHE_CLIENT_URL,decode_responses=self.decode_responses)

    def get(self, key):
        key = f"{self.service_key}_{key}"
        return self.client.get(key)
    
    def set(self, key, value):
        key = f"{self.service_key}_{key}"
        return self.client.set(key, value, ex=self.timeout)

    def delete(self, key):
        key = f"{self.service_key}_{key}"
        return self.client.delete(key)
    