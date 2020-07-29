import redis

#
# Conexão com o redis
#
cliente = redis.Redis(host='localhost', port=6379, db=0)