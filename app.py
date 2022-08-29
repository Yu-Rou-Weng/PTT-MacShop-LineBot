from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from linebot import LineBotApi


#======這裡是呼叫的檔案內容=====
from crawler import *
from custom import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

#搭配PTT-Macshop-Bot(熊大頭像)，Webhook URL https://oreo-linebot.herokuapp.com/callback (heroku為oreo-linebot)

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# My Channel Access Token
line_bot_api = LineBotApi('m6OLMV6UtVgbnoAV41nGeApiWsJmxrbqrSdQ/mpTteIp+PTKC56dR5ownF8YldyTHvFBzLRFNsc8wbQEZwqag6wa5Bos569qZRmTha9/yMOJfexY3PnhvmMpb1oGpx1wXAfUMlf1TAIAZQoa9aXyXwdB04t89/1O/w1cDnyilFU=')
# My Channel Secret
handler = WebhookHandler('273912ec03ee20ffa23d6009955f6e29')


# 監聽所有來自 /callback 的 Post Request
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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    
    if 'AirPods' in msg:
        message = TextSendMessage(text= ptt_alert(msg))
        line_bot_api.reply_message(event.reply_token, message)
        
    elif 'MacBook' in msg:
        message = TextSendMessage(text=ptt_alert(msg))
        line_bot_api.reply_message(event.reply_token, message)
        
    elif 'iPhone' in msg:
        message = TextSendMessage(text=ptt_alert(msg))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'iPad' in msg:
        message = TextSendMessage(text=ptt_alert(msg))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Pencil' in msg:
        message = TextSendMessage(text=ptt_alert(msg))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Watch' in msg:
        message = TextSendMessage(text=ptt_alert(msg))
        line_bot_api.reply_message(event.reply_token, message)  
    elif 'iMac' in msg:
        message = TextSendMessage(text=ptt_alert(msg))
        line_bot_api.reply_message(event.reply_token, message)

    elif 'help' in msg:
        message = TextSendMessage(text=custom())
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Help' in msg:
        message = TextSendMessage(text=custom())
        line_bot_api.reply_message(event.reply_token, message)
    elif 'HELP' in msg:
        message = TextSendMessage(text=custom())
        line_bot_api.reply_message(event.reply_token, message)                             
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    