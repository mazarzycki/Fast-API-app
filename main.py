from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from random import randint
from PIL import Image
import glob, os

app = FastAPI()

db = []

@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):

    contents = await file.read() 
    db.append(contents)
    return {"filename": file.filename}

@app.get("/images/")
async def read_random_file():

    random_index = randint(0, len(db) - 1)
    response = Response(content=db[random_index])
    return response

@app.get("/images/800x400")
async def show_image():  
    
    random_index = randint(0, len(db) - 1)
    response = Response(content=db[random_index])

#I wanted to implement this part of code taken from the Pillow library documentation to display 800x400 image.
    size = 800, 400
    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")

    return response

