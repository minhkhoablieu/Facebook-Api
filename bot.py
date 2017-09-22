#!/usr/bin/python
import requests, json, time, random
def like(idlike, token):
    reaction_list =  ['LIKE', 'LOVE', 'WOW', 'HAHA', 'SAD', 'ANGRY']
    # ['LIKE', 'LOVE', 'WOW', 'HAHA', 'SAD', 'ANGRY']
    reaction = random.choice(reaction_list)
    payload = {'type':reaction, 'method': 'POST' ,'access_token':token}
    a = requests.post('https://graph.facebook.com/v2.8/'+idlike+'/reactions', params=payload)
    print reaction, idlike
token = ''

#364997627165697 J2team
#100003880469096 Manh Tuan
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
