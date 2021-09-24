import json
import boto3
from botocore.exceptions import ClientError
import datetime

def handler(event, context):
    print('hello')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('visitor-counter2')
    today = str(datetime.datetime.today().strftime('%d%m%Y'))
    print('today', today)
    update = table.get_item(
        Key={
            'date': today
        }
    )
    if 'Item' in update:
        updateday = update['Item']['count'] + 1
        dbResponse = table.put_item(
        Item = {
            'date':today,
            'count':updateday,
        }
    )      
    else:
        dbResponse = table.put_item(
        Item = {
            'date':today,
            'count':1,
        }
    ) 
    resp = table.scan(AttributesToGet=['count']) 
    print('resp', resp)
    length = len(resp['Items']) 
    total = 0
    print('length of list', length)
    for i in range(length):
        total += resp['Items'][i]['count']
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS, POST, GET"
        },
        "body": total
    }
    print('apiresponse', apiResponse)
    return apiResponse