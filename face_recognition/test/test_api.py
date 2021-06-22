import asyncio
import unittest
from api import post_base64Image
from util.db import init_db


class TestStringMethods(unittest.TestCase):

    def test_upload_image(self):
        import base64

        with open("../../../FaceRecognition/lukas.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        asyncio.run(post_base64Image(encoded_string))

    def test_init_db(self):
        assert init_db('../database/db.json') == [{'count': 7, 'type': 'apple'}, {'count': 3, 'type': 'peach'}]


if __name__ == '__main__':
    unittest.main()
