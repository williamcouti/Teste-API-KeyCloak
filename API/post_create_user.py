from pprint import pprint
import requests

_print = print
print = pprint

url = 'http://cdf4cd4c1e0a.sa.ngrok.io/api/v1/users?code=b51e4c59-10f8-46ca-8cf2-09f62ef29b5d'

user_data = {
    "email": "willian_couti@gmail.com",
    "firstName": "teste",
    "password": "teste123 ",
    "lastName": "teste",
    "phone": "98217398127",
    "birthdate": "2021-06-01",
    "cpf": "00000000024",
    "gender": "male",
    "nickname": "testee"
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
