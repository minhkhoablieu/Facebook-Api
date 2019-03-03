import requests, json,time
token = ""
your_id_fb = ""
payload = {'method': 'get', 'access_token':token}
your_id = requests.get('https://graph.facebook.com/v2.10/'+your_id_fb+'/feed', params=payload).json()

while True:
	try:
		for i in your_id['data']:
			
			payload ={
				'method': 'DELETE',
				'access_token':token
			}
			delete = requests.post('https://graph.facebook.com/v2.10/'+i["id"] ,params=payload).json()
			
			if(delete.has_key('error')):
				print i['id'] + '  : khong xoa duoc'
				
			else:
				print i['id'] + '  : da xoa' 
				

			print("------------")	
		your_id = requests.get(your_id["paging"]["next"]).json()
				
	except KeyError:
		break
