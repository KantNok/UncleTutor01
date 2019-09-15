from flask import Flask ,request 
app = Flask(__name__)

@app.route('/')
def hello_World():
    return 'Hello my tiny World'

@app.route('/webhook',methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'OK'                     #requet.json,200
    elif request.method == 'GET':
         return 'This หน้าweb รับ Package'


if __name__ == "__main__":
    app.run()

