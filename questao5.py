from flask import Flask
import time

app = Flask(__name__)


def log_request_time_middleware(app):
    def middleware(environ, start_response):
        
        request_time = time.strftime('%Y-%m-%d %H:%M:%S')
        method = environ['REQUEST_METHOD']
        url = environ['PATH_INFO']

        
        response = app(environ, start_response)

        
        response_time = time.strftime('%Y-%m-%d %H:%M:%S')

        
        print(f"Hora solicitação: {request_time} | Método: {method} | URL: {url} | Hora Respondida: {response_time}")

        return response

    return middleware


app.wsgi_app = log_request_time_middleware(app.wsgi_app)

@app.route('/')
def hello_world():
    return 'Gerfatory 4.0!'

if __name__ == '__main__':
    app.run()