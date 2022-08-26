import redis


r = redis.Redis(host='10.10.89.138', port=16379, db=0, password="CMPvUhMN", decode_responses=True)
print(r.keys())

