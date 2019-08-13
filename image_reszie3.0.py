from PIL import Image
import os
#H = 2.2 / B = 5.3

path1 = r"C:\Users\Administrator.USER-20190423VA\Desktop\image\6\H"
path2 = r"C:\Users\Administrator.USER-20190423VA\Desktop\image\6\B"
re_path_L = r"C:\Users\Administrator.USER-20190423VA\Desktop\image\6\RH"
re_path_R = r"C:\Users\Administrator.USER-20190423VA\Desktop\image\6\RB"

size = 1075/2592
count = 0
bmp_L = []
bmp_R = []

##resize to R_HIK & get the numbers of images
filelist1 = os.listdir(path1) #get names of file and subfile 
filelist1.sort() #the names of files will be sorted by file order
for file in filelist1:
    Olddir = os.path.join(path1,file)
    if os.path.splitext(Olddir)[1] == '.bmp':
        bmp_L.append(Olddir)
        count += 1
    else:
        print('LHshit!')
#print(bmp_L[0])

for i in range(count):
    img = Image.open(bmp_L[i])
    (x, y) = img.size
    out = img.resize((int(x*size), int(y*size)), Image.ANTIALIAS)
    path = os.path.join(re_path_L,'%d.bmp'%i)
    out.save(path)
   
#resize to L_BAS
filelist2 = os.listdir(path2) #get names of file and subfile 
filelist2.sort() #the names of files will be sorted by file order
for file in filelist2:
    Olddir = os.path.join(path2,file)
    if os.path.splitext(Olddir)[1] == '.bmp':
        bmp_R.append(Olddir)
    else:
        print('RBshit!')
print('1')

for i in range(count):
    img = Image.open(bmp_R[i])
    cropped = img.crop((163, 150, 1238, 956)) 
    path = os.path.join(re_path_R,'%d.bmp'%i)
    cropped.save(path)
