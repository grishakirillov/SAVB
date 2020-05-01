import vk_api
from flask import Flask, request, json
import os

token = "56afa7c01cb0587b3b7dd76bbf91e52b12d122a34274aada6b622bfe8e9c0392be2e5563213b07997d2cf"
vk = vk_api.VkApi(token = token)
vk._auth_token()
confirmation_token = "360edd42"
app = Flask(__name__)
vk = vk.get_api()

@app.route('/messages', methods=['POST'])
def messages():
    data = json.loads(request.data)
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v=5.0)
        user_id = data['object']['user_id']
        api.messages.send(access_token=token, user_id=str(user_id), message='Привет, я новый бот!')
        return 'ok'

@app.route('/', methods=['GET'])
def home():
    return "Hello stupid!"


if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))