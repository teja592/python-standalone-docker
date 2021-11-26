from flask import Flask
from redis import Redis
app = Flask(__name__)

@app.route('/')
def hello():
    #count = redis.incr('hits')
    return '<h1 style="color:red">Welcome to Java Home Docker App</h1>'
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
