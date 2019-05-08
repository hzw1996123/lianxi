import urllib.request
import urllib.parse
import json

content = input('输入需要翻译的内容：')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
'''
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
'''
date = {}

date['i'] = content
date['from'] = 'AUTO'
date['to'] = 'AUTO'
date['smartresult'] = 'dict'
date['client'] = 'fanyideskweb'
date['salt'] = '15565067028049'
date['sign'] = 'dfe68732193c5fa81b6b9c4912c887e2'
date['ts'] = '1556506702804'
date['bv'] = 'e2a78ed30c66e16a857c5b6486a1d326'
date['doctype'] = 'json'
date['version'] = '2.1'
date['keyfrom'] = 'fanyi.web'
date['action'] = 'FY_BY_CLICKBUTTION'

date = urllib.parse.urlencode(date).encode('utf-8')

req = urllib.request.Request(url,date)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0')
response = urllib.request.urlopen(req)

htlm = response.read().decode('utf-8')

target = json.loads(htlm)

print('翻译结果：%s' % (target['translateResult'][0][0]['tgt']))
