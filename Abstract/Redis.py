import redis

#
# Conexão com o redis
#
connection = redis.Redis(host='localhost', port=6379, db=0)

# https://www.youtube.com/watch?v=Hbt56gFj998
# cursor, keys = r.scan(match='123*')
# data = r.mget(keys)
# connection.delete('1')
connection.lpush('pessoa', [1, 2])
for key in connection.scan_iter():
    print(key)