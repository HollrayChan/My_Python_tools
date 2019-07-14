import os

def rename(path): 
#    path='/home/chan/Desktop/neuralrgbd-master/data/datasets/scan-net-5-frame/scene0191_10' 
    filelist = os.listdir(path) #get names of file and subfile 
    filelist.sort() #the names of files will be sorted by file order
    count = 0
    jpg = []
    txt = []
    pgm = []
    
    for file in filelist:
#divided according to file suffix
        Olddir = os.path.join(path,file)
        if os.path.splitext(Olddir)[1] == '.jpg':
            jpg.append(Olddir)
            count += 1                      
        elif os.path.splitext(Olddir)[1] == '.txt':
            txt.append(Olddir)
        elif os.path.splitext(Olddir)[1] == '.pgm':
            pgm.append(Olddir)
        else:
            print('shit!')
#    print(jpg)
   
    for i in range(count):
        Newjpg = os.path.join(path,'frame-%06d.color.jpg'%i) 
        os.rename(jpg[i],Newjpg)
        Newtxt = os.path.join(path,'frame-%06d.pose.txt'%i) 
        os.rename(txt[i],Newtxt)
        Newpgm = os.path.join(path,'frame-%06d.depth.pgm'%i) 
        os.rename(pgm[i],Newpgm)


if __name__ == "__main__":
    for i in range(11):
        pathname = '/home/chan/Desktop/neuralrgbd-master/data/datasets/scan-net-5-frame/scene0191_%02d'%i
        rename(pathname)
