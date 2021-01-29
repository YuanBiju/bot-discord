import requests

def img_request(img_url):
    byte_image = requests.get(img_url)
    return byte_image.content

