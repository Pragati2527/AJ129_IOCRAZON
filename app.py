from flask import Flask, render_template, request
#import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal
import uuid
import smtplib

from flask_cors import CORS, cross_origin
i=0
dynamodb = boto3.resource('dynamodb')
petrol_table = dynamodb.Table('petrol_data')


app = Flask(__name__)
CORS(app)

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


def sendEmail(email,date,am,tid,vid):
    rec_email =email
    sender_email = "piyushait12@gmail.com"
    password ="qazmlp10"
    message= " fuel - "+am+"\n"+"Date : -"+date+"\n"+"Transactio ID: "+tid+"\n"+"Vendor Id:"+vid

    m="""
    Subject: Fuel verification""" + message



    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail (sender_email, rec_email, m)
    print(" email.has been sent to" ,rec_email)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recieve_data",methods = ['POST'])
def recieve_data():
    # data = request.get_json()
    # print(data)
    date = request.values.get('date')
    entered_amount = request.values.get('entered_amount','0.0')
    tid_s=''
    v_id='Vendor 1'
    for i in range(0, 500, 1):
        tid = uuid.uuid4()
        tid = str(tid)
        tid_s = tid
        print(tid)
    res = petrol_table.put_item(
    Item={
            'Date': date,
            'TID': tid,
            'Quantity': Decimal(entered_amount),
            'VID':v_id,
            'Email': request.values.get("email")
            
        }
    )
    sendEmail(request.values.get("email"),date,entered_amount,tid_s,v_id)

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
    
                    
@app.route("/get",methods=["POST"])
def get1():

    r = petrol_table.scan()
    email = request.get_json().get("email")
    i=0
    response_s = []
    r=r["Items"]
    for x in r:
        if 'Email' in x:
               
            if x["Email"] == email:
                response_s.append( x)
                i = i+1
        
    return str(response_s)

    
# print(json_list)

if __name__ == "__main__":
    app.run(debug=True)
