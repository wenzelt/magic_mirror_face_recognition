import asyncio
import unittest
from io import BytesIO

from PIL import Image

from src.api import post_check_user, post_register_user
from src.util.db import init_db


class TestStringMethods(unittest.TestCase):
    def test_compare_user(self):
        import base64

        image = Image.open("src/test/lukas.jpeg")

        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        encoded_string = base64.b64encode(buffered.getvalue())

        assert asyncio.run(post_check_user(encoded_string)) == ([0], [0.0])

    def test_register_user(self):
        import base64

        image = Image.open("src/test/lukas.jpeg")

        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        encoded_string = base64.b64encode(buffered.getvalue())
        assert asyncio.run(post_register_user(encoded_string, "Lukas")) == "success"

    def test_init_db(self):
        assert init_db("test_db.json") == [
            {"count": 7, "type": "apple"},
            {"count": 3, "type": "peach"},
        ]


if __name__ == "__main__":
    unittest.main()
