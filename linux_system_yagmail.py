import yagmail

#user = email sender

ya_obj = yagmail.SMTP(user='', password='')
content = 'hello world'
ya_obj.send('', "ygmail test", content)


