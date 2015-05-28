__author__ = 'chris'

import boto
import boto.sqs
from boto.sqs.message import Message
import keyinfo


sqsConn = boto.sqs.connect_to_region("us-west-2",
                                     aws_access_key_id = keyinfo.akey(),
                                     aws_secret_access_key = keyinfo.skey())

def countRS(queueRS):
    i = 0
    for message in queueRS:
        i += 1
    return i

def printbodies(queueRS):
    for message in queueRS:
        print (message.get_body())

if __name__ == '__main__':
    my_q = sqsConn.get_queue('cracequeque')

    print ('listing queue')

    sqsResultSet = my_q.get_messages(visibility_timeout=10)
    print ('queue is this big: {0}'.format(str(countRS(sqsResultSet))))
    printbodies(sqsResultSet)
