
import requests
import json
json_url='http://dummy.restapiexample.com/api/v1/employees'
data = requests.get(json_url)
print(data.content)

