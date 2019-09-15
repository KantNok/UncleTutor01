#เช็คราคาจาก bX bitCoin
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
from linebot.models import *    ####(    MessageEvent, TextMessage, TextSendMessage)

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


    Reply_token = event.reply_token     ##Reply token
    text_fromUser = event.message.text  ##ข้อความจาก user 

    if 'เช็คราคา' in text_fromUser:
        ##from Resource.bxAPI import GetBxPrice
        from bxAPI import GetBxPrice
        
        from random import randint
        num  = randint(1,10)
        data = GetBxPrice(num)  #เก็บ จำนวนข้อมูล ที่จะ display
        
        from flexmessage import setbubble , setCarousel 

        flex = setCarousel(data)  #type dictionary ครือออ flex ที่มี carousel=1 /bubble=5

        from reply import SetMenuMessage_Object ,send_flex

        flex = SetMenuMessage_Object(flex)
        send_flex(Reply_token ,file_data = flex ,bot_access_key = channel_access_token)

    else:
        text_list = [
            'ฉันไม่เข้าใจที่คุณพูดค่ะ กรุณาลองถามใหม่ค่ะ',
            'ไม่เข้าใจจริงๆๆๆ ลองใหม่นะ',
            'ขอโทษอ่ะ โทรคุยละกัน งงจริงๆ'
        ]

        from random import choice

        text_data = choice(text_list)

        text = TextSendMessage(text=text_data)

        line_bot_api.reply_message(Reply_token,text)




@handler.add(FollowEvent)
def RegisRichmenu(event):
    userid  = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name

    button1 = QuickReplyButton(action=MessageAction(label='เช็คราคา',text='เช็คราคา'))
    button2 = QuickReplyButton(action=MessageAction(label='เช็คข่าวสาร',text='เช็คข่าวสาร'))
    qbtn = QuickReply(items={button1,button2})
    #text message object
    text = TextSendMessage(text='ยินดีที่ได้รู้จัก {} แชทบอทเอง'.format(disname))
    text2 = TextSendMessage(text='กรุณาเลือกเมนูที่ท่านต้องการ ',quick_reply=qbtn )
    ### link richmenu
    line_bot_api.link_rich_menu_to_user(userid,'richmenu-422bbc07f5bf346303652863de5d0d5d') #*********>>>>>>เอา result จากการ run richmenu.py 
    #####reply message wien user follow 
    line_bot_api.reply_message(event.reply_token,messages={text,text2})

if __name__ == "__main__":
   app.run(port=200)

