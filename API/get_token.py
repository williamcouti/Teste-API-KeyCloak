access_token = ''

with open('token.txt', 'r') as file:
    access_token += file.read()
    print(access_token)
