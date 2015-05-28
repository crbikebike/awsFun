__author__ = 'ChrisKristen'

import boto
from boto.s3.key import Key
import keyinfo

putMe = 'putme.txt'
putme2 = 'putme2.png'
putme3 = 'banana.xlsx'
s3conn = boto.connect_s3(keyinfo.akey(),keyinfo.skey(),is_secure = True)
appBucket = s3conn.get_bucket('crace-appstore')
filePut = open(putMe,mode='r')
filePut2 = open(putme2,mode='r')
filePut3 = open(putme3,mode='r')
k = Key(appBucket)

if __name__ == '__main__':
    k.key = putme2
    k.set_contents_from_file(filePut2)
    k.key = putMe
    k.set_contents_from_file(filePut)
    k.key = putme3
    k.set_contents_from_file(filePut3)

    listBucket = appBucket.list()
    print 'listing bucket items'
    for item in listBucket:
        m = Message()
        m.set_body(str(item))
        my_q.write(m)