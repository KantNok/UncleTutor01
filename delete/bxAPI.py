import requests  #not from flask but 'request' is from flask
import pprint

## ดึงราคาจาก Bx.in.th

def GetBxPrice():
    data = requests.get('https://bx.in.th/api/').json() #เพื่อให้เป็น type dict แปลงจาก string

    # pp = pprint.PrettyPrinter(indent=3)

    # pp.pprint(data)
    result = []  #สร้าง empty list
    for key in list(data.keys())[0:5]:
        prim_name = data[key]['primary_currency']
        sec_name = data[key]['secondary_currency']
        change = data[key]['change']
        last_price = data[key]['last_price']
        volume = data[key]['volume_24hours']
        price_data = {
            prim_name : prim_name,
            sec_name : sec_name,
            change : change,
            last_price : last_price,
            volume : volume ,
        }
        result.append(price_data)
        # print(prim_name , change , ' : ' , sec_name , ' : ', last_price , ' : ', change , ' : ', volume)
    return result


# if __name__ == '__main__':
#     print(GetBxPrice())