import requests
from pprint import pprint

_print = print
print = pprint

url = 'http://0eba13b98a1e.ngrok.io/api/v1/login'

user_data = {

    "email": "willian_couti@gmail.com",
    "password": "teste123"
}

response = requests.post(url=url, json=user_data)

if response.status_code == 200:
    # Success
    message = "Status da sua requisição e:"
    print(message)
    print(response.status_code)
    print(response.reason)
    print('Requisição executada com sucesso')
    response_data = response.json()
    access_token = response_data['data']['user']['access_token']
    with open('token.txt', 'w') as file:
        file.write(access_token)
        print('Seu token e:')
        print(access_token)
    print(response_data)
else:
    # Errors
    message = "Status da sua requisição e:"
    print(message)
    print(response.status_code)
    print(response.reason)
    print('Erro na requisição')
    response_data = response.json()
    print(response_data)


