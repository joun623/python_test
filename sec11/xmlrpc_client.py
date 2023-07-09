import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
num = 7
result = proxy.double_test(num)
print("Double %s is %s" % (num, result))
