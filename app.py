from flask import Flask
import redis
import os
import socket

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_client = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    redis_client.incr('hits')
    hit_count = redis_client.get('hits').decode('utf-8')
    hostname = socket.gethostname()
    
    secret_message = os.getenv('SECRET_MESSAGE', 'No secret found')
    feature_flag = os.getenv('FEATURE_FLAG', 'off')
    
    return f"""
    <h1>Welcome to the Interesting K8s App!</h1>
    <p>You're visitor number: <strong>{hit_count}</strong></p>
    <p>Hostname: {hostname}</p>
    <p>Secret Message: {secret_message}</p>
    <p>Feature Flag Status: {feature_flag}</p>
    <p>Debug Info: {os.environ.get('DEBUG_INFO', '')}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)