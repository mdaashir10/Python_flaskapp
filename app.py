from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps! CI/CD is working"

@app.route('/health')
def health():
    return {"status": "healthy", "message": "App is running"}, 200

@app.route('/info')
def info():
    return {
        "app": "Flask DevOps App",
        "version": "1.0",
        "author": "mdaashir10",
        "endpoints": ["/", "/health", "/info"]
    }, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
