import asyncio
import unittest
from io import BytesIO

from PIL import Image

from src.api import post_check_user, post_register_user
from src.util.db import init_db


class TestStringMethods(unittest.TestCase):
    def test_check_user(self):
        import base64

        image = Image.open("../lukas.jpg")

        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        encoded_string = base64.b64encode(buffered.getvalue())

        asyncio.run(post_check_user(encoded_string))

    def test_register_user(self):
        import base64

        image = Image.open("../lukas.jpg")

        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        encoded_string = base64.b64encode(buffered.getvalue())

        asyncio.run(post_register_user(encoded_string, "Lukas"))

    def test_init_db(self):
        assert init_db("test_db.json") == [
            {"count": 7, "type": "apple"},
            {"count": 3, "type": "peach"},
        ]


if __name__ == "__main__":
    unittest.main()