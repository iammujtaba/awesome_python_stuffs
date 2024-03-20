import json
from wredis.cache import RedisCache


b_cache = RedisCache()

dschemes = {'wschemecode': 'MMRE117IORGGGR', 'amc': 1045}

# I need to set dschemes in redis cache 
# what are the ways to achieve this?





































key = "dschemes"
b_cache.set(key, dschemes)























bytes_data = json.dumps(dschemes)
b_cache.set(key, bytes_data)

res = b_cache.get(key)
print(type(res)) # ???
res = res.decode()
print(type(res)) # ???
res = json.loads(res)
print(type(res)) # ???
print(f"res: {res}")



























# Total efforts to set 2 line and get 4 lines of code
# can we do better?





















s_cache = RedisCache(decode_responses=True)

res = s_cache.get(key)
print(type(res)) # ???
res = json.loads(res)
print(type(res)) # ???  
print(f"res: {res}")
























cc = s_cache.client
cc.hset(key,mapping = dschemes)

resp = cc.hgetall(key)
print(type(resp)) # ???
print(f"resp: {resp}")


