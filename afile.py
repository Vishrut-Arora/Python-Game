import os
import time
import random
from random import randint
class Grid:
    def __init__(self,N):
        self.N=N
        l1=[0,N-1]
        l2=[0,random.randint(1,N-1)]
        x=random.randint(0,1)
        z=random.randint(0,1)
        y=random.randint(0,1)
        self.myObstacles=[]
        self.myRewards=[]
        if(x==0):
            self.startx=l1[z]
            self.starty=l2[y]
            self.goalx=l1[1-z]
            self.goaly=l2[1-y]
        else:
            self.starty=l1[z]
            self.startx=l2[y]
            self.goaly=l1[1-z]
            self.goalx=l2[1-y]
        self.p=Player(self.startx,self.starty,(self.N)*2)

        for i in range(random.randint(1,2*N)):
            a=random.randint(0,N-1)
            b=random.randint(0,N-1)
            self.myObstacles.append(Obstacle(a,b))
            self.myRewards.append(Reward(N-a,N-b,random.randint(1,9)))


    def rotateClockwise(self,n):
        count=0
        while(count<=n):
            for i in range(len(self.myObstacles)):
                a=self.myObstacles[i].x
                b=self.myObstacles[i].y
                self.myObstacles[i].x=b
                self.myObstacles[i].y=self.N-a-1
            for i in range(len(self.myRewards)):
                a=self.myRewards[i].x
                b=self.myRewards[i].y
                self.myRewards[i].x=b
                self.myRewards[i].y=self.N-a-1
            count=count+1
            self.p.energy-=self.N//3



    def rotateAnticlockwise(self,m):
        count=0
        while(count<=m):
            for i in range(len(self.myObstacles)):
                a=self.myObstacles[i].x
                b=self.myObstacles[i].y
                self.myObstacles[i].x=y=self.N-b-1
                self.myObstacles[i].y=a
            for i in range(len(self.myRewards)):
                a=self.myRewards[i].x
                b=self.myRewards[i].y
                self.myRewards[i].x=self.N-b-1
                self.myRewards[i].y=a
            count=count+1
            self.p.energy-=self.N//3





    def showgrid(self,N):


        k=[]
        print()
        for i in range(0, N):
                p=[]
                for j in range(0, N):
                    #print (i,end=" ")
                    if(self.goaly==i and self.goalx==j):
                        p.append("@")
                    elif(self.starty==i and self.startx==j):
                        p.append("O")
                    else:
                        flg=0
                        for c in range(len(self.myObstacles)):
                            if(self.myObstacles[c].x==i and self.myObstacles[c].y==j):
                                flg=1
                                p.append("#")
                        for d in range(len(self.myRewards)):
                            if(self.myRewards[d].x==i and self.myRewards[d].y==j):
                                flg=1
                                p.append(self.myRewards[d].v)
                                break
                        if(flg==0):
                            p.append(".")
                k.append(p)
                #print(end="\n")
        for i in range(len(k)):
            for j in range(len(k[i])):
                print(k[i][j],end="")
            print()
        print(self.p)

class Obstacle:
    def __init__(self,xo,yo):
        self.x=xo
        self.y=yo

class Reward:
    def __init__(self,xr,yr,v):
        self.x=xr
        self.y=yr
        self.v=v

