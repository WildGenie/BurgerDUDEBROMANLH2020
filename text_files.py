# num = 1
# sumname = "Summoner{}.txt".format(num)

def addSummonerNameFile(name, slot):
    for _ in range(10):
        sumname = f"Summoner{slot + 1}.txt"
        f = open(sumname, "w+")
        f.write(name)


