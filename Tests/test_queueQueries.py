import pytest
import boto3
import time
import Lambda.QueueQueries as qq

TEST_JSON = {"test" : True}
NUM_TEST_QUERIES = 2


def test_retrieve_queries():
   assert(qq.queueQueries(TEST_JSON,None) == NUM_TEST_QUERIES)

def test_wrote_to_queue():
   sqs = boto3.client('sqs')
   # time.sleep(5) #wait for it to appear on the queue.
   # response = sqs.get_queue_attributes(QueueUrl= qq.QUEUE_URL, AttributeNames=['ApproximateNumberOfMessages'])
   # assert int(response['Attributes']['ApproximateNumberOfMessages']) == NUM_TEST_QUERIES
  