__author__ = 'chris'

import boto
import boto.sqs
from boto.sqs.message import Message
from boto.s3.key import Key
import keyinfo



putMe = 'putme.txt'
putme2 = 'putme2.png'
putme3 = 'banana.xlsx'
s3conn = boto.connect_s3(keyinfo.akey(),keyinfo.skey(),is_secure = True)
sqsConn = boto.sqs.connect_to_region("us-west-2",
                                     aws_access_key_id = keyinfo.akey(),
                                     aws_secret_access_key = keyinfo.skey())
appBucket = s3conn.get_bucket('crace-appstore')
filePut = file(putMe,mode='rb')
filePut2 = file(putme2,mode='rb')
filePut3 = file(putme3,mode='rb')
k = Key(appBucket)
k2 = Key(appBucket)

if __name__ == '__main__':
    k2.key = putme2
    k2.set_contents_from_file(filePut2)
    k.key = putMe
    k.set_contents_from_file(filePut)
    k.key = putme3
    k.set_contents_from_file(filePut3)
    my_q = sqsConn.get_queue('cracequeque')

    listBucket = appBucket.list()
    print 'listing bucket items'
    for item in listBucket:
        m = Message()
        m.set_body(str(item))
        my_q.write(m)

    print 'listing queue'
    sqsResultSet = my_q.read(60)
    print sqsResultSet.get_body()
