import cv2
from numba import jit
import os
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_ascii_img(img):
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #转换了灰度化

    height, width = im_gray.shape
    if height > 60 or width > 60: 
        im_gray = cv2.resize(im_gray, (width * 60 // height, 60))
        height, width = im_gray.shape
    ascii_img = ""
    for i in range(height):
        for j in range(width):
            ascii_img += ascii_char[im_gray[i][j]//len(ascii_char)]
        ascii_img += "\n"
    ascii_img += "\n"
    return ascii_img

if __name__ == "__main__":
    cap = cv2.VideoCapture("./van.Flv")
    while(cap.isOpened()):
        ret, frame = cap.read()
        # show a frame
        print(get_ascii_img(frame))
        os.popen("clear")
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows() 
