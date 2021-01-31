import httplib2

h = httplib2.Http(".cache")
h.add_credentials('user', 'pass')
r, content = h.request("https://journey-of-foobar-server.herokuapp.com",
  "PUT", body="This is text",
  headers={'content-type':'text/plain'} )
h.close()
print(r['status'])
print(r['content-type'])