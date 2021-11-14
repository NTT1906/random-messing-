from json import loads
from requests import get
request_result = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=en&tl=vi&q=Hello")
translated_text = loads(request_result.text)[0][0][0]
print(translated_text)