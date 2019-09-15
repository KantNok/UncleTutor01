import pprint
from flask import Flask ,request 
app = Flask(__name__)

@app.route('/')
def hello_World():
    return 'Hello my tiny World'

@app.route('/webhook',methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        pp = pprint.PrettyPrinter(indent=3)
        pp.pprint(request.json)
        return 'OK'                     #requet.json,200
    elif request.method == 'GET':
         return 'This หน้าweb รับ Package'


if __name__ == "__main__":
    app.run(port=200)  #ตอนแรก ไม่ได้กำหนดport มันก็จะ default 5000 ก็จะ Verify ไม่ได้

