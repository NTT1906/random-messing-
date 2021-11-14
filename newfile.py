import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = "q=Hello%2C%20world!&source=en&target=vi"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/json",
    'x-rapidapi-key': "f786aa0d34msh47a274d82982f42p12266bjsn4d1b640621f8",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

response.text