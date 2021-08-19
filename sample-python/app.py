from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_k3d():
    return '<h1 align="center" style="font-family:sans-serif;font-size:200px;">Hello from K3D!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)