class Player:
    def __init__(self,xp,yp,energy):
        self.xp=xp
        self.yp=yp
        self.energy=energy

    def makeMove(self,N,s):   #put condition when value of move greater than current
        global gr

                           #coordinate of player

        aa=[]
        for i in range(len(s)):
            if(s[i].isalpha()):
                aa.append(i)
        for i in range(len(aa)):

            if(s[aa[i]]=='R'or s[aa[i]]=='r'):

                if((len(aa))==1 or i==(len(aa)-1)):
                    for j in range(int(s[aa[i]+1:])):
                        if(gr.startx>=N-1):
                            gr.startx=0
                            gr.p.energy-=1
                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()
                        else:
                            gr.startx+=1
                            gr.p.energy-=1
                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")

                            print("ENERGY:",gr.p.energy)

                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()

                else:
                    for a in range(int(s[aa[i]+1:aa[i+1]])):
                        if(gr.startx>=N-1):
                            gr.startx=0
                            gr.p.energy-=1
                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()
                        else:
                            gr.startx+=1
                            gr.p.energy-=1
                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()


            if(s[aa[i]]=='L'or s[aa[i]]=='l'):
                if(len(aa)==1 or i==len(aa)-1):
                    for j in range(int(s[aa[i]+1:])):
                        if(gr.startx<=0):
                            gr.startx=N-1
                            gr.p.energy-=1

                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()
                        else:
                            gr.startx-=1
                            gr.p.energy-=1

                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()
                else:
                    for j in range(int(s[aa[i]+1:aa[i+1]])):
                        if(gr.startx<=0):
                            gr.startx=N-1
                            gr.p.energy-=1

                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()
                        else:
                            gr.startx-=1
                            gr.p.energy-=1

                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()

            if(s[aa[i]]=='U'or s[aa[i]]=='u'):
                if(len(aa)==1 or i==len(aa)-1):
                    for j in range(int(s[aa[i]+1:])):
                        if(gr.starty<=0):
                            gr.starty=N-1
                            gr.p.energy-=1

                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()
                        else:
                            gr.starty-=1
                            gr.p.energy-=1

                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()

                else:
                    for j in range(int(s[aa[i]+1:aa[i+1]])):
                        if(gr.starty<=0):
                            gr.starty=N-1
                            gr.p.energy-=1

                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()
                        else:
                            gr.starty-=1
                            gr.p.energy-=1
                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()

            if(s[aa[i]]=='D'or s[aa[i]]=='d'):
                if(len(aa)==1 or i==len(aa)-1):
                    for j in range(int(s[aa[i]+1:])):
                        if(gr.starty>=N-1):
                            gr.starty=0
                            gr.p.energy-=1

                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()
                        else:
                            gr.starty+=1
                            gr.p.energy-=1


                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()


                else:
                    for j in range(int(s[aa[i]+1:aa[i+1]])):
                        if(gr.starty>=N-1):
                            gr.starty=0
                            gr.p.energy-=1
                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()

                        else:
                            gr.starty+=1
                            gr.p.energy-=1


                            for c in range(len(gr.myObstacles)):
                                if(gr.myObstacles[c].y==gr.startx and gr.myObstacles[c].x==gr.starty):
                                    gr.p.energy-=gr.N*4
                            for d in range(len(gr.myRewards)):
                                if(gr.myRewards[d].y==gr.startx and gr.myRewards[d].x==gr.starty):
                                    gr.p.energy+=gr.myRewards[d].v*gr.N
                            time.sleep(1)
                            os.system("cls")
                            print("ENERGY:",gr.p.energy)
                            gr.showgrid(N)
                            if(gr.p.energy<=0):
                                print("GAME OVER")
                                exit()


            if((s[aa[i]]=='A'or s[aa[i]]=='a')):
                if(len(aa)==1 or i==len(aa)-1):
                    for j in range(int(s[aa[i]+1:])):
                        gr.rotateAnticlockwise(1)
                        time.sleep(1)

                        print("ENERGY:",gr.p.energy)
                        gr.showgrid(N)
                    if(gr.p.energy<=0):
                        print("GAME OVER")
                        exit()

                else:
                    for j in range(int(s[aa[i]+1:aa[i+1]])):
                        gr.rotateAnticlockwise(1)
                        time.sleep(1)

                        print("ENERGY:",gr.p.energy)
                        gr.showgrid(N)
                    if(gr.p.energy<=0):
                        print("GAME OVER")
                        exit()

            if(s[aa[i]]=='C'or s[aa[i]]=='c'):
                if(len(aa)==1 or i==len(aa)-1):
                    for j in range(int(s[aa[i]+1:])):
                        gr.rotateClockwise(1)
                        time.sleep(1)

                        print("ENERGY:",gr.p.energy)
                        gr.showgrid(N)
                    if(gr.p.energy<=0):
                        print("GAME OVER")
                        exit()

                else:
                    for j in range(int(s[aa[i]+1:aa[i+1]])):
                        gr.rotateClockwise(1)
                        time.sleep(1)

                        print("ENERGY:",gr.p.energy)
                        gr.showgrid(N)
                    if(gr.p.energy<=0):
                        print("GAME OVER")
                        exit()


N=int(input("Enter N:"))
gr=Grid(N)

print("ENERGY:",gr.p.energy)
gr.showgrid(N)
while((gr.startx!=gr.goalx or gr.starty!=gr.goaly)):
    time.sleep(1)
    s=input("Enter algo ")
    gr.p.makeMove(N,s)

print("YOU WON")
