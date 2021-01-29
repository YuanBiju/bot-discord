import cv2
import numpy as np
from io import BytesIO
from PIL import Image,ImageDraw

def convert_image(img):
    image = BytesIO(img)
    image0 = Image.open(image).convert('RGB')
    open_cv_image = np.array(image0) 
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    return open_cv_image