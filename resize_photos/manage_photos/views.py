from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image


class ImageView(APIView):
    """
    Retrieve the list of Employee name
    """

    def get(self, request, format=None):
        images = []

        for im in Image.objects.all():
            images.append(list(im.url_images))

        return Response({'images': images})
