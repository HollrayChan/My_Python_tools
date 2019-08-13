from PIL import Image
import os
#H = 2.2 / B = 5.3

pathH = r"C:\Users\Administrator.USER-20190423VA\Desktop\image\industry_camera_pose\sequence190812\H"
pathB = r"C:\Users\Administrator.USER-20190423VA\Desktop\image\industry_camera_pose\sequence190812\B"
re_pathH = r"C:\Users\Administrator.USER-20190423VA\Desktop\image\industry_camera_pose\sequence190812\RH"
re_pathB = r"C:\Users\Administrator.USER-20190423VA\Desktop\image\industry_camera_pose\sequence190812\RB"

size = 1075/2592
count = 0
bmp_L = []
bmp_R = []

##resize to R_HIK & get the numbers of images
filelist1 = os.listdir(pathH) #get names of file and subfile 
filelist1.sort() #the names of files will be sorted by file order
for file in filelist1:
    Olddir = os.path.join(pathH,file)
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
    path = os.path.join(re_pathH,'%d.bmp'%i)
    out.save(path)
   
#resize to L_BAS
filelist2 = os.listdir(pathB) #get names of file and subfile 
filelist2.sort() #the names of files will be sorted by file order
for file in filelist2:
    Olddir = os.path.join(pathB,file)
    if os.path.splitext(Olddir)[1] == '.bmp':
        bmp_R.append(Olddir)
    else:
        print('RBshit!')
print('success')

for i in range(count):
    img = Image.open(bmp_R[i])
    cropped = img.crop((163, 118, 1238, 924)) 
    path = os.path.join(re_pathB,'%d.bmp'%i)
    cropped.save(path)
