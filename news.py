from newsapi import NewsApiClient
from igpls import news_key
import http.client, urllib.parse
import json

conn = http.client.HTTPSConnection('api.thenewsapi.com')

params = urllib.parse.urlencode({
    'api_token': news_key,
    'categories': 'business',
    'search': 'microsoft',
    'limit': 3,
    'language': 'en'
    })

conn.request('GET', '/v1/news/all?{}'.format(params))

res = conn.getresponse()
data = res.read()
news = data.decode('utf-8')
temp = json.loads(news)
sources = temp['data']

for i in sources:
    print(i['title'])