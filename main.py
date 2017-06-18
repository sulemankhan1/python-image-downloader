# Author: msuleman Ibrahim

import random
import urllib.request

def download_img():
    url = input('Please Enter the image url to Download: ')
    address = input('Address to save image (eg: d:/): ')
    name = random.randrange(1,1000)
    full_name = str(address)
    full_name += str(name) + '.jpg'

    urllib.request.urlretrieve(url,full_name)
    print('Your image is being downloaded and saved to ' + full_name)

download_img()
