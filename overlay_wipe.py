from PIL import Image

with open("Tweets.txt", "w+") as f:
    f.write("")
with open("Team1.txt", "w+") as f:
    f.write("")
with open("Team2.txt", "w+") as f:
    f.write("")
for num in range(10):
    img= Image.open("transparent.png")
    img.save(f'champ{num + 1}.png')
    img.save(f'spell{2 * num + 1}.png')
    img.save(f'spell{2 * num + 2}.png')
    img.save(f'ban{num + 1}.png')
    sumname = f"Summoner{num + 1}.txt"
    with open(sumname, "w+") as f:
        f.write("")


