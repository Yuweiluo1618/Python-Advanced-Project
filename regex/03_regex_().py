import re

result = re.match('\w{4,12}@(gmail|yahoo|outlook)\.com$','hello@gmail.com')

if result:
    print('match success')
    print(result.group())
    print(result.group(1))

else:
    print('match fail')