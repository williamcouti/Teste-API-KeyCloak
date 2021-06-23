import requests
from pprint import pprint

_print = print
print = pprint

url = 'http://cdf4cd4c1e0a.sa.ngrok.io/api/v1/users'

get_all_user_data = {

        # 'birthdate': '2021-06-01T00:00:00.000Z',
        # 'cpf': '00000000024',
        # 'cpfVerified': 'False',
        # 'createdAt': '2021-06-14T14:12:02.334Z',
        # 'email': 'ssssssssss@asmdiorraisdee.com',
        # 'firstName': 'teste',
        # 'fromInvite': 38,
        # 'gender': 'male',
        # 'id': 151,
        # 'lastName': 'teste',
        # 'nickname': 'testee',
        # 'phone': '98217398127',
        # 'phoneVerified': 'False',
        # 'updatedAt': '2021-06-14T14:12:02.334Z'
}

response = requests.get(url=url, json=get_all_user_data)

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