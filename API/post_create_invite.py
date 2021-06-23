import requests
from pprint import pprint

_print = print
print = pprint

url = 'http://cdf4cd4c1e0a.sa.ngrok.io/api/v1/invite/willian_couti@gmail.com'

invite_data = {
   # "nome": "Luiz Otávio",
   # "password": "123456",
   #"email": "luiz@email.com"
}

response = requests.post(url=url, json=invite_data)

if response.status_code == 200:
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
    print(response.reason)
    print('Erro na requisição')
    response_data = response.json()
    print(response_data)
