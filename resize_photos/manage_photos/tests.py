from rest_framework.test import APITestCase
from .import_images import get_images, download_image, resize_image
from .models import Image


class TestImportImages(APITestCase):

    def setUp(self):
        self.data_images = ["http://54.152.221.29/images/b737_5.jpg", "http://54.152.221.29/images/b777_5.jpg",
                            "http://54.152.221.29/images/b737_3.jpg", "http://54.152.221.29/images/b777_4.jpg",
                            "http://54.152.221.29/images/b777_3.jpg", "http://54.152.221.29/images/b737_2.jpg",
                            "http://54.152.221.29/images/b777_2.jpg", "http://54.152.221.29/images/b777_1.jpg",
                            "http://54.152.221.29/images/b737_4.jpg", "http://54.152.221.29/images/b737_1.jpg"]

    def test_get_images(self):
        self.assertEqual(self.data_images, get_images('http://54.152.221.29/images.json'))

    def test_download_image(self):
        self.assertEqual('2a30975741c39d210b184ccb479c9040.jpg', download_image("http://54.152.221.29/images/b737_5.jpg"))

    def test_resize_image(self):
        self.assertEqual({'images': [
            {'original': '2a30975741c39d210b184ccb479c9040.jpg'},
            {'small': '2a30975741c39d210b184ccb479c9040_320_240.jpg'},
            {'medium': '2a30975741c39d210b184ccb479c9040_384_288.jpg'},
            {'large': '2a30975741c39d210b184ccb479c9040_640_480.jpg'}]},
            resize_image('2a30975741c39d210b184ccb479c9040.jpg'))

    def test_save(self):
        data = {'images':[
            {'original': '2a30975741c39d210b184ccb479c9040.jpg'},
            {'small': '2a30975741c39d210b184ccb479c9040_320_240.jpg'},
            {'medium': '2a30975741c39d210b184ccb479c9040_384_288.jpg'},
            {'large': '2a30975741c39d210b184ccb479c9040_640_480.jpg'}]}
        Image(uuid="teste", content=data).save()

        img = Image.objects.get(uuid="teste")
        self.assertEqual(data, img.content)

    def test_lst_images(self):
        images = Image.objects.all()
        self.assertTrue(images)
