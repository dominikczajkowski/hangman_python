import sys
from random import randint

def check(lista):
	for i in lista:
		if (i == False):
			return False
	return True
l=0
if( sys.argv[1] == "easy"):
	print ("You choose easy level")
	lvl=0
elif( sys.argv[1] == "hard"):
	print("You choose hard level")
	lvl=1

while(True):
		if (lvl == 0):
			cnt=len(open("easy.txt" , "r").readlines())
			try:
				st=open("easy.txt", "r")
			except FileNotFoundError:
				print("Nie ma pliku easy.txt")
				break
		elif (lvl == 1):
			cnt=len(open("hard.txt", "rU").readlines())
			try:
				st=open("hard.txt", "r")
			except FileNotFoundError:
				print("Nie ma pliku hard.txt")
				break
		r=randint(1,cnt)
		st2=[]
		for i in range(0,r):
			st2=st.readline()
		st.close()
		st3=[]
		st4=[]
		e=0
		s=0
		s2=0
		for i in range(len(st2)-1):
			st3.append('_')
			st4.append(False)
		while((check(st4) == False)):
			s=0
			f=False
			for i in range(len(st2)-1):
				print(st3[i], end=" ")
			print("")
			if (s2 == 0 and lvl == 1):
				k=' '
				s2=1
			else:
				k=input("Podaj literę:\n")
			for i in range(len(st2)-1):
				if ( st2[i] == k):
					st3[i]=k
					st4[i]=True
					f=True
				elif (st4[i] == False):
					st3[i]='_'
			if(f == False):
				e+=1
			print (80*"\n")
		
			if(e == 1):
				print("  ")
				print("  ")
				print("  ")
				print("  ")
				print("  ")
				print("/|\\")
			elif(e == 2):
				print(" |")
				print(" |")
				print(" |")
				print(" |")
				print("/|\\")
			elif(e == 3):
				print(" ____")
				print(" |")
				print(" |")
				print(" |")
				print(" |")
				print("/|\\")
			elif(e == 4):
				print(" ____")
				print(" |/")
				print(" |")
				print(" |")
				print(" |")
				print("/|\\")
			elif(e == 5):
				print(" ____")
				print(" |/ |")
				print(" |")
				print(" |")
				print(" |")
				print("/|\\")
			elif(e == 6):
				print(" ____")
				print(" |/ |")
				print(" |  O")
				print(" | /|\\")
				print(" | / \\")
				print("/|\\")		
			if (e > 5):
 				break;
		if (e > 5):
			print("przegrałeś xD")
		else:
			print("wygrałeś")
		y=input("Jeszcze raz? y/n")
		if (y == 'n'):
			break;
