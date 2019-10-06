import numpy as np
import cv2
import matplotlib.pyplot as plt
import PIL.Image as Image

def cv_circle():
    img_white = np.ones((256,384,3))
    u,v=img_white.shape[:2]
    img_circle = cv2.circle(img_white,(int(v/2),int(u/2)),128,(255,0,0),2)
    print(np.max(img_circle))
    plt.imsave('circle', img_circle)
    
def numpy_circle(center):
    img_white = np.zeros((256,384))
    u,v=img_white.shape[:2]
    for i in range(u):
        for j in range(v):
            radius = np.linalg.norm([i-u/2, j-v/2])
            if radius <= center:
                img_white[i][j] = 1
    plt.imsave('circle.png', img_white)
    img_white = Image.fromarray(img_white).convert('I')
    img_white.save('circle.pgm')

if __name__ == '__main__':
    cv_circle()
    numpy_circle(center = 120)