import urllib.request
import urllib.parse #handles spaces etc
#Basic http requests <address><?><q=><var1=value><&><var2=J etcetc>
#google.com/search?q=python%20programming%20tutorials The %20 is basically the same as +

values = {'q': 'python programming tutorials'}

data = urllib.parse.urlencode(values) #this adds the + or %20 to the right areas
url = 'https://www.google.com/search?' + data
# data = data.encode('utf-8')

#This header changes the header to say that we are accessing this via a browser instead of via python.
headers = {'User-Agent' : "Mozilla/5.0 (X11; Linux i686)"} #dictionary with the user agent set to Mozilla
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
# req = urllib.request.urlopen("https://www.google.com")
# print(req.read())

inp = input("")