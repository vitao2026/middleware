import jwt


secret_key = '1234'


def generate_jwt_token(user_id):
    payload = {'user_id': user_id}
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


user_id = 'user123'
token = generate_jwt_token(user_id)


print(token)
