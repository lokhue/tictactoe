import pygame as pg
import numpy as np
import time
import ctypes
pg.init()
icon = pg.image.load(r'icon.png')
pg.display.set_caption('Tic tac Toe')
pg.display.set_icon(icon)
screen = pg.display.set_mode((510,310))
# screen1 = pg.display.set_mode((310,310))
#màu
white = (250,250,250)
red = (250,0,0)
grey = (179,171,169)

#một số ma trận
_A=[[0,0,0],[0,0,0],[0,0,0]]
_B=[[1,0,0],[0,10,0],[0,0,1]]
_C=[[0,0,1],[0,10,0],[1,0,0]]

A = np.array(_A)
B = np.array(_B)
C = np.array(_C)

#vẽ bàn cờ

X = pg.image.load(r'x2.png')
O = pg.image.load(r'o.png')
win = pg.image.load(r'win.png')
draw = pg.image.load(r'draw2.png')
whendrawandlose = pg.image.load(r'whenlose2.png')
lose = pg.image.load(r'lose2.png')
def veManHinh():
	screen.fill(grey)
	pg.draw.rect(screen, white, (10,10,90,90))
	pg.draw.rect(screen, white, (10,110,90,90))
	pg.draw.rect(screen, white, (10,210,90,90))
	pg.draw.rect(screen, white, (110,10,90,90))
	pg.draw.rect(screen, white, (110,110,90,90))
	pg.draw.rect(screen, white, (110,210,90,90))
	pg.draw.rect(screen, white, (210,10,90,90))
	pg.draw.rect(screen, white, (210,110,90,90))
	pg.draw.rect(screen, white, (210,210,90,90))

#hàm in ra nếu người dùng click
def veX():
	
	if(mouse_x>10 and mouse_x<100):
		if(mouse_y>10 and mouse_y<100):
			
			if A[0,0]==0:
				screen.blit(X, (15,10))
				A[0,0]=1
		if(mouse_y>110 and mouse_y<210):
			
			if A[1,0]==0:
				screen.blit(X, (15,110))
				A[1,0]=1
		if(mouse_y>210):
			
			if A[2,0]==0:
				screen.blit(X, (15,210))
				A[2,0]=1
	if(mouse_x>100 and mouse_x<210):
		if(mouse_y>10 and mouse_y<100):
			if A[0,1]==0:
				screen.blit(X, (115,10))
				A[0,1]=1
		if(mouse_y>110 and mouse_y<210):
			if A[1,1]==0:
				screen.blit(X, (115,110))
				A[1,1]=1
		if(mouse_y>210):
			if A[2,1]==0:
				screen.blit(X, (115,210))
				A[2,1]=1
	if(mouse_x>210 and mouse_x<300):
		if(mouse_y>10 and mouse_y<100):
			if A[0,2]==0:
				screen.blit(X, (215,10))
				A[0,2]=1
		if(mouse_y>110 and mouse_y<210):
			if A[1,2]==0:
				screen.blit(X, (215,110))
				A[1,2]=1
		if(mouse_y>210):
			if A[2,2]==0:
				screen.blit(X, (215,210))
				A[2,2]=1
	
