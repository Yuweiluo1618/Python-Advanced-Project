import re

result = re.match('<(?P<name1>[a-zA-Z0-9>]+)><(?P<name2>[a-zA-Z0-9>]+).*</(?P=name2)></(?P=name1)>','<html><h1>test</h1></html>')
if result:
    print('match success')
    print(result.group())

else:
    print('match fail')