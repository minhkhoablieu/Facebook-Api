# -*- coding: utf-8 -*-
import requests, json, time, random, sys
####

token =''
count_stt= 0
list_id=[]
count_react = {'like': 0,'love': 0,'haha': 0,'wow': 0,'sad': 0,'angry': 0,}
payload = {'method': 'get', 'access_token':token}
t = requests.get('https://graph.facebook.com/v2.8/me/posts?limit=1000', payload).json()
while True:
    try:
        for i in t['data']:
            count_stt+=1
            list_id.append(i['id'])
        t=requests.get(t["paging"]["next"]).json()
    except KeyError:
        break
sys.stdout.write("Dang xu li: ")
sys.stdout.flush()
for idx, item in enumerate(list_id):
    try:
        payload = {'method': 'GET', 'access_token':token}
        get_react = requests.get('https://graph.facebook.com/v2.10/'+item+'?fields=reactions.type(LIKE).limit(0).summary(1).as(like),reactions.type(LOVE).limit(0).summary(1).as(love),reactions.type(HAHA).limit(0).summary(1).as(haha),reactions.type(WOW).limit(0).summary(1).as(wow),reactions.type(SAD).limit(0).summary(1).as(sad),reactions.type(ANGRY).limit(0).summary(1).as(angry)&limit=10', payload).json()
        count_react['like']+=get_react['like']['summary']['total_count']
        count_react['love']+=get_react['love']['summary']['total_count']
        count_react['haha']+=get_react['haha']['summary']['total_count']
        count_react['wow']+=get_react['wow']['summary']['total_count']
        count_react['sad']+=get_react['sad']['summary']['total_count']
        count_react['angry']+=get_react['angry']['summary']['total_count']
        msg = "stt %i of %i" % (idx, len(list_id))
        sys.stdout.write(msg + chr(8) * len(msg))
        sys.stdout.flush()
    except KeyError:
         break
sys.stdout.write("DONE" + " "*len(msg)+"\n")
sys.stdout.flush()
print 'like %d love %d haha %d wow %d sad %d angry %d' %( count_react['like'], count_react['love'], count_react['haha'], count_react['wow'], count_react['sad'], count_react['angry'])