import requests
from pprint import pprint
from get_token import access_token

_print = print
print = pprint

url = 'http://cdf4cd4c1e0a.sa.ngrok.io/api/v1/users/willian_couti@gmail.com'

headers = {
    'Authorization': access_token
}

delete_user_data = {
    # "nome": "Let",
    # "sobrenome": "Vieira",
    # "email": "luana2@email.com",
    # "idade": "50",
    # "peso": "80.04",
    # "altura": "1.90"
}

response = requests.delete(url=url, headers=headers, json=delete_user_data)

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
