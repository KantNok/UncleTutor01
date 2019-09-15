#ส่ง message ไปให้ line user
#Copy from : https://github.com/line/line-bot-sdk-python/blob/master/examples/flask-echo/app_with_handler.py
#ตัวนี้เป็น File starter
import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
####(    MessageEvent, TextMessage, TextSendMessage)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = 'e9300087d149c94cb509ff65b7e3dd33' ##get from line console
channel_access_token = 'bQ2oBx3p0GQEB0FkLr1aitV22EdUieOwFvs5RDTNJB9cYGc0/q9U2LYcFfhYHpLt6HCNUqFRtwBBTneG1GAQQjyVgaeCbs2wI3oopKazBGdVbnG3imnlH6CAM/eDvTuRppJ5IY8qvRPhPX3EdWSLggdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)  #ตัวส่ง api 
handler = WebhookHandler(channel_secret)

###แก้ route +channel-secret +access-toker 
@app.route("/webhook", methods=['POST']) ###old code ==> ("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature'] #บ่งบอกว่า มาจาก line จริงป่ะ 

    # get request body as text
    body = request.get_data(as_text=True)       
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)  #body ที่ line ส่งมา เราจะสร้าง specialist ให้รู้ว่ามันเป็น text,audio,sticker หรืออะไร
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent,message=TextMessage)
def message_text(event):    #event คือได้กลับมาจาก handler
    ## Function reply_token 

    print(event.reply_token)
    print(event.message.text)

#    line_bot_api.reply_message(
#        event.reply_token,                          #ได้ reply token กลับมา 
#        TextSendMessage(text=event.message.text)    #ส่ง message กลับไป >>เข้าถึง text เลย 
#    )
    Reply_token = event.reply_token     ##Reply token
    text_fromUser = event.message.text  ##ข้อความจาก user 

    text_tosend1 = TextSendMessage(text='ต่อไปนี้นะ',quick_reply=None) ##ส่ง text ตรงๆ ไม่ได้ ต้องเป็น json จะได้ส่งต่อได้
    text_tosend2 = TextSendMessage(text='จะไม่ยุ่งเลย',quick_reply=None) 

    image_message1 = ImageSendMessage(
        original_content_url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fanimal.catdumb.com%2Fwp-content%2Fuploads%2F2019%2F09%2F6-31.jpg&imgrefurl=https%3A%2F%2Fanimal.catdumb.com%2Fthe-cat-nung-vurr-nom-777%2F&docid=6sO5lkCH-rToZM&tbnid=rfxtfumgDFQkdM%3A&vet=10ahUKEwj51M2hgdLkAhULso8KHeVlD-UQMwhDKAUwBQ..i&w=720&h=960&bih=569&biw=860&q=%E0%B8%A7%E0%B8%B1%E0%B8%A7%E0%B8%99%E0%B8%A1&ved=0ahUKEwj51M2hgdLkAhULso8KHeVlD-UQMwhDKAUwBQ&iact=mrc&uact=8'
       ,preview_image_url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fanimal.catdumb.com%2Fwp-content%2Fuploads%2F2019%2F09%2F6-31.jpg&imgrefurl=https%3A%2F%2Fanimal.catdumb.com%2Fthe-cat-nung-vurr-nom-777%2F&docid=6sO5lkCH-rToZM&tbnid=rfxtfumgDFQkdM%3A&vet=10ahUKEwj51M2hgdLkAhULso8KHeVlD-UQMwhDKAUwBQ..i&w=720&h=960&bih=569&biw=860&q=%E0%B8%A7%E0%B8%B1%E0%B8%A7%E0%B8%99%E0%B8%A1&ved=0ahUKEwj51M2hgdLkAhULso8KHeVlD-UQMwhDKAUwBQ&iact=mrc&uact=8' 
        )

    line_bot_api.reply_message(
        Reply_token ,
        messages = [text_tosend1,text_tosend2] ###ส่งได้มาสุด 5 ข้อความ 
    )

 #   line_bot_api.push_message(
 #       to='' ##เอามาจากfirebird ที่แอบเก็บไว้
 #       #messages=[text_tosend1,text_tosend2,image_message1]  แบบนี้ไม่ได้ 
 #   )


if __name__ == "__main__":
    app.run(port=200)

