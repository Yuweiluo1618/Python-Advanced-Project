import re

#result = re.search('\d+', 'view: 6666')
#result = re.findall('\d+', 'view: 6666, read: 8888, write: 99999')
#result = re.sub('\d+', '100000', 'view: 6666, read: 8888, write: 99999')
result = re.split(':| ', 'view:6666 read:8888 write:99999')
if result:
    #print(result.group())
    print(result)

else:
    print('match fail')