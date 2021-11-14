import requests
import urllib.parse
import urllib3
class Translator:
	def __init__(self):
		pass
		
	def uc(self, string):
		urllib3.disable_warnings()
		return urllib.parse.quote(string)
	
	def translate(self, source, target, text):
		url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
		payload = "sl" + self.uc(source) + "&tl" + self.uc(target) + "&q" + self.uc(text)
		hdr = {
			"Content-Type": "application/x-www-form-urlencoded",
			'User-Agent': 'AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1',
			#'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Connection': 'keep-alive'
		}
		
		response = requests.post(url, data=payload, headers = hdr, verify = False)
		return response

a = Translator()
print(a.translate("en", "vi", "This is a hello"))