import urllib.request
import urllib.parse #handles spaces etc
#Basic http requests <address><?><q=><var1=value><&><var2=J etcetc>
#google.com/search?q=python%20programming%20tutorials The %20 is basically the same as +
url = 'https://www.google.com/search'
values = {'q': 'python programming tutorials'}

data = urllib.parse.urlencode(values) #this adds the + or %20 to the right areas
data = data.encode('utf-8')

req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
# req = urllib.request.urlopen("https://www.google.com")
# print(req.read())

inp = input("")