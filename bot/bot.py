import vk_api
from flask import Flask, request, json
import os

token = "56afa7c01cb0587b3b7dd76bbf91e52b12d122a34274aada6b622bfe8e9c0392be2e5563213b07997d2cf"
vk = vk_api.VkApi(token = token)

confirmation_token = "360edd42"
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "ok"


@app.route('/', methods=['POST'])
def messages():
    data = json.loads(request.data)
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        id = data['object']['message']['from_id']
        body = data['object']['message']['text']
        vk.method("messages.send", {"peer_id": id, "message": body, "random_id": 0})
        return 'ok'
    else:
        return 'ok'

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))