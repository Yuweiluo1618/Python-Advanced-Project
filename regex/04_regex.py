import re

result = re.match('<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\\2></\\1>','<html><h1>test</h1></html>')
if result:
    print('match success')
    print(result.group())

else:
    print('match fail')