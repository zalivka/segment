from flask import Flask, request, render_template
from cut2 import click_handler_bp

app = Flask(__name__)
app.register_blueprint(click_handler_bp)

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/get-coordinates', methods=['GET'])
# def get_coordinates():
#     x = request.args.get('x')
#     y = request.args.get('y')
#     print(f'Clicked coordinates: x={x}, y={y}')
#     return 'Coordinates received'

if __name__ == '__main__':
    app.run()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')