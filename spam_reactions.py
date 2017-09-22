#!/usr/bin/python
import requests, json, time, random

def gettoken():
    username = raw_input('nhap username fb: ')
    password = raw_input('nhap password fb: ')
    payload = {'u': username, 'p': password}
    get_token = requests.get('http://gymtranhuynh-winazure.rhcloud.com/token.php', params=payload).json()
    token = get_token['access_token']
    return token;

question = raw_input('Ban da co token full quyen chua (Y or N) ')

if question.upper() == 'Y':
    token = raw_input('nhap token: ')
    
else:
    token = gettoken()
    print token

idfb = raw_input('Id fb nguoi ban muon bao:=> ' )
payload = {'method': 'get', 'access_token':token}
t = requests.get('https://graph.facebook.com/v2.10/'+idfb+'/feed', params=payload).json()
reaction_list =  ['LIKE', 'LOVE', 'WOW', 'HAHA', 'SAD', 'ANGRY']
all_id = []

while True:
    try:
        for i in t['data']:
            all_id.append(i['id'])
        t=requests.get(t["paging"]["next"]).json()
    except KeyError:
        break
    
for id in all_id:
   reaction = random.choice(reaction_list)
   payload = {'type':reaction, 'method': 'POST' ,'access_token':token}
   a = requests.post('https://graph.facebook.com/v2.8/'+id+'/reactions', params=payload)
   print reaction + ' ' + id 
   time.sleep(1)
