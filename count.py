import requests,time
#add your toke here 
token = ''

payload = {'method': 'GET','fields': 'message_count,senders,thread_key', 'access_token':token}
t = requests.get('https://graph.facebook.com/v2.10/me/conversations', params=payload).json()

data = {}
data['data'] = []
while True:
    try:
        for i in t['data']:
            if i["thread_key"][0:5] == "t_100":
                name = i["senders"]["data"][0]['name']
                number_count = i['message_count']
                name_and_count = {'name': name, 'number_count': number_count}
                data['data'].append(name_and_count)
        t=requests.get(t["paging"]["next"]).json()
    except KeyError:
         break

data = sorted(data['data'], key=lambda k: k['number_count'], reverse=True)
print 'top 20'
i = 0
while i < 20:
    print '%s => %u mess' %(data[i]['name'], data[i]['number_count'])
    i +=1
    
