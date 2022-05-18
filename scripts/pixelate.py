from PIL import Image
import os
c=[0,0,0]
def avg(l,k):
    return l//(k*k)
def init():

    pixel('bmo.png',0)
def iterateThroughKbox(k,Xoffset,Yoffset,pix):
    for i in range (k):
        for j in range (k):
            c[0]+=pix[i+Xoffset,j+Yoffset][0]
            c[1]+=pix[i+Xoffset,j+Yoffset][1]
            c[2]+=pix[i+Xoffset,j+Yoffset][2]
    return (avg(c[0],k),avg(c[1],k),avg(c[2],k))


def assignAvg(k,Xoffset,Yoffset,pix,avg):
    for i in range (k):
        for j in range (k):
            pix[i+Xoffset,j+Yoffset]=tuple(avg)
            
            
def doShit(k,i,j,pix):
    avg=iterateThroughKbox(k,i*k,j*k,pix)
    #print(avg)
    assignAvg(k,(i*k),j*k,pix,avg)
    c[0]=0
    c[1]=0
    c[2]=0
def pixel(img,nG):
    pf=30- (5*nG)
    if nG==0:
        pf=60

    path='./app/static/images/'+img
    im = Image.open(path)
    k=1
    totalPixels=im.size[0] #*(im.size[1])
    k= pf # pixelation factor
    if k!=0:
        pix = im.load()
        row=im.size[0]//k
        col= im.size[1]//k
        for i in range(row):
            for j in range(col):
                doShit(k,i,j,pix)
        

    
    destination='./app/static/images/'+'c'+img[-4:]
    im.save(destination)
                
 #image source name in current dir

