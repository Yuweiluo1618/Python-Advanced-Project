import re

result = re.match('^[0-9]?[0-9]$|^100$','100')

if result:
    print(result.group())

else:
    print('match fail')