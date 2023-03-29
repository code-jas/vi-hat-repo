import requests


def get_message(api_url):
    response = requests.get(api_url)
    data = response.json()
    message = data['message']
    return message

message = get_message('http://127.0.0.1:5000/api/v1/endpoint')
print(message)