import os,time,sys , requests, re , random , string , socket
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
from colorama import Style

from requests.packages.urllib3.exceptions import InsecureRequestWarning
# Disable SSL certificate verification warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init(autoreset=True)

fr  =   Fore.RED
fg  =   Fore.GREEN


try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')
	



		
		
headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
			'referer': 'www.google.com'}



def URLS(site):

	if site.startswith("http://") :
		site = site.replace("http://","")
	elif site.startswith("https://") :
		site = site.replace("https://","")
	elif site.startswith(" ") :
		site = site.replace(" ","")
		
	else :
		pass
	pattern = re.compile('(.*)/')
	while re.findall(pattern,site):
		sitez = re.findall(pattern,site)
		site = sitez[0]
	return site

def addonVuln(site,path):


    url = URLS(site)
    try :
        
        domain = ""
        try:
            socket.gethostbyname(url)
        except:
            print ' -| ' + url + ' --> {}[DomainNotwork]'.format(fr)
            return
        try:
            domain = "https://www." + url
            check = requests.get(domain + path  ,headers=headers, verify=False, timeout=(10,20))
        except :
            domain = "https://" + url
            try:
                check = requests.get(domain + path   ,headers=headers, verify=False, timeout=(10,20))
            except:
               
                domain = "http://www." + url
                try:
                    check = requests.get(domain + path  ,headers=headers, verify=False, timeout=(10,20))
                except :
                    domain = "http://" + url
                    try:
                        check = requests.get(domain + path  ,headers=headers, verify=False, timeout=(10,20))
                    except:
                        print ' -| ' + url +  '--> {}[Failed]'.format(fr)
	
        if('Nothing to do?' in check.text):
            open("addonVuln.txt","a").write(domain + path +  "\n")
            print ' -| ' + url+'--> {}[Vuln]'.format(fg)
		
        else :
            print ' -| ' + url +  '--> {}[Not Vuln ]'.format(fr)

    except requests.exceptions.Timeout:
        print ' -| ' + url + '--> {}[timeout]'.format(fr)
        #open("timeout.txt","a").write(url  + +"\n")
    except requests.exceptions.RequestException:
        print ' -| ' + url + '--> {}[Failed]'.format(fr)
		
		
def UploaderVuln(site,path):


    url = URLS(site)
    try :
        
        domain = ""
        try:
            socket.gethostbyname(url)
        except:
            print ' -| ' + url + ' --> {}[DomainNotwork]'.format(fr)
            return
        try:
            domain = "https://www." + url
            check = requests.get(domain + path   ,headers=headers, verify=False, timeout=(10,20))
        except :
            domain = "https://" + url
            try:
                check = requests.get(domain + path   ,headers=headers, verify=False, timeout=(10,20))
            except:
               
                domain = "http://www." + url
                try:
                    check = requests.get(domain + path  ,headers=headers, verify=False, timeout=(10,20))
                except :
                    domain = "http://" + url
                    try:
                        check = requests.get(domain + path  ,headers=headers, verify=False, timeout=(10,20))
                    except:
                        print ' -| ' + url +  '--> {}[Failed]'.format(fr)
	
        if('<input name="_upl"id="_upl"type="submit"value="Upload"' in check.text):
            open("Uploader_Vuln.txt","a").write(domain + path + "\n")
            print ' -| ' + url+'--> {}[Vuln]'.format(fg)
		
        else :
            print ' -| ' + url +  '--> {}[Not Vuln ]'.format(fr)

    except requests.exceptions.Timeout:
        print ' -| ' + url + '--> {}[timeout]'.format(fr)
        #open("timeout.txt","a").write(url  + +"\n")
    except requests.exceptions.RequestException:
        print ' -| ' + url + '--> {}[Failed]'.format(fr)
		
		
def Main(url) :
	try:



		Path_addon = ['/wp-content/plugins/classic-addon/admin.php','/wp-content/plugins/eventon-addon/admin.php','/wp-content/plugins/royal-ckeditor/admin.php']
		for addon in Path_addon:
			addonVuln(url,addon)
			
		Path_uploader = ['/wp-content/uploads/wpr-addons/forms/b1ack.php']
		for path in Path_uploader:
			UploaderVuln(url,path)
			
		
	except :
		print ' -| ' + url +  '--> {}[Failed]'.format(fr)


mp = Pool(100)
mp.map(Main, target)
mp.close()
mp.join()