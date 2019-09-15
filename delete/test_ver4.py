import pprint
from flask import Flask ,request 
app = Flask(__name__)
from wolf

@app.route('/')
def hello_World():
    return 'Hello my tiny World'

@app.route('/webhook',methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        data = request.json
        data_show = pp.pprint(data)

        text_fromline = data['events'][0]['replytoker'],
        TextMessage=result,
        Line_Access_Token = 
        result = search(text_fromline)
        print(result)

        from reply import ReplyMessage
        ReplyMessage=result,
        Line_Access_Token='bQ2oBx3p0GQEB0FkLr1aitV22EdUieOwFvs5RDTNJB9cYGc0/q9U2LYcFfhYHpLt6HCNUqFRtwBBTneG1GAQQjyVgaeCbs2wI3oopKazBGdVbnG3imnlH6CAM/eDvTuRppJ5IY8qvRPhPX3EdWSLggdB04t89/1O/w1cDnyilFU=
')
        return 'OK'                     #requet.json,200
    elif request.method == 'GET':
         return 'This หน้าweb รับ Package'


if __name__ == "__main__":
    app.run(port=200)  #ตอนแรก ไม่ได้กำหนดport มันก็จะ default 5000 ก็จะ Verify ไม่ได้

