import Lambda.RunQuery as rq
import pytest

TEST_EVENT ={'Records': 
        [{'messageId': 'aea5e372-85a4-4836-a4e0-c969cadf1d64', 
        'receiptHandle': 'AQEBsHyK1pZQeMS+CoK3J+BWatKf6lbjPxI5tqkAtqycjfxrIvaXimLQPU1a80/AukvZFIR16O8Q71J8toUJzoPYWCEd/2GVxhSnJ6piOQWZPx8pKcbiwmNkM3meetgaA32na0Mvjgitc9vKP8DPmxAntYBKkIpFn3wbVtpufagN8uHXZe2LkDyrTO7KaZQ6lAlGOEb4/m2TbpMcZLum3PwgKQ9qul/Djvx02hmm7lNhae/h68NYkq8OadcMQrXr4Ahcn1aqENnPS6F2rThfe5pxi74ubMnfYNWm+iQb3qOXpZ/ZhVGcP8VszjOwQwWcMwJl+XXLxMp8kvemGoKpw5C/iwNStl/+my2vlCwQYVmCx5CaGZMtJEoVifxaUkvAIZaNRhDHhvkSmAfiSSh+YcDJMg==', 
        'body': 
            "{'location': '05401', 'distance': '100', 'test': True, 'email': 'dfelcan@gmail.com', 'type': 'dog'}", 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1613090964650', 'SenderId': 'AIDAY57NSPBJO2XNRNVNC', 'ApproximateFirstReceiveTimestamp': '1613090964653'}, 'messageAttributes': {}, 'md5OfBody': '8109b97f8d62f3e5d282f82524fc2cc2', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-2:614141687890:PetRadar_Query_Queue', 'awsRegion': 'us-east-2'}]}

def test_get_petFinderAPI_token():
    assert (len(rq.getToken()) > 0)

def test_parse_queue_event():
    query_dict = rq.parseQueueEvent(TEST_EVENT)
    assert ('type' in query_dict)
    print(query_dict)

def test_run_query():
    response_from_petfinder = rq.runQuery(TEST_EVENT,None)
    assert(len(response_from_petfinder) > 0)
    print(response_from_petfinder)