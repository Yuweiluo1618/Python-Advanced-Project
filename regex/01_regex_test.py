import re

result = re.match('ab','abc')
if result:
    print('match succesfully')
    print(result.start())
    print(result.end())
    print(result.group())

else:
    print('match fail')