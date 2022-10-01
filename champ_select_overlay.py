import requests
import shutil
import cv2



def fullCSTest():
    id = 266
    # somewhere here relate champ id to champ name, in this case Nami
    champions = ["Shen", "Graves", "Syndra", "Samira", "Leona", "Ornn", "Hecarim", "Galio", "Ezreal", "Yuumi"]
    num = 0
    for cs_slot_num, champion in enumerate(champions, start=1):
        addChampPick(champion, 0, cs_slot_num)

def addChampPick(champion, skinID, slot):
    print(f'attempting to update with {champion}')
    image_url = f"http://ddragon.leagueoflegends.com/cdn/img/champion/loading/{champion}_0.jpg"

    print(image_url)
    # filename = image_url.split("/")[-1]
    filename = f"champ{str(slot)}.png"
    print(filename)

    r = requests.get(image_url, stream=True)

    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print(f'Image successfully downloaded: {filename}')
    else:
        print("Image could\n't be retrieved")

    image = cv2.imread(filename)
    resized_image = cv2.resize(image, (160, 291))
    cv2.imwrite(filename, resized_image)
    cv2.waitKey(0)

def addChampBan(champion, slot):
    #print('attempting to update with ' + champion)
    image_url = f"http://ddragon.leagueoflegends.com/cdn/10.22.1/img/champion/{champion}.png"

    #print(image_url)
    # filename = image_url.split("/")[-1]
    filename = f"ban{str(slot)}.png"
    #print(filename)

    r = requests.get(image_url, stream=True)

    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        #print('Image successfully downloaded: {}'.format(filename))
    else:
        print("Image could\n't be retrieved")

    image = cv2.imread(filename)
    resized_image = cv2.resize(image, (80, 80))
    cv2.imwrite(filename, resized_image)
    cv2.waitKey(0)

if __name__ == '__main__':
    fullCSTest()
