import base64
import os
from io import BytesIO
from tempfile import NamedTemporaryFile
from typing import List

from fastapi import FastAPI, HTTPException

import numpy as np
from PIL import Image
from fastapi import FastAPI
from numpy import asarray
from tinydb import TinyDB, Query
from face import get_face_encodings

from face import get_persons_from_frame
from fastapi import FastAPI, File, UploadFile, Form

from util.db import query_db_for_encodings, init_db

app = FastAPI()

@app.post("/registersUser")
async def post_registerUser(base64_bytes: bytes, name: str):
    try:
        img_data = Image.open(BytesIO(base64.b64decode(base64_bytes)))

        np_image_array = np.asarray(img_data)

        # Assume there only is one person on the image
        face_encodings = get_face_encodings(np_image_array)[0].tolist()

        path_to_db = '../database/db.json'
        db = TinyDB(path_to_db)
        db.insert({'name': 'Lukas', 'encoding': face_encodings})
        db.close()

    except HTTPException:
        raise HTTPException(status_code=420, detail="Issue posting")

    return "success"

@app.post("/uploadbase64")
async def post_checkUser(base64_bytes: bytes):
    try:
        img_data = Image.open(BytesIO(base64.b64decode(base64_bytes)))

        np_image_array = np.asarray(img_data)

        path_to_db = '../database/db.json'

        db = TinyDB(path_to_db)
        list_of_known_encodings = [r['encoding'] for r in db.all()]
        db.close()

        res = get_persons_from_frame(np_image_array, list_of_known_encodings)
    except HTTPException:
        raise HTTPException(status_code=420, detail="Issue posting")

    return res
