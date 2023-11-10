from engine import getClassData, getRoleData


def calculatePoints(ranks, size):
    totalPoints = 0
    challengerCount = 0
    grandmasterCount = 0
    masterCount = 0

    for rank in ranks:
        if challengerCount + grandmasterCount + masterCount >= size:
            break
        if rank == "Challenger":
            challengerCount += 1
        elif rank == "Grandmaster":
            grandmasterCount += 1
        elif rank == "Master":
            masterCount += 1
        totalPoints = (challengerCount * 3) + (grandmasterCount * 2) + masterCount
    return totalPoints, challengerCount, grandmasterCount, masterCount

def updatePoints(championData, championName):
    for i, champion in enumerate(championData):
        championDaVez = championName[i]
        totalPoints, challengerPointsCount, grandmasterPointsCount, masterPointsCount = calculatePoints(
            championData[championDaVez]['ranks'], len(championData[championDaVez]['names']))
        #Adicionar pontos ao campeao
        championData[championDaVez]['points'] = {}
        championData[championDaVez]['points']['totalPoints'] = totalPoints
        championData[championDaVez]['points']['challengerPointsCount'] = challengerPointsCount
        championData[championDaVez]['points']['grandmasterPointsCount'] = grandmasterPointsCount
        championData[championDaVez]['points']['masterPointsCount'] = masterPointsCount



def retrieveData(role="a", classname="a"):
    championData = []
    championName = []
    if len(role) >= 2:
        championData, championName = getRoleData(role)
    elif len(classname) >= 2:
        championData, championName = getRoleData(role)
    # print(f"to no retrieve, com champion data: {championData['Aatrox']['ranks']}")
    updatePoints(championData,championName)

    return championData, championName

if __name__ == "__main__":
    retrieveData("adc")
