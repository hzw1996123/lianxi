import urllib.request

url = 'http://45.32.164.128/ip.php'

proxy_support = urllib.request.ProxyHandler({'http':'61.142.176.17:8082'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
