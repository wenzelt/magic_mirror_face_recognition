import base64
import os
from tempfile import NamedTemporaryFile
from typing import List

from fastapi import FastAPI, HTTPException

import numpy as np
from PIL import Image
from fastapi import FastAPI
from numpy import asarray
from tinydb import TinyDB, Query

from face import get_persons_from_frame
from fastapi import FastAPI, File, UploadFile, Form

from util.db import query_db_for_encodings, init_db

app = FastAPI()


@app.post("/uploadbase64")
async def post_base64Image(base64_bytes: bytes):
    try:
        img_data = base64.encodebytes(base64_bytes)
        np_image_array = np.fromstring(img_data, np.uint8)

        path_to_db = 'database/production.json'
        production_db = TinyDB(path_to_db)
        encoding_query = Query()

        get_persons_from_frame(np_image_array, list_of_known_encodings)
    except HTTPException:
        raise HTTPException(status_code=420, detail="Issue posting")

    return "success"
