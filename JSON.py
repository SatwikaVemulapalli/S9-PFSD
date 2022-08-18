import json
#Converting json into python
x='{"name":"Satwika","age":18,"branch":"cse"}'
y=json.loads(x)
print(y["branch"])

#Converting python into json
a={"name":"Satwika","id":509,"cgpa":9.8}
b=json.dumps(a)
print(b)

