from flask import Flask, request, jsonify
from flask_cors import CORS
import telepot
import dotenv

env = dotenv.dotenv_values(".env")

bot = telepot.Bot(env['telegram_token'])

app = Flask(__name__)
CORS(app)

data = {
    '01': [],
    '25': [],
    '10': [],
    'te': [],
    'labels': []
}

@app.route("/datos",methods=["POST"])
def send_data():
    req = request.get_json()
    data['01'].append(req['01'])
    data['25'].append(req['25'])
    data['10'].append(req['10'])
    data['te'].append(req['te'])
    return jsonify(req)

@app.route("/get-data", methods=["GET"])
def get_data():
    data['labels'] = [e for e in range(len(data['01']))]
    return jsonify(data)

@app.route("/send-image", methods=["POST"])
def send_image():
    file = request.files.get('file')
    bot.sendPhoto(env['telegram_user_id'],photo=file)
    response = jsonify("Hola")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True, port=8000)