import requests

url = "http://localhost:4000/predict"
file = {"file": open("test_image.jpeg", "rb")}
response = requests.post(url, files=file)

print(response.json())
