import requests
import os
from flask import Flask, request

server = Flask(__name__)

@server.route("/bot", methods=['POST'])
def getMessage():
    text = request.get_json()['message']['text']
    url = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20190326T205614Z.90fe981868ebe21d.07ae7a57abb1ff0f1f3912f6c5af593880090026&text={text}&lang=en'
    translated_text = requests.get(url).json()['text'][0]
    print(translated_text)
    #f'{text} -> {translated_text}'

    return 'ok'

def main():
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()