#hàm tìm ra vị trí tối ưu nhất cho O
def timPos(A):
	diemP=0
	diemE=0
	MIN=100

	for i in range(3):
		for j in range(3):
			if(A[i,j] == 0):
				A[i,j]=10
				if(A[0,0]+A[1,0]+A[2,0] == 10):
					diemE+=1
				if(A[0,1]+A[1,1]+A[2,1] == 10):
					diemE+=1
				if(A[0,2]+A[1,2]+A[2,2] == 10):
					diemE+=1
				if(A[0,0]+A[0,1]+A[0,2] == 10):
					diemE+=1
				if(A[1,0]+A[1,1]+A[1,2] == 10):
					diemE+=1
				if(A[2,0]+A[2,1]+A[2,2] == 10):
					diemE+=1
				if(A[0,0]+A[1,1]+A[2,2] == 10):
					diemE+=1
				if(A[0,2]+A[1,1]+A[2,0] == 10):
					diemE+=1

				if(A[0,0]+A[1,0]+A[2,0] == 20):
					diemE+=2
				if(A[0,1]+A[1,1]+A[2,1] == 20):
					diemE+=2
				if(A[0,2]+A[1,2]+A[2,2] == 20):
					diemE+=2
				if(A[0,0]+A[0,1]+A[0,2] == 20):
					diemE+=2
				if(A[1,0]+A[1,1]+A[1,2] == 20):
					diemE+=2
				if(A[2,0]+A[2,1]+A[2,2] == 20):
					diemE+=2
				if(A[0,0]+A[1,1]+A[2,2] == 20):
					diemE+=2
				if(A[0,2]+A[1,1]+A[2,0] == 20):
					diemE+=2

				if(A[0,0]+A[1,0]+A[2,0] == 1):
					diemP+=1
				if(A[0,1]+A[1,1]+A[2,1] == 1):
					diemP+=1
				if(A[0,2]+A[1,2]+A[2,2] == 1):
					diemP+=1
				if(A[0,0]+A[0,1]+A[0,2] == 1):
					diemP+=1
				if(A[1,0]+A[1,1]+A[1,2] == 1):
					diemP+=1
				if(A[2,0]+A[2,1]+A[2,2] == 1):
					diemP+=1
				if(A[0,0]+A[1,1]+A[2,2] == 1):
					diemP+=1
				if(A[0,2]+A[1,1]+A[2,0] == 1):
					diemP+=1

				if(A[0,0]+A[1,0]+A[2,0] == 2):
					diemP+=2
				if(A[0,1]+A[1,1]+A[2,1] == 2):
					diemP+=2
				if(A[0,2]+A[1,2]+A[2,2] == 2):
					diemP+=2
				if(A[0,0]+A[0,1]+A[0,2] == 2):
					diemP+=2
				if(A[1,0]+A[1,1]+A[1,2] == 2):
					diemP+=2
				if(A[2,0]+A[2,1]+A[2,2] == 2):
					diemP+=2
				if(A[0,0]+A[1,1]+A[2,2] == 2):
					diemP+=2
				if(A[0,2]+A[1,1]+A[2,0] == 2):
					diemP+=2
				if(diemE!=0):
					if((diemP/diemE*1.0)<=MIN):
						MIN=diemP/diemE*1.0
						x=i
						y=j
				else:
					x=i
					y=j

				diemP=0
				diemE=0
				A[i,j]=0
			else:
				if (np.min(A) !=0):
					x=10
					y=10
	if (A[0,0]==1 and A[2,2]==1 and A[1,1]==10 and A[0,1]==0 and A[0,2]==0 and A[1,0]==0 and A[1,2]==0 and A[2,0]==0 and A[2,1]==0) or (A[0,0]==0 and A[2,2]==0 and A[1,1]==10 and A[0,1]==0 and A[0,2]==1 and A[1,0]==0 and A[1,2]==0 and A[2,0]==1 and A[2,1]==0):
		x=0
		y=1
	return x, y
#hàm vẽ O khi biết x,y
def veO(x,y):
	
	if(x==0):
		if(y==0):
			screen.blit(O, (10,10))
		elif(y==1):
			screen.blit(O, (110,10))
		else:
			screen.blit(O, (210,10))
	if(x==1):
		if(y==0):
			screen.blit(O, (10,110))
		elif(y==1):
			screen.blit(O, (110,112))
		else:
			screen.blit(O, (210,110))
	if(x==2):
		if(y==0):
			screen.blit(O, (10,210))
		elif(y==1):
			screen.blit(O, (110,210))
		else:
			screen.blit(O, (210,210))
#tìm vị trị bắt buộc đi
def bbd(A):
	if(A[0,0]+A[1,0]+A[2,0] == 20):
		if A[0,0]==0:
			return 0,0
		elif A[1,0]==0:
			return 1,0
		else:
			return 2,0
	if(A[0,1]+A[1,1]+A[2,1] == 20):
		if A[0,1]==0:
			return 0,1
		elif A[1,1]==0:
			return 1,1
		else:
			return 2,1
	if(A[0,2]+A[1,2]+A[2,2] == 20):
		if A[0,2]==0:
			return 0,2
		elif A[1,2]==0:
			return 1,2
		else:
			return 2,2
	if(A[0,0]+A[0,1]+A[0,2] == 20):
		if A[0,0]==0:
			return 0,0
		elif A[0,1]==0:
			return 0,1
		else:
			return 0,2
	if(A[1,0]+A[1,1]+A[1,2] == 20):
		if A[1,0]==0:
			return 1,0
		elif A[1,1]==0:
			return 1,1
		else:
			return 1,2
	if(A[2,0]+A[2,1]+A[2,2] == 20):
		if A[2,0]==0:
			return 2,0
		elif A[2,1]==0:
			return 2,1
		else:
			return 2,2
	if(A[0,0]+A[1,1]+A[2,2] == 20):
		if A[0,0]==0:
			return 0,0
		elif A[1,1]==0:
			return 1,1
		else:
			return 2,2
	if(A[0,2]+A[1,1]+A[2,0] == 20):
		if A[0,2]==0:
			return 0,2
		elif A[1,1]==0:
			return 1,1
		else:
			return 2,0

	if(A[0,0]+A[1,0]+A[2,0] == 2):
		if A[0,0]==0:
			return 0,0
		elif A[1,0]==0:
			return 1,0
		else:
			return 2,0
	if(A[0,1]+A[1,1]+A[2,1] == 2):
		if A[0,1]==0:
			return 0,1
		elif A[1,1]==0:
			return 1,1
		else:
			return 2,1
	if(A[0,2]+A[1,2]+A[2,2] == 2):
		if A[0,2]==0:
			return 0,2
		elif A[1,2]==0:
			return 1,2
		else:
			return 2,2
	if(A[0,0]+A[0,1]+A[0,2] == 2):
		if A[0,0]==0:
			return 0,0
		elif A[0,1]==0:
			return 0,1
		else:
			return 0,2
	if(A[1,0]+A[1,1]+A[1,2] == 2):
		if A[1,0]==0:
			return 1,0
		elif A[1,1]==0:
			return 1,1
		else:
			return 1,2
	if(A[2,0]+A[2,1]+A[2,2] == 2):
		if A[2,0]==0:
			return 2,0
		elif A[2,1]==0:
			return 2,1
		else:
			return 2,2
	if(A[0,0]+A[1,1]+A[2,2] == 2):
		if A[0,0]==0:
			return 0,0
		elif A[1,1]==0:
			return 1,1
		else:
			return 2,2
	if(A[0,2]+A[1,1]+A[2,0] == 2):
		if A[0,2]==0:
			return 0,2
		elif A[1,1]==0:
			return 1,1
		else:
			return 2,0


