import sys
import os
import requests
import time
import threading
import random
import json
import string

def InstaEmail(email):
 while True:
  try:
   head={
    "content-type":"application/x-www-form-urlencoded",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 jr/537.36",
    "x-csrftoken":"IoOjlJgt3Xstc4rESmEbrxfT2KmOdiry",
    "x-ig-app-id":"936619743392459",
    "x-ig-www-claim":"0",
    "x-instagram-ajax":"0737da2dc667",
    "x-requested-with":"XMLHttpRequest",
    "Pragma":"no-cache",
    "Accept":"*/*",
    "origin":"https://www.instagram.com",
    "referer":"https://www.instagram.com/accounts/password/reset/",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
   }
   data={
    'email_or_username':str(email),
    'recaptcha_challenge_field':'',
   }
   time.sleep(1)
   tt='http://%s' % (random.sample(listaprx,1)[0])
   proxies ={'https':tt}
   response=requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/',headers=head,data=data,proxies=proxies).json()
   if response['status']=='ok':
     print('[----------------------------------------------]\n [jr] Proxy : '+tt+'\n [jr] Status : Valid\n [jr] Number : '+email+'\n [jr] Status : Valid')
     f = open("Valid.txt", "a+")
     f.write(str(email)+'\n')
     f.close()
   else:
    print('[----------------------------------------------]\n [jr] Proxy : '+tt+'\n [jr] Proxy Status : Valid\n [jr] Number : '+email+'\n [jr] Status : Invalid')
  except Exception as exx:
   continue
  break
txt = input('[?] Phone Number List: ')
filep = input('[?] Proxies List (http ONLY): ')
Threads='1'
with open(filep) as fileprx:
  listaprx = fileprx.read().split('\n')
  random.shuffle(listaprx)
with open(txt) as file:
  lista = file.read().split('\n')
threadnum = int(Threads)
threads = []
for i in lista:
  thread = threading.Thread(target=InstaEmail,args=(i.strip(),))
  threads.append(thread)
  thread.start()

