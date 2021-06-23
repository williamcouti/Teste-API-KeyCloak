import requests
from pprint import pprint

_print = print
print = pprint

url = 'http://cdf4cd4c1e0a.sa.ngrok.io/api/v1/users/willian_couti@gmail.com'

user_data = {
    # "nome": "Luana 2",
    # "sobrenome": "Vieira",
    # "email": "luana2@email.com",
}

response = requests.get(url=url, json=user_data)

if response.status_code == 300:
    # Success
    message = "Status da sua requisição e:"
    print(message)
    print(response.status_code)
    print(response.reason)
    print('Requisição executada com sucesso')
    response_data = response.json()
    print(response_data)
else:
    # Errors
    message = "Status da sua requisição e:"
    print(message)
    print(response.status_code)
    print('Erro na sua requisição')
    print(response.reason)
    response_data = response.json()
    print(response_data)
