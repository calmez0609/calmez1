from flask import Flask, request, abort
import random
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('x9I42/HXzVLQQ3HLWVmxCf7z5jLAtEf44gpdKmlnGCkzXw9+y+LuKjA8WIklR29p4cXtdgCmV1CCD3woIswyRrOkphjpeubSVLIgWlBtMnI4mcAWYjkHuV48A4C9q3JIhV8GauV4tRmfKDmmZwwSoQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('3d7644d429a491ed618d3b2b2fec3b2d') 
#監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def Reply(text):
    list=['畜生','王八蛋','龜孫']
    if text='隆基是':
     text=random.choice(list)
        return text
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text= Reply(event.message.text))
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
