from PIL import Image
import os
c=[0,0,0]
def avg(l,k):
    return l//(k*k)

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
def pixel(image,pf):
    im = Image.open(image)
    k=1
    totalPixels=im.size[0] #*(im.size[1])
    k= pf # pixelation factor
    print(k)
    pix = im.load()
    row=im.size[0]//k
    col= im.size[1]//k
    for i in range(row):
        for j in range(col):
            doShit(k,i,j,pix)
        

    
    
    im.save("./static/images/c.png")
                
path='./static/images/bmo.png'
print(path)
pixel(path,23) #image source name in current dir

