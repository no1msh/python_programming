url = 'https://docs.python.org/3/tutorial'
https = url[url.find('https'):url.find(':')]
print(https)
address = url[url.find('docs'):url.find('/3')]
print(address)
tuto = url[url.find('tutorial'):]
print(tuto)
