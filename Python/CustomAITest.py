import requests  
import json
url = ""
image = {"Url": "https://media.deseretdigital.com/file/8699523496?resize=width_1200&type=jpg&c=14&a=e0717f4c"}
headers = { "Content-Type": "application/json", 
           "Prediction-Key": ""}
r=requests.post(url, data=json.dumps(image), headers=headers)
print(r.text)
