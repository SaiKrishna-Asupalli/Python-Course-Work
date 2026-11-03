import json
data={"name":"sai","age":23}
r=json.dumps(data)
print(r)
k=json.loads(r)
print(k)
