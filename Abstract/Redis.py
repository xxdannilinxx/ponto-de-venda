import redis
import json


#
# Conexão com o redis
#
r = redis.Redis(host='localhost', port=6379, db=0)