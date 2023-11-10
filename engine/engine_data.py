# Scrapping
from api import get_database

# Lista Campeoes por Role
from api import getToplaneChampions
from api import getJungleChampions
from api import getMidLaneChampions
from api import getBotlaneChampions
from api import getSupportChampions

# Lista Campeoes por Classe
from api import getControllerChampions
from api import getFighterChampions
from api import getMageChampions
from api import getMarksmanChampions
from api import getSlayerChampions
from api import getTankChampions
from api import getSpecialistChampions

def getRoleData(role):
    championData = {}
    championsName = []
    if role == "top":
        championsName = getToplaneChampions()
    elif role == "jg":
        championsName = getJungleChampions()
    elif role == "mid":
        championsName = getMidLaneChampions()
    elif role == "adc":
        championsName = getBotlaneChampions()
    elif role == "sup":
        championsName = getSupportChampions()
    for champion in championsName:
        names, ranks, servers = get_database(champion)
        championData[champion] = {"names": names, "ranks": ranks, "servers": servers}
    return championData, championsName


def getClassData(classname, subclass="hold"):
    championData = {}
    championsName = []
    if classname == "controller":
        championsName = getControllerChampions(subclass)
    elif classname == "fighter":
        championsName = getFighterChampions(subclass)
    elif classname == "mage":
        championsName = getMageChampions(subclass)
    elif classname == "marksman":
        championsName = getMarksmanChampions()
    elif classname == "slayer":
        championsName = getSlayerChampions(subclass)
    elif classname == "tank":
        championsName = getTankChampions(subclass)
    elif classname == "specialist":
        championsName = getSpecialistChampions()
    for champion in championsName:
        names, ranks, servers = get_database(champion)
        championData[champion] = {"names": names, "ranks": ranks, "servers": servers}
    return championData, championsName
