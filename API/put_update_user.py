import requests
from pprint import pprint
from get_token import access_token

_print = print
print = pprint

url = 'http://cdf4cd4c1e0a.sa.ngrok.io/api/v1/users/willian_couti@gmail.com'

headers = {
    'Authorization': access_token
}.replace

update_user_data = {
    "email": "willian_cout@gmail.com"
}

response = requests.put(url=url, headers=headers, json=update_user_data, )

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
