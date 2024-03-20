# Python code for subscribing to real-time analytics data
import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Subscribe to the 'analytics' channel
pubsub = redis_client.pubsub()
pubsub.subscribe('nfos')

# Process incoming messages
for message in pubsub.listen():
    print('Received message:', message['data'])

'''
connect to redis cli and show it to audience both python subscriber and redis-cli subscriber :-)

'''