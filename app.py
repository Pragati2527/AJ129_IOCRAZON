from flask import Flask, render_template, request
#import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
petrol_table = dynamodb.Table('Petrol_Pump_Table')

app = Flask(__name__)

# def float_range(start, stop, step):
#     while start < stop:
#         yield float(round(start,1))
#         start += float(step)
#     if start!=stop:
#         yield float(round(stop))

# n = float(input("Enter N : "))

# seq = list(float_range(0, n, 0.4))

# def json_data(i):
#     return json.dumps({'progress': i })

# json_list = list(map(json_data,seq))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recieve_data",methods = ['POST'])
def recieve_data():
    # data = request.get_json()
    # print(data)
    date = request.values.get('date')
    entered_amount = request.values.get('entered_amount','0.0')

    res = petrol_table.put_item(
    Item={
            'Date': date,
            'Quantity': Decimal(entered_amount)
        }
    )   

    print(date,entered_amount)
    
    return str(res),200
@app.route("/get_sum",methods=["POST"])
def get_sum():
     date = request.get_json()
     
     response = petrol_table.query(
        KeyConditionExpression=Key('Date').eq(date.get("date"))
     )
     res = response['Items']

     sum=0;
     for r in res:
         sum = sum+ r["Quantity"]

     
     return str(sum),200
    
                    

# print(json_list)

if __name__ == "__main__":
    app.run(debug=True)
