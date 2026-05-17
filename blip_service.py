"""
Salesforce BLIP Image Captioning Base servisi.

Kullanım:
    service = BlipService()
    service.load()
    caption = service.caption_bytes(image_bytes)
"""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
from typing import Optional

import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from deep_translator import GoogleTranslator


class BlipService:
    def __init__(self, device: Optional[str] = None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.processor: Optional[BlipProcessor] = None
        self.model: Optional[BlipForConditionalGeneration] = None
        self.ready = False
        self.error: Optional[str] = None

    def load(self) -> None:
        try:
            print(f"BLIP modeli yükleniyor... (Device: {self.device})")
            self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
            self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
            self.model.to(self.device)
            self.model.eval()
            self.ready = True
            print("BLIP modeli başarıyla yüklendi.")
        except Exception as exc:
            self.error = str(exc)
            raise

    def caption_bytes(self, image_bytes: bytes, translate_to_turkish: bool = True) -> str:
        if not self.ready:
            raise RuntimeError("Model henüz yüklenmedi.")

        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        
        inputs = self.processor(image, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            out = self.model.generate(**inputs, max_length=100, num_beams=5, early_stopping=True)
        
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        
        if translate_to_turkish:
            try:
                translator = GoogleTranslator(source='auto', target='tr')
                caption = translator.translate(caption)
            except Exception:
                pass
        
        return caption

    def caption_path(self, image_path: Path) -> str:
        image_bytes = image_path.read_bytes()
        return self.caption_bytes(image_bytes)
