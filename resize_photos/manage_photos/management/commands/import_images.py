#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from manage_photos.models import Image
from manage_photos.import_images import get_images, download_image, resize_image

__author__ = '@elinaldosoft'


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        help = 'Download imagens'
        url = options['url'][-1]
        imagens = get_images(url)

        for im in imagens:
            path = download_image(im)
            lst_imgs = resize_image(path)
            Image(uuid=im, content=lst_imgs).save()
