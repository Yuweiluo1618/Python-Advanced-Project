import re

result = re.search('src="(.+?)"', 'tm="gg" src="www.google.com" img = "kkkk"')
if result:
    print("match success")
    print(result.group())
    print(result.group(1))

else:
    print('match fail')