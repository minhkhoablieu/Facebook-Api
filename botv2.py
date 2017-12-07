#!/usr/bin/python
import requests, json, time, random, operator, heapq
count_react = {'LIKE': 0,'LOVE': 0,'HAHA': 0,'WOW': 0,'SAD': 0,'ANGRY': 0,}
react = ''
def like(idlike, token):
    time.sleep(2)
    payload = {'method': 'GET', 'access_token':token}
    get_react = requests.get('https://graph.facebook.com/v2.10/'+idlike+'?fields=reactions.type(LIKE).limit(0).summary(1).as(like),reactions.type(LOVE).limit(0).summary(1).as(love),reactions.type(HAHA).limit(0).summary(1).as(haha),reactions.type(WOW).limit(0).summary(1).as(wow),reactions.type(SAD).limit(0).summary(1).as(sad),reactions.type(ANGRY).limit(0).summary(1).as(angry)&limit=10', payload).json()
    count_react['LIKE']=get_react['like']['summary']['total_count']
    count_react['LOVE']=get_react['love']['summary']['total_count']
    count_react['HAHA']=get_react['haha']['summary']['total_count']
    count_react['WOW']=get_react['wow']['summary']['total_count']
    count_react['SAD']=get_react['sad']['summary']['total_count']
    count_react['ANGRY']=get_react['angry']['summary']['total_count']
    reaction = sorted(count_react, key=count_react.__getitem__)[4]
    reaction2 = sorted(count_react, key=count_react.__getitem__)[5]
    if count_react[reaction] != 0 and count_react[reaction2] != 0:
        if reaction == 'LIKE':
            react = reaction2
        else:
            react = reaction
    elif count_react[reaction] == 0 and count_react[reaction2] != 0:
        react = reaction2
    else:
        react = 'LOVE'
    payload = {'type':react.upper(), 'method': 'POST' ,'access_token':token}
    a = requests.post('https://graph.facebook.com/v2.8/'+idlike+'/reactions', params=payload)
    print '%-35s%-6s%-6s%-5i%-6s%-5s' % (idlike,react,reaction,count_react[reaction],reaction2,count_react[reaction2])
token = ''
next_id = ['364997627165697', '100003880469096', '100010362521296','100005179329159','100009618621937']
id = 0
while True:
    payload2 = {'method': 'get', 'access_token':token}
    t = requests.get('https://graph.facebook.com/v2.10/me/home?limit=20', params=payload2).json()
    for i in t['data']:
        if i['id'] == id:   break
        if i['id'][:15] not in next_id:
            payload = {'fields':'gender','method': 'POST' ,'access_token':token}
            a = requests.post('https://graph.facebook.com/v2.8/'+i['id'][:15], params=payload).json()
            try:
                if a['gender'] == 'famele':
                    next
                else:
                    like(i['id'], token)
            except KeyError:            
                like(i['id'], token)
    time.sleep(10)
    id = t['data'][0]['id']
