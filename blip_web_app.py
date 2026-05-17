"""
BLIP Image Captioning web uygulaması.

Çalıştırma:
    python blip_web_app.py
"""

import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, FileSystemLoader

from blip_service import BlipService

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
service: BlipService | None = None


@asynccontextmanager
async def lifespan(_app: FastAPI):
    global service
    service = BlipService()
    try:
        await run_in_threadpool(service.load)
    except Exception as exc:
        service._error = str(exc)
    yield


app = FastAPI(title="BLIP Image Captioning", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

env = Environment(loader=FileSystemLoader(os.path.join(BASE_DIR, "templates")), auto_reload=False)
templates = Jinja2Templates(env=env)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="blip_index.html",
        context={"request": request}
    )


@app.get("/api/health")
async def health():
    if service is None:
        return {"ready": False, "loading": True, "error": None}
    return {
        "ready": service.ready,
        "loading": not service.ready and service.error is None,
        "error": service.error,
        "model": "Salesforce/blip-image-captioning-base",
    }


@app.post("/api/caption")
async def caption(image: UploadFile = File(...)):
    if service is None or not service.ready:
        detail = service.error if service and service.error else "Model henüz yükleniyor."
        raise HTTPException(status_code=503, detail=detail)

    if not image.content_type or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Lütfen geçerli bir görüntü dosyası yükleyin.")

    data = await image.read()
    if len(data) > 20 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Dosya boyutu 20 MB'dan küçük olmalı.")

    try:
        caption = await run_in_threadpool(service.caption_bytes, data)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return {"caption": caption}


if __name__ == "__main__":
    print("Tarayıcıda açın: http://127.0.0.1:8001")
    uvicorn.run("blip_web_app:app", host="127.0.0.1", port=8001, reload=False)
