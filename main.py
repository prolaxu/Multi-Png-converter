from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def process():
	print("######################  Png Converter ######################")
	path=input("Enter image path : ")
	files= os.listdir(path)
	try:
		os.mkdir(path+'convertedpng')
	except:
		print("Folder Found")
		
	for x in files:
		if(x[-4:]=='.jpg'):
			p= path+x
			im1 = Image.open(p)
			sp=path+'convertedpng/'+x[:len(x)-4]+'.png'
			im1.save(sp)
			print(x," Converted to png")

		elif (x[-4:]=='jpeg'):
			p= path+x
			im1 = Image.open(p)
			sp=path+'convertedpng/'+x[:len(x)-4]+'png'
			im1.save(sp)
			print(x," Converted to png")

	if (len(files)==0):
		print("No jpg and jpeg file fonud !")
	else:
		print("All Converted successfully !")

process()
