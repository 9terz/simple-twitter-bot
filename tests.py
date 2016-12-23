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
    strtodel2 = ["<strong>","</strong>"]
    wordtosay = str(soup.find_all('p',{'id':'update-at'},'.'))[51:].translate(None,"".join(strtodel)).decode('unicode-escape')
    word = wordtosay.encode('utf-8')
    words = current_date + " ในเวปดูเกรดขึ้นว่า  "+word +" ดูได้ที่ https://www3.reg.cmu.ac.th/transcript/"
    onlineuser = str(soup.find_all('div',{'id':'useronline'},'.'))[22:-7].translate(None,"".join(strtodel2)).decode('unicode-escape')
    online = onlineuser.encode('utf-8')
    if(word == 'ข้อมูลอัพเดทเมื่อวันที่ 23 ธันวาคม 2559'):
    	api.update_status(status='เฮ้ย อัพเดทวันที่ 23 เกรดออกแล้วปะวะสาสสสสสส ไปเช็คดิ๊ https://www3.reg.cmu.ac.th/transcript/')
    elif(word == 'ข้อมูลอัพเดทเมื่อวันที่ 24 ธันวาคม 2559'):
    	api.update_status(status='เฮ้ย อัพเดทวันที่ 24 เกรดออกแล้วปะวะสาสสสสสส ไปเช็คดิ๊ https://www3.reg.cmu.ac.th/transcript/')
    else:
    	tweet = online + ' แต่เกรดยังม่ายออก'
    	api.update_status(status=tweet)
    print word
    print online
    time.sleep(444)
#api.update_status(status=urlEncodeNonAscii(cname))
#print cname