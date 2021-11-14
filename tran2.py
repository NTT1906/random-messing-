import requests
import json
url = 'https://www.bing.com/ttranslatev3'

post_header = {}
post_header['Host'] = 'www.bing.com'
post_header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
post_header['Accept'] = '*/*'
post_header['Accept-Language'] = 'en-US,en;q=0.5'
post_header['Accept-Encoding'] = 'gzip, deflate'
post_header['Referer'] = 'https://www.bing.com/'
post_header['Content-Type'] = 'application/x-www-form-urlencoded'
post_header['Connection'] = 'keep-alive'

parameters_payload = {'IG' : '839D27F8277F4AA3B0EDB83C255D0D70', 'IID' : 'translator.5033.3'}
data_payload = {'text':'Hello', 'fromLang':'en', 'to':'vi'}
resp = requests.post(url, headers=post_header, params=parameters_payload, data=data_payload)

print(resp.json()[0]["translations"][0]["text"])