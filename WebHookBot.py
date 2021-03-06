import requests
import os
from flask import Flask, request

server = Flask(__name__)
bot_token = os.environ['BOT_TOKEN']
yandex_key = os.environ['YANDEX_KEY']

@server.route("/bot", methods=['POST'])
def getMessage():
    message = request.get_json()['message']
    text_to_translate = message['text']
    url = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={yandex_key}&text={text_to_translate}&lang=en'
    translated_text = requests.get(url).json()['text'][0]

    body_data = {'chat_id': message['chat']['id'], 'text': f'{text_to_translate} -> {translated_text}'}
    requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage', body_data)

    return 'ok'

def main():
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()