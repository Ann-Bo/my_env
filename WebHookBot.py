import requests
import os
from flask import Flask, request

server = Flask(__name__)
bot_token = os.environ['BOT_TOKEN']
yandex_key = os.environ['YANDEX_KEY']

@server.route("/bot", methods=['POST'])
def getMessage():
    message = request.get_json()['message']
    text = message['text']
    url = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={yandex_key}&text={text}&lang=en'
    translated_text = requests.get(url).json()['text'][0]

    params = {'chat_id': message['chat']['id'], 'text': f'{text} -> {translated_text}'}
    method = 'sendMessage'
    resp = requests.post(f'https://api.telegram.org/{bot_token}/{method}', params)
    print(resp)

    return 'ok'

def main():
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()