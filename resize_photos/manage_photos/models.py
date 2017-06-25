from django_mongoengine import Document
from django_mongoengine import fields
from django.conf import settings
import datetime
import os


class Image(Document):
    uuid = fields.StringField(max_length=255, primary_key=True)
    content = fields.DictField(verbose_name="Imagens")
    created_at = fields.DateTimeField(default=datetime.datetime.now, editable=False)

    @property
    def url_images(self):
        for im in self.content['images']:
            url = list(im.values())[0]
            yield os.path.join(settings.MEDIA_URL, url)
