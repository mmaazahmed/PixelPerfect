from PIL import Image
from config import Config
from datetime import datetime,timedelta
import shutil
import os

UPLOAD_FOLDER=

c=[0,0,0] # will store average r,g,b values for each pf_block i.e pf*pf

def remove_directory():  # will remove puzzle 2 from today

    remove_date=datetime.strftime(datetime.now() - timedelta(2), '%m-%d-%Y')
    path=os.getcwd()+'/app/static/images/'+ remove_date
    try:
        shutil.rmtree(path)
    except OSError:
        print ("del of the directory %s failed" % path)
        return False
    else:
        print ("del of the directory succeeded %s " % path)
        return True

def create_directory():
    today=datetime.strftime(datetime.now(), '%m-%d-%Y')
    path=os.getcwd()+'/app/static/images/'+ str(today)

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
        return False
    else:
        print ("Successfully created the directory %s " % path)
        return True
    pass
def create_new_puzzle():

    today=datetime.strftime(datetime.now() - timedelta(1), '%m-%d-%Y')
    remove_directory()
    create_directory()
    #image=[(img path,today)]pull image frmo db using (today)
    #populate_directories(image)
    

def populate_directories(images):
    if len(images)> 1: 
        pass
    else:
        pixelelate(images[0],images[1],images[2])
    
    pass

def get_images(dates):
    images=[]
    for date in dates:
        # pull image from db
        #image= (imagePath,date,pf)
        pass

    return []



def initialiseGame():
    dates=get_dates
    create_directories() # create 3 directories with yesterday,today's, and tomorrow's dates in that order
    images=get_images(dates)# return a list of tuples in the format (path to image,date associated with image,pixelFactor)
    populate_directories(images) # populate directories with pixelated images


def get_dates():
    dates=[]

    yesterday=datetime.strftime(datetime.now() - timedelta(1), '%m-%d-%Y') 
    dates.append(yesterday)

    today=datetime.strftime(datetime.now(), '%m-%d-%Y')
    dates.append(today)

    tomorrow=datetime.strftime(datetime.now() + timedelta(1), '%m-%d-%Y') 
    dates.append(tomorrow)

    return dates

def create_directories():
    dates=get_dates()
    
    for date in dates:

        path=os.getcwd()+'/app/static/images/'+ str(date)
        print(path)
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
            print("fa")
            return False
        else:
            print ("Successfully created the directory %s " % path)
            return True
    
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
    assignAvg(k,(i*k),j*k,pix,avg)
    c[0]=0
    c[1]=0
    c[2]=0


def pixelelate(img,pixel_factors): #@params img= string path to the image , pixel_factor= list of pixelation factors for 5 attempts
    
    path='./app/static/images/images/'
    img_path= path+img
    im = Image.open(img_path)

    pix = im.load()
    row=im.size[0]
    col= im.size[1]
    count=len(pixel_factors)+1

    for pf in pixel_factors:
        if pf!=0:
            block_row=row//int(pf) # creating a block of area pf*pf to go through the image
            block_col=col//int(pf)
            print("im here")
            for i in range(block_row):
                for j in range(block_col):
                    i=int(i)
                    j=int(j)
                    pf=int(pf)
                    doShit(pf,i,j,pix)
        count-=1
        destination='./app/static/images/'+'tmp/'+str(count)+img[-4:]
        im.save(destination)


#print(create_directories())
remove_directory()