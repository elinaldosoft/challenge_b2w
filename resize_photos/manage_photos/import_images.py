#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import requests
import os
from django.conf import settings
import shutil
from PIL import Image

__author__ = '@elinaldosoft'

DEFAULT_FORMATS_CUT = [
    {'w': 320, 'h': 240, 'type': 'small'},
    {'w': 384, 'h': 288, 'type': 'medium'},
    {'w': 640, 'h': 480, 'type': 'large'}
]


def resize_image(name_file, formats=DEFAULT_FORMATS_CUT):
    path_image = os.path.join(settings.MEDIA_ROOT, name_file)
    lst_image = []
    path_file, ext = os.path.splitext(path_image)
    img = Image.open(path_image)

    lst_image.append({'original': name_file})

    for sizes in formats:
        width, height = sizes.get('w'), sizes.get('h')
        name_file = "_"+str(width) + "_" + str(height) + ext
        new_path = "{}{}".format(path_file, name_file)
        lst_image.append({sizes.get('type'): new_path.split('/')[-1]})
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(new_path)

    return {'images': lst_image}


def download_image(url):
    name = hashlib.md5(url.encode('utf-8')).hexdigest()
    _, ext = os.path.splitext(url)
    file_response = requests.get(url, stream=True)
    name_file = "{}{}".format(name, ext)
    path_image = os.path.join(settings.MEDIA_ROOT, name_file)

    with open(path_image, 'wb') as f:
        shutil.copyfileobj(file_response.raw, f)
    f.close()

    return name_file


def get_images(url):
    data = requests.get(url).json()
    return [url['url'] for url in data['images']]
