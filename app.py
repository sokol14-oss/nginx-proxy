from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    xff = request.headers.get('X-Forwarded-For', 'Header not found')
    return f"Получен заголовок X-Forwarded-For: {xff}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
