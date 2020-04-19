import redis

rds = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

rds.set('test', 'hello')

print(rds.get('test'))

# rds.delete('test')

rds.close()
