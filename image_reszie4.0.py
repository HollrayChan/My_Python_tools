from PIL import Image
import os

def recrop(path, size):
    count = 0
    images = []
    
    folder_name = 'recrop_basler'
    temp_path = os.path.join(path, folder_name)
 
    try:
        os.mkdir(temp_path)
    except OSError:
        pass
    
    filelist = os.listdir(path) #get names of file and subfile 
    filelist.sort() #the names of files will be sorted by file order
    for file in filelist:
        Olddir = os.path.join(path,file)
        if os.path.splitext(Olddir)[1] == '.bmp':
            images.append(Olddir)
            count += 1
    
    for i in range(count):
        img = Image.open(images[i])
        cropped = img.crop((163, 150, 1238, 956))
        newpath = os.path.join(path, folder_name ,'recrop_%d.bmp'%i)
        cropped.save(newpath)
    return print('%i images have recrop totally' %count)

def resize(path, size):
    count = 0
    images = []
    
    folder_name = 'resize_HIK'
    temp_path = os.path.join(path, folder_name)
 
    try:
        os.mkdir(temp_path)
    except OSError:
        pass
    
    filelist = os.listdir(path) #get names of file and subfile 
    filelist.sort() #the names of files will be sorted by file order
    for file in filelist:
        Olddir = os.path.join(path,file)
        if os.path.splitext(Olddir)[1] == '.bmp':
            images.append(Olddir)
            count += 1
    
    for i in range(count):
        img = Image.open(images[i])
        (x, y) = img.size
        out = img.resize((int(x*size), int(y*size)), Image.ANTIALIAS)
        newpath = os.path.join(path, folder_name, 'resize_%d.bmp'%i)
        out.save(newpath)
    return print('%i images have resize totally' %count)



if __name__ == '__main__':
    size = 1075/2592
    recrop_path = r'C:\Users\Administrator.USER-20190423VA\Desktop\image\test_backup\1\L'
    resize_path = r'C:\Users\Administrator.USER-20190423VA\Desktop\image\test_backup\1\R'
    recrop(recrop_path, size)
    resize(resize_path, size)
    