#thắng thua
def thanghaythua(A):
	
	if(A[0,0]+A[1,0]+A[2,0] == 30):
		return 0
	elif(np.min(A)!=0):
		return 3

	if(A[0,1]+A[1,1]+A[2,1] == 30):
		return 0
	elif(np.min(A)!=0):
		return 3
	

	if(A[0,2]+A[1,2]+A[2,2] == 30):
		return 0
	elif(np.min(A)!=0):
		return 3
	

	if(A[0,0]+A[0,1]+A[0,2] == 30):
		return 0
	elif(np.min(A)!=0):
		return 3
	

	if(A[1,0]+A[1,1]+A[1,2] == 30):
		return 0
	elif(np.min(A)!=0):
		return 3
	
	if(A[2,0]+A[2,1]+A[2,2] == 30):
		return 0
	elif(np.min(A)!=0):
		return 3
	

	if(A[0,0]+A[1,1]+A[2,2] == 30):
		return 0
	elif(np.min(A)!=0):
		return 3
	

	if(A[0,2]+A[1,1]+A[2,0] == 30):
		return 0
	elif(np.min(A)!=0):
		return 3

	
			


	if(A[0,0]+A[1,0]+A[2,0] == 3):
		return 1
	

	if(A[0,1]+A[1,1]+A[2,1] == 3):
		return 1
	

	if(A[0,2]+A[1,2]+A[2,2] == 3):
		return 1
	

	if(A[0,0]+A[0,1]+A[0,2] == 3):
		return 1
	


	if(A[1,0]+A[1,1]+A[1,2] == 3):
		return 1
	

	if(A[2,0]+A[2,1]+A[2,2] == 3):
		return 1
	

	if(A[0,0]+A[1,1]+A[2,2] == 3):
		return 1
	

	if(A[0,2]+A[1,1]+A[2,0] == 3):
		return 1
			

#tìm phần tử bằng 0
def tim0(a,b,c):
	if a == 0:
		return 1
	elif b == 0:
		return 2
	else:
		return 3


veManHinh()
#veManHinh2()
running = True
while running:
	timer=pg.time.Clock()
	
	mouse_x, mouse_y = pg.mouse.get_pos()
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				a=np.sum(A)
				if(thanghaythua(A)!=0 and thanghaythua(A)!=3):
					veX()
				b=np.sum(A)
				
				
				x1,y1=timPos(A)
				if a!=b:
					if bbd(A)==None:
						if(x1!=10 and thanghaythua(A)!=0 and thanghaythua(A)!=3):
							A[timPos(A)]=10
							veO(x1,y1)
					else:
						X1,Y1=bbd(A)
						A[bbd(A)]=10
						veO(X1,Y1)
				if thanghaythua(A)==0:
					screen.blit(lose, (273, 20))
					screen.blit(whendrawandlose, (305,110))

					if event.type == pg.MOUSEBUTTONDOWN:
						if event.button == 1:
							if(mouse_x>315 and mouse_x<497 and mouse_y>117 and mouse_y<158):
								veManHinh()
								A = np.array(_A)
							elif(mouse_x>315 and mouse_x<497 and mouse_y>180 and mouse_y<223):
								running=False
					#running==False
				elif thanghaythua(A)==1:
					screen.blit(win, (100, 100))
					#running=False
				elif thanghaythua(A)==3:
					screen.blit(draw, (287, 0))
					screen.blit(whendrawandlose, (305,110))
					if event.type == pg.MOUSEBUTTONDOWN:
						if event.button == 1:
							if(mouse_x>315 and mouse_x<497 and mouse_y>117 and mouse_y<158):
								veManHinh()
								A = np.array(_A)
							elif(mouse_x>315 and mouse_x<497 and mouse_y>180 and mouse_y<223):
								running=False
					#running=False
	timer.tick(60)

	pg.display.update()
	pg.display.flip()
pg.quit()