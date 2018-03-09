import time
import vk_api
import requests
import sys
import weather as weat

vk = vk_api.VkApi(token = 'f53b3ee4912a5b03eb33589f74e9e979bc40fd532d527967c5fe3cbdd7a52620ab8c515983f6350ae9bfc')
values = {'out': 0,'count': 100,'time_offset': 10}

upload = vk_api.VkUpload(vk)
photo  = upload.photo_messages('D:\Bot-Weather\weather.jpg')
vk_photo_url = 'https://vk.com/photo{}_{}'.format(
        photo[0]['owner_id'], photo[0]['id']
        )
a = vk_photo_url[15:-1]
b, c = a.split('-')
result = b + c


def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id, 'attachment':'photo299887547_456242309', 'message':s})

while True:
	response = vk.method('messages.get', values)
	if response['items']:
		values['last_message_id'] = response['items'][0]['id']
		msg = response['items'][0]['body'].lower()
		weathermsg = {"погода", "gjujlf"}
		weathermsg2 = {"погода на завтра", "gjujlf yf pfdnhf"}
		weat.main()
		if msg in weathermsg:
			for item in response['items']:
				write_msg(item[u'user_id'], weat.pogoda1)
		elif msg in weathermsg2:
			for item in response['items']:
				write_msg(item[u'user_id'], weat.pogoda2)
	time.sleep(1) 

