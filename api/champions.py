# Campeoes pela Lane
def getToplaneChampions():
    champions = [
        "Aatrox", "Akshan", "Camille", "Chogath", "Darius", "DrMundo", "Fiora", "Gangplank", "Garen", "Gnar",
        "Gwen", "Illaoi", "Irelia", "Jax", "Jayce", "Kennen", "Kled", "Ksante", "Malphite", "Maokai", "Mordekaiser",
        "Nasus", "Olaf", "Ornn", "Pantheon", "Poppy", "Quinn", "Renekton", "Riven", "Rumble", "Sett", "Shen",
        "Singed", "Sion", "Teemo", "TahmKench", "Tryndamere", "Urgot", "Volibear", "Wukong", "Yone", "Yorick"
    ]
    return champions


def getJungleChampions():
    champions = ["Amumu", "BelVeth", "Briar", "ChoGath", "Darius", "Diana", "Ekko", "Elise", "Evelynn", "Fiddlesticks",
                 "Gragas", "Graves", "Hecarim", "Ivern", "JarvanIV", "Karthus", "Kayn", "KhaZix", "Kindred", "LeeSin",
                 "Lillia", "MasterYi", "Nidalee", "Nocturne", "Nunu", "Rammus", "RekSai", "Rengar", "Sejuani", "Shaco",
                 "Shyvana", "Skarner", "Trundle", "Udyr", "Vi", "Viego", "Warwick", "XinZhao", "Zac"]
    return champions


def getMidLaneChampions():
    champions = ["Ahri", "Akali", "Anivia", "Annie", "AurelionSol", "Azir", "Brand", "Cassiopeia", "Corki", "Fizz",
                 "Galio", "Heimerdinger", "Kassadin", "Katarina", "LeBlanc", "Lissandra", "Lux", "Malzahar", "Naafiri",
                 "Neeko", "Orianna", "Qiyana", "Ryze", "Swain", "Sylas", "Syndra", "Taliyah", "Talon", "TwistedFate",
                 "Veigar", "VelKoz", "Vex", "Viktor", "Vladimir", "Xerath", "Yasuo", "Zed", "Ziggs", "Zoe"]
    return champions


def getBotlaneChampions():
    champions = ["Aphelios", "Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin", "Jinx", "Kaisa", "Kalista", "Karthus",
                 "KogMaw", "Lucian", "MissFortune", "Nilah", "Samira", "Sivir", "Tristana", "Twitch", "Varus",
                 "Vayne", "Xayah", "Zeri"]
    return champions


def getSupportChampions():
    champions = ["Alistar", "Bard", "Blitzcrank", "Braum", "Janna", "Karma", "Leona", "Lulu", "Milio", "Morgana",
                 "Nami", "Nautilus", "Rakan", "Rell", "RenataGlasc", "Senna", "Seraphine", "Sona", "Soraka", "Taric",
                 "Thresh", "Yuumi", "Zilean", "Zyra"]
    return champions


# Campeoes pela Classe
def getControllerChampions(subclass):
    if subclass == "enchanter":
        champions = ["Janna", "Karma", "Lulu", "Milio", "Nami", "RenataGlasc", "Senna", "Seraphine", "Sona", "Soraka",
                     "Taric", "Yuumi"]
    else:
        champions = ["Bard", "Blitzcrank", "Ivern", "Jhin", "Morgana", "Neeko", "Pyke", "Rakan", "Thresh", "Zyra"]
    return champions


def getFighterChampions(subclass):
    if subclass == "divers":
        champions = ["Briar", "Camille", "Diana", "Elise", "Hecarim", "Irelia", "JarvanIV", "LeeSin", "Olaf",
                     "Pantheon", "RekSai", "Renekton", "Rengar", "Skarner", "Vi", "Warwick", "Wukong", "XinZhao"]
    else:
        champions = ["Aatrox", "Darius", "DrMundo", "Garen", "Illaoi", "Mordekaiser", "Nasus", "Sett", "Shyvana",
                     "Trundle", "Udyr", "Urgot", "Volibear", "Yorick"]
    return champions


def getMageChampions(subclass):
    if subclass == "artillery":
        champions = ["Jayce", "Lux", "Varus", "VelKoz", "Xerath", "Ziggs"]
    elif subclass == "battlemages":
        champions = ["Anivia", "AurelionSol", "Cassiopeia", "Karthus", "Malzahar", "Rumble", "Ryze", "Swain",
                     "Taliyah", "Viktor", "Vladimir"]
    else:
        champions = ["Ahri", "Annie", "Brand", "Karma", "LeBlanc", "Lissandra", "Lux", "Neeko", "Orianna", "Seraphine",
                     "Sylas", "Syndra", "Twisted Fate", "Veigar", "Vex", "Zoe"]
    return champions


def getMarksmanChampions():
    champions = ["Akshan", "Aphelios", "Ashe", "Caitlyn", "Corki", "Draven", "Ezreal", "Jhin", "Jinx", "KaiSa",
                 "Kalista", "Kindred", "KogMaw", "Lucian", "Miss Fortune", "Samira", "Senna", "Sivir", "Tristana",
                 "Twitch", "Varus", "Vayne", "Xayah", "Zeri"]
    return champions


def getSlayerChampions(subclass):
    if subclass == "assassins":
        champions = ["Akali", "Akshan", "Diana", "Ekko", "Evelynn", "Fizz", "Kassadin", "Katarina", "KhaZix",
                     "Naafiri", "Nocturne", "Pyke", "Qiyana", "Rengar", "Shaco", "Talon", "Yone", "Zed"]
    else:
        champions = ["BelVeth", "Fiora", "Gwen", "Jax", "KSante", "Kayn", "Kled", "Lillia", "MasterYi", "Nilah",
                     "Riven", "Sylas", "Tryndamere", "Viego", "Yasuo", "Yone"]
    return champions


def getTankChampions(subclass):
    if subclass == "vanguard":
        champions = ["Alistar", "Amumu", "Gragas", "Leona", "Malphite", "Maokai", "Nautilus", "Nunu", "Ornn", "Rammus",
                     "Rell", "Sejuani", "Sion", "Zac"]
    else:
        champions = ["Braum", "Galio", "KSante", "Poppy", "Shen", "TahmKench", "Taric"]
    return champions


def getSpecialistChampions():
    champions = ["Azir", "ChoGath", "Fiddlesticks", "Gangplank", "Gnar", "Graves", "Heimerdinger", "Kayle", "Kennen",
                 "Nidalee", "Quinn", "Singed", "Teemo", "Zilean"]
    return champions
