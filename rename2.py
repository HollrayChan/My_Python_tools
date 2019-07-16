import os

def rename(path): 
#    path='/home/chan/Desktop/neuralrgbd-master/data/datasets/scan-net-5-frame/scene0191_10' 
    filelist = os.listdir(path) #get names of file and subfile 
    filelist.sort() #the names of files will be sorted by file order
    count = 0
#    jpg = []
    txt = []
    png = []
    color =[]
    depth = []

#divided according to file suffix    
    for file in filelist:
        Olddir = os.path.join(path,file)
        if os.path.splitext(Olddir)[1] == '.png':
            png.append(Olddir)            
        elif os.path.splitext(Olddir)[1] == '.txt':
            txt.append(Olddir)
            count += 1
        else:
            print('shit!')
    print(count)
 
    for i in range(count):
        color.append(png[i*2])
#        color[i] == png[2 * i]
#        print(color)
    
    for i in range(count):
        depth.append(png[i*2+1])
#        depth[i] == png[2 * i - 1]
     
    for i in range(count):
        Newcolor = os.path.join(path,'frame-%06d.color.png'%i) 
        os.rename(color[i],Newcolor)
        Newtxt = os.path.join(path,'frame-%06d.pose.txt'%i) 
        os.rename(txt[i],Newtxt)
        Newdepth = os.path.join(path,'frame-%06d.depth.png'%i) 
        os.rename(depth[i],Newdepth)


if __name__ == "__main__":
    for i in range(3):
        pathname = '/home/chan/Desktop/neuralrgbd-master/data/datasets/7scenes/scene0191_%02d'%i
        rename(pathname)
