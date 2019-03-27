import requests
import os
from flask import Flask, request

server = Flask(__name__)

@server.route("/bot", methods=['POST'])
def getMessage():
    text = request.get_json()
    print(text)

def main():
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()