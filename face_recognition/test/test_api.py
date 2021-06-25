import asyncio
import unittest

from tinydb import TinyDB

from api import post_checkUser, post_registerUser
from util.db import init_db

from io import BytesIO
from PIL import Image


class TestStringMethods(unittest.TestCase):

    def test_check_user(self):
        import base64

        image = Image.open('../lukas.jpg')

        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        encoded_string = base64.b64encode(buffered.getvalue())

        asyncio.run(post_checkUser(encoded_string))

    def test_register_user(self):
        import base64

        image = Image.open('../lukas.jpg')

        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        encoded_string = base64.b64encode(buffered.getvalue())

        asyncio.run(post_registerUser(encoded_string, 'Lukas'))

    def test_init_db(self):
        assert init_db('../database/db.json') == [{'count': 7, 'type': 'apple'}, {'count': 3, 'type': 'peach'}]


if __name__ == '__main__':
    unittest.main()
