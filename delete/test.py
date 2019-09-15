import pprint
from flask import Flask , request  
#ถ้าคนละ Layer ==>> from folder-name.ชื่อFile เช่น resource.wolf  import ชื่อfunction

## from{ name of your file } import search  [ctrl kc  ,ctrl ku]
from wolf import search_wiki 

app = Flask(__name__)
access_token = 'bQ2oBx3p0GQEB0FkLr1aitV22EdUieOwFvs5RDTNJB9cYGc0/q9U2LYcFfhYHpLt6HCNUqFRtwBBTneG1GAQQjyVgaeCbs2wI3oopKazBGdVbnG3imnlH6CAM/eDvTuRppJ5IY8qvRPhPX3EdWSLggdB04t89/1O/w1cDnyilFU='

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':

        pp = pprint.PrettyPrinter(indent=3)
        ### dictionary from line
        data = request.json #type เป็น dictionary
        print(type(data))

        data_show = pp.pprint(data)

        ## extract text from line
        text_fromline = data['events'][0]['message']['text']
        ## ค้นหาคำจาก wikipedia
        result = search_wiki(text_fromline)

        ### import function ในการส่งmessage reply.py
        from reply import ReplyMessage

        ReplyMessage(Reply_token=data['events'][0]['replyToken'],
        TextMessage=result,
        Line_Acees_Token= access_token
        )


        return 'OK'

    elif request.method == 'GET':
        return 'นี้คือลิงค์เว็บสำหรับรับ package'

if __name__ == "__main__":
    app.run(port=200)