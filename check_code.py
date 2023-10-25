import httplib2
url = "http://"+input("Input URL: ")
ht = httplib2.Http()
# This will return a dictionary of values. We want the ‘status’.
resp = ht.request(url, 'HEAD')
# Test if http response code is 200.
if int(resp[0]['status'])  == 200:
    print("Response Code: "+resp[0]['status'])
    print("Website is up.")
else:
    print("Response Code: "+resp[0]['status'])
    print("Website is down.")