import cv2
import requests
import shutil


def addSummonerSpell(spell, slot):
    image_url = (
        f"http://ddragon.leagueoflegends.com/cdn/10.22.1/img/spell/{spell}.png"
    )

    #filename = image_url.split("/")[-1]
    filename = f"spell{str(slot)}.png"
    #print(filename)

    r= requests.get(image_url, stream =True)

    if r.status_code ==200:
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        #print('Image successfully downloaded: {}'.format(filename))
    else:
        print("Image could\n't be retrieved")

    image = cv2.imread(filename)
    resized_image = cv2.resize(image, (40, 40))
    cv2.imwrite(filename, resized_image)
    cv2.waitKey(0)
