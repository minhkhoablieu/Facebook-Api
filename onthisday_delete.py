import requests, json,time
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


sine_time = raw_input('Since: year-month-day: ')
until_time = raw_input('Until: year-month-day: ')

payload = {'method': 'get', 'since': sine_time, 'until': until_time, 'access_token':token}
your_id = requests.get('https://graph.facebook.com/v2.10/me/feed', params=payload).json()

while True:
    try:
        for i in your_id['data']:
            payload ={
                'method': 'DELETE',
                'access_token':token
            }
            delete = requests.post('https://graph.facebook.com/v2.10/'+i["id"] ,params=payload).json()
            try:
                print delete['error']['message'],' | ', i["id"], ' | ', i['created_time']
                
            except KeyError :
                print 'deleted',' | ', i["id"], ' | ', i['created_time']
        your_id = requests.get(your_id["paging"]["next"]).json()
                
    except KeyError:
        break
