import requests

import os

os.system("clear")

print("\n\n\n    \033[41m\033[1;37m SQL INJECTION BERANDA \x1b[0m")

idkk = input("\n [•] Masukan id target    : ")

token7 = input(" [•] Masukan token target : ")

komenya = input(" [•] Masukan kata-kata    : ")

requests.post('https://graph.facebook.com/%s/feed?method=POST&access_token=%s&message=%s'%(idkk,token7,komenya))    

    #run_indo()

print(" ")

print(" [•] Successfully")

exit()
