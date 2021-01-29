import cv2
import os
import numpy as np
from .image_request import img_request
from .image_converter import convert_image
import json

def mixer_output(key,member_url,mention_url):
    #reading json file for template points
    with open('data/meme_template.json','r') as read_file:
        data = json.load(read_file)
        r1 = data[key]['pos1']
        r2 = data[key]['pos2']
        r3 = data[key]['pos3']
        r4 = data[key]['pos4']
    
    #author's image
    member_byte_image = img_request(member_url)
    member_avatar_img = convert_image(member_byte_image)
    member_avatar_img = cv2.resize(member_avatar_img, (data[key]["avatars"]["size"]["avatar1"], data[key]["avatars"]["size"]["avatar2"]))
    
    image_file = data[key]['file_name']
    meme_template = cv2.imread('imgs/'+image_file,1)

    #member image mixing
    rows,cols,channels = member_avatar_img.shape
    roi = meme_template[r2:r2+rows,r1:r1+cols]

    member_avatar_img2gray = cv2.cvtColor(member_avatar_img,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(member_avatar_img2gray,-100,255,cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    meme_template_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

    avatar_img_fg = cv2.bitwise_and(member_avatar_img,member_avatar_img,mask=mask)

    dst = cv2.add(meme_template_bg,avatar_img_fg)
    meme_template[r2:r2+rows,r1:r1+cols] = dst

    os.chdir(r"C:\Users\home\Documents\Projects\Discord\PringlesBot\imgs_temp")
    cv2.imwrite(image_file, meme_template)
    os.chdir(r"C:\Users\home\Documents\Projects\Discord\PringlesBot")

    #mention's image
    if mention_url:
        mention_byte_image = img_request(mention_url)
        mention_avatar_img = convert_image(mention_byte_image)
        mention_avatar_img = cv2.resize(mention_avatar_img, (data[key]["avatars"]["size"]["avatar1"], data[key]["avatars"]["size"]["avatar2"]))
    #mention image mixing
    if mention_url:
        meme_template = cv2.imread('imgs_temp/'+image_file,1)
        rows,cols,channels = mention_avatar_img.shape
        print(rows,cols)
        roi = meme_template[r4:r4+rows,r3:r3+cols]

        mention_avatar_img2gray = cv2.cvtColor(mention_avatar_img,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(mention_avatar_img2gray,-100,255,cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        meme_template_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

        avatar_img_fg = cv2.bitwise_and(mention_avatar_img,mention_avatar_img,mask=mask)

        dst = cv2.add(meme_template_bg,avatar_img_fg)
        meme_template[r4:r4+rows,r3:r3+cols] = dst

        os.chdir(r"C:\Users\home\Documents\Projects\Discord\PringlesBot\imgs_temp")
        cv2.imwrite(image_file, meme_template)
        os.chdir(r"C:\Users\home\Documents\Projects\Discord\PringlesBot")

    '''cv2.imshow('image',meme_template)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    
    return meme_template
