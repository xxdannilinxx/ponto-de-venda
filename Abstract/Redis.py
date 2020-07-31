import redis
import json


#
# Conexão com o redis
#
r = redis.Redis(host='localhost', port=6379, db=0)


# mydict = { 'var1' : 5, 'var2' : 9, 'var3': [1, 5, 9] }
# rval = json.dumps(mydict)
# r.set('key1', rval)

# data = r.get('key1')
# result = json.loads(data)
# arr = result['var3']
# for i in result:
#     print(i)
#     print(result[i])




# print(result)
# print(arr)
