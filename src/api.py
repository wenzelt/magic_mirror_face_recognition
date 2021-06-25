import base64
from io import BytesIO

import numpy as np
from PIL import Image
from fastapi import FastAPI
from fastapi import HTTPException
from tinydb import TinyDB

from src.face.face import get_face_encodings, get_persons_from_frame

app = FastAPI()


@app.post("/register_user")
async def post_register_user(base64_bytes: bytes, name: str):
  try:
    img_data = Image.open(BytesIO(base64.b64decode(base64_bytes)))

    np_image_array = np.asarray(img_data)

    # Assume there only is one person on the image
    face_encodings = get_face_encodings(np_image_array)[0].tolist()

    path_to_db = 'database/db.json'
    db = TinyDB(path_to_db)
    db.insert({'name': 'Lukas', 'encoding': face_encodings})
    db.close()

  except HTTPException:
    raise HTTPException(status_code=420, detail="Issue posting")

  return "success"


@app.post("/check_user")
async def post_check_user(base64_bytes: bytes):
  try:
    img_data = Image.open(BytesIO(base64.b64decode(base64_bytes)))

    np_image_array = np.asarray(img_data)

    path_to_db = 'database/db.json'

    db = TinyDB(path_to_db)
    list_of_known_encodings = [r['encoding'] for r in db.all()]
    db.close()

    res = get_persons_from_frame(np_image_array, list_of_known_encodings)
  except HTTPException:
    raise HTTPException(status_code=420, detail="Issue posting")

  return res
