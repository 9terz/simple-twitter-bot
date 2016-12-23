#coding=utf-8
import tweepy, re, time, ConfigParser
from urllib import urlopen
from bs4 import BeautifulSoup

import re, urlparse

config = ConfigParser.ConfigParser()
config.read('.twitter')

consumer_key = config.get('apikey', 'key')
consumer_secret = config.get('apikey', 'secret')
access_token = config.get('token', 'token')
access_token_secret = config.get('token', 'secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while(1):
    optionsUrl = 'https://www3.reg.cmu.ac.th/transcript/'
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage,"html.parser")
    current_date = time.strftime("%a %d %b %H:%M")
    strtodel = ["]","</p>"]
    wordtosay = str(soup.find_all('p',{'id':'update-at'},'.'))[51:].translate(None,"".join(strtodel)).decode('unicode-escape')
 
    word = wordtosay.encode('utf-8')
    words = "ขณะนี้เวลา " + current_date + " ในเวปดูเกรดขึ้นว่า  "+word +" ดูได้ที่ https://www3.reg.cmu.ac.th/transcript/"
    print len(words)
    api.update_status(status=words)
    print word
    time.sleep(444)
#api.update_status(status=urlEncodeNonAscii(cname))
#print cname