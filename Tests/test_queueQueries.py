import pytest
import Lambda.QueueQueries as qq

def test_successful_execution():
   return qq.queueQueries(False,False)