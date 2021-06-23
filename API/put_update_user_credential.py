import requests
from pprint import pprint
from get_token import access_token

_print = print
print = pprint

url = 'http://cdf4cd4c1e0a.sa.ngrok.io/api/v1/users/credential/hotmail@hotmail.com'

headers = {
    'Authorization': access_token
}

credentials_data = {
    "password": " test123 "
    # "sobrenome": "Vieira",
    # "email": "luana2@email.com",
    # "idade": "50",
    # "peso": "80.04",
    # "altura": "1.90"
}

response = requests.put(url=url, json=credentials_data, headers=headers)

if response.status_code == 200:
    # Success
    message = "Status da sua requisição e:"
    print(message)
    print(response.status_code)
    print(response.reason)
    print('Requisição executada com sucesso')
    response_data = response.json()
else:
    # Errors
    message = "Status da sua requisição e:"
    print(message)
    print(response.status_code)
    print(response.reason)
    print('Erro na requisição')
    response_data = response.json()
    print(response_data)
