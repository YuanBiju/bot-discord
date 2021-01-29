import cv2
import numpy as np
from template_mixer import mixer_output

def meme_output(meme_key,member_url,mention_url):
    meme = mixer_output(meme_key,member_url,mention_url)
    return meme

