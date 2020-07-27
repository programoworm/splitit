import time
import multiprocessing
from PyPDF2 import PdfFileReader,PdfFileWriter
iname=input("Enter the name of the pdf file: ")
fname=input("Enter the name of the text file: ")
file=open(fname,'r')
serial=int(input("Enter the serial no. to start: "))
ip=PdfFileReader(iname)
for i in range(ip.getNumPages()):
	s=file.readline().strip()
	if not s:
		break
	l= s.split()
	line= ""
	for j in range(len(l)):
		s=l[j]
		line += (s[0].upper())
	print(line)
	writer=PdfFileWriter()
	writer.addPage(ip.getPage(i))
	with open(str(serial)+"_"+line+".pdf",'wb') as out:
		writer.write(out)
	serial+=1
	print('Created: page '+str(i+1))
file.close()