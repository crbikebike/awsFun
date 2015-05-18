__author__ = 'ChrisKristen'

import boto
from boto.s3.key import Key
import keyinfo
import requests


putMe = 'putme.txt'
conn = boto.connect_s3(keyinfo.akey(),keyinfo.skey(),is_secure = True)
appBucket = conn.get_bucket('crace-appstore')
filePut = file(putMe,mode='r')
k = Key(appBucket)

if __name__ == '__main__':
    k.key = putMe
    k.set_contents_from_file(filePut)
    #k.send_file(filePut,headers=None)
    listBucket = appBucket.list()
    for item in listBucket:
        print item