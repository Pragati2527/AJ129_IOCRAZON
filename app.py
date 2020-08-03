from flask import Flask, render_template, request
#import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal
import uuid
import smtplib
import mysql.connector

from flask_cors import CORS, cross_origin


i=0
dynamodb = boto3.resource('dynamodb')
petrol_table = dynamodb.Table('Petrol_Pump')

mydb = mysql.connector.connect(
   host='127.0.0.1', user='root', password='', database='petrol')
mycursor = mydb.cursor()



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
    mydb = mysql.connector.connect(
        host='127.0.0.1', user='root', password='', database='petrol')
    mycursor = mydb.cursor()
    insert_stmt = (
        "INSERT INTO petrol_data(date, tid, vid, amount, email)"
        "VALUES (%s, %s, %s, %s, %s)"
        )
    data = ( date, tid, v_id, Decimal(entered_amount), request.values.get("email"))
    mycursor.execute(insert_stmt, data)
    mydb.commit()
        
    sendEmail(request.values.get("email"),date,entered_amount,tid_s,v_id)

    print(date,entered_amount)
    
    return str(res),200
#==========================================================================




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
#==================================================================================================

@app.route("/local",methods=["POST"])
def local():
    email = request.get_json().get("email")
    query= "SELECT * FROM petrol_data WHERE email = '"+email+"'"
    mydb = mysql.connector.connect(
        host='127.0.0.1', user='root', password='', database='petrol')
    mycursor = mydb.cursor()
    r= mycursor.execute(query)
  ##  sql_select_query = "SELECT * FROM petrol_data WHERE email = 'amirraaj0@gmail.com' "
    ##mycursor.execute(sql_select_query, (email,))
    record = mycursor.fetchall()
    print(record)

    i=0
    response_s = []
   
    for x in record:
        response_s.append({
            "date":x[0],
            "tid":x[1],
            "vid":x[2],
            "amount":x[3],
            "email":x[4]})
        
    return str(response_s)






    


if __name__ == "__main__":
    app.run(debug=True)
