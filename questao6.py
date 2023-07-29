from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)


def verify_jwt_token(token):
    try:
        
        secret_key = '1234'
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


@app.before_request
def authenticate_request():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
        user_id = verify_jwt_token(token)
        if user_id:
            
            request.user_id = user_id
            return

   
    response = jsonify({'message': 'Unauthorized'})
    response.status_code = 401
    return response


@app.route('/')
def protected_route():
    
    user_id = getattr(request, 'user_id', None)
    return f'Rota protegida! Usuário autenticado: {user_id}' if user_id else 'Rota protegida! Usuário não autenticado.'

if __name__ == '__main__':
    app.run()
