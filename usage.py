import requests

base_url = "http://localhost"

meme_image_url = requests.post(f"{base_url}/generate-meme", data={})
