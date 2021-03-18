import httplib


connect = httplib.HTTPConnection("192.168.1.1", 80, timeout=10)
print connect
