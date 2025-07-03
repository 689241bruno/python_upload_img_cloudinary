import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url



cloudinary.config(
    cloud_name = "MINHA_CHAVE", 
    api_key = "MINHA_CHAVE", 
    api_secret = "MINHA_CHAVE",
    secure=True
)

result = cloudinary.uploader.upload("macawdemy.png", public_id="macawdemy", transformation=[{"width": 500, "height": 500, "crop": "fill"}])
print(result['secure_url'])