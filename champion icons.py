import requests
import shutil

champion = "Yasuo"

image_url = f"http://ddragon.leagueoflegends.com/cdn/10.22.1/img/champion/{champion}.png"

filename = image_url.split("/")[-1]
# print(filename)

r= requests.get(image_url, stream =True)

if r.status_code ==200:
    r.raw.decode_content = True
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    print(f'Image successfully downloaded: {filename}')
else:
    print("Image could\n't be retrieved")
