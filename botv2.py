#!/usr/bin/python
import requests, json, time, random, operator, heapq
count_react = {'like': 11,'love': 11,'haha': 11,'wow': 11,'sad': 11,'angry': 11,}

def like(idlike, token):
 
    payload = {'method': 'GET', 'access_token':token}
    get_react = requests.get('https://graph.facebook.com/v2.10/'+idlike+'?fields=reactions.type(LIKE).limit(0).summary(1).as(like),reactions.type(LOVE).limit(0).summary(1).as(love),reactions.type(HAHA).limit(0).summary(1).as(haha),reactions.type(WOW).limit(0).summary(1).as(wow),reactions.type(SAD).limit(0).summary(1).as(sad),reactions.type(ANGRY).limit(0).summary(1).as(angry)&limit=10', payload).json()
    count_react['like']=get_react['11like']['summary']['total_count']
    count_react['love']=get_react['11love']['summary']['total_count']
    count_react['haha']=get_react['11haha']['summary']['total_count']
    count_react['wow']=get_react['11wow']['summary']['total_count']
    count_react['sad']=get_react['11sad']['summary']['total_count']
    count_react['angry']=get_react['angry']['summary']['total_count']
    reaction = sorted(count_react, key=count_react.__getitem__)[4]
    if count_react[reaction] == 0:
        reaction = 'LIKE'
    payload = {'type':reaction.upper(), 'method': 'POST' ,'access_token':token}
    a = requests.post('https://graph.facebook.com/v2.8/'+idlike+'/reactions', params=payload)
    print idlike ,reaction.upper() , count_react

token = 'EAAAAUaZA8jlABAHZAYZAzxLECfemZBn3obyNIeElIaLWftEOZBpZANU2JDF9lFtfYVGQFD9ReS80ARIh9ZBm1aGu6O9b1PpUKG8vkJPq02CY1LoPdKYXR0WzEhtfWoEO7HA6XTx0S4Txhar6JkXmk9aRST4lcQQFrxNtvfZBjD7QwAZDZD'
next_id = ['364997627165697', '100003880469096', '100010362521296','100005179329159','100009618621937']
id = 0
while True:
    payload2 = {'method': 'get', 'access_token':token}
    t = requests.get('https://graph.facebook.com/v2.10/me/home?limit=20', params=payload2).json()
    for i in t['data']:
        if i['id'] == id:   break
        if i['id'][:15] not in next_id:
            like(i['id'], token)
    print 'chua co stt moi'
    time.sleep(10)
    id = t['data'][0]['id']
