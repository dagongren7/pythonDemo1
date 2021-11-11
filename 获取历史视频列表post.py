import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'accessToken': 'MC0yMTc3Ni02MTg4ZGY5ZTA4NDdh'
    }

url = 'http://120.204.204.58:48000/sgs-api/v1/video/history/list'

data = {
    "page" : 1,
    "pageSize" : 100
}
page_text = requests.post(url=url,headers=headers,data=data).text
print("page_text: "+ page_text)