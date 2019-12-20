# Adds noise into an image and applies Gaussian Filtering
import cv2  # install opencv-python package, not cv2
import numpy as np

img = cv2.imread(r'/Users/puaqieshang/Desktop/insta.jpeg') # Reads image from local disk

dst = np.empty_like(img) #create empty array the size of the image
noise = cv2.randn(img, (0,0,0), (1,1,1)) #add random img noise

# Pass img through noise filter to add noise
# alpha, beta and gamma adjusts the contrasts??
img_noise = cv2.addWeighted(dst, 0.75, noise, 0.75, 60)

# Blurring function; kernel and sigma is up to user's preference
img_final = cv2.GaussianBlur(img_noise, (21, 21), 9)

cv2.imshow('Img', img_final)

k = cv2.waitKey(0) & 0xFF
if k == 27:  # Enter ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # Enter 's' key to save and exit
    cv2.imwrite('test.png', img_final.astype(np.uint8))
    # Python saves images in uint32 or uint64, so need to typecast it to uint8
    cv2.destroyAllWindows()

