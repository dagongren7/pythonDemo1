import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'accessToken': 'MC0yMTc3Ni02MTg4ZGY5ZTA4NDdh'
    }
url = 'http://120.204.204.58:48000/sgs-api/v1/cusmap/location/find?userIds=21275,21276'
page_text = requests.get(url=url,headers=headers).text
print("page_text: "+ page_text)