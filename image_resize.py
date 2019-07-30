# 1280x1024 1280=32x40
# 2592x1944 2592=32x81
# 1296 972  1024/1944=0.5267


'''
img = Image.open('ee.jpg')

(x, y) = img.size

x_s = 190

y_s = y * x_s / x

out = img.resize((x_s, y_s), Image.ANTIALIAS)

out.save('ff.jpg')
'''

from PIL import Image
import os

path = r"C:\Users\Administrator.USER-20190423VA\Desktop\photo\L_camera"
filelist = os.listdir(path) #get names of file and subfile 
filelist.sort() #the names of files will be sorted by file order
size = 1024/1944
count = 0
bmp = []

for file in filelist:
    Olddir = os.path.join(path,file)
    if os.path.splitext(Olddir)[1] == '.bmp':
        bmp.append(Olddir)
        count += 1
    else:
        print('shit!')
print(count)

for i in range(count):
    img = Image.open(bmp[i])
    (x, y) = img.size
    out = img.resize((int(x*size), int(y*size)), Image.ANTIALIAS)
    cropped = out.crop((43, 0, 1323, 1024)) 
    cropped.save('%d.bmp' %i)
print(cropped)
    
    