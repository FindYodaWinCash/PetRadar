import boto3
from boto3.dynamodb.conditions import Key, Attr

QUERY_TABLE_NAME='PetRadar_Queries'
QUEUE_URL = 'https://sqs.us-east-2.amazonaws.com/614141687890/PetRadar_Query_Queue'

def queueQueries(event,context):
    table = boto3.resource('dynamodb').Table(QUERY_TABLE_NAME)
    sqs = boto3.client('sqs')

    response = None
    if 'test' in event:
        response = table.scan(FilterExpression=Attr('test').exists())
    else:
        response = table.scan(FilterExpression=Attr('test').not_exists())

    for item in response['Items']:
        sqs.send_message(QueueUrl=QUEUE_URL,MessageBody=str(item))

    return response['Count']
