from flask import Flask
from blueprints import *

app = Flask(__name__)
app.register_blueprint(trans_bp)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Welcome ~'



if __name__ =='__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)

