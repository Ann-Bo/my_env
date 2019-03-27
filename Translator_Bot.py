import requests

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]

        return last_update

    def translate(self, text):
        url = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20190326T205614Z.90fe981868ebe21d.07ae7a57abb1ff0f1f3912f6c5af593880090026&text={text}&lang=ru-en'
        translatedText = requests.get(url).json()['text'][0]
        return f'{text} -> {translatedText}'


greet_bot = BotHandler('882179046:AAGLbbPeIlEhHWI8oVKfrbSWpDWQ2yVfjy0')

def main():
    new_offset = None

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        translated_text = greet_bot.translate(last_chat_text)

        greet_bot.send_message(last_chat_id, translated_text)

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
