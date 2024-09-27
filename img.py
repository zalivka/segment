from flask import Flask, send_file, current_app

app = Flask(__name__)

@app.route('/')
def flask_logo():
    return "!!!!"
    # return current_app.send_static_file('mask_0.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0')