from bs4 import BeautifulSoup
import requests


def get_name(names):
    nameArray = []
    for name in names:
        a = name.find("a")
        nameArray.append(a.contents)
    return nameArray


def get_rank(ranks):
    rankArray = []
    for rank in ranks:
        rankArray.append(rank.get("alt"))
    return rankArray


def get_server(servers):
    serverArray = []
    for server in servers:
        small = server.find("small")
        serverArray.append(small.contents[0])
    return serverArray


def get_database(championName):
    html = requests.get(f"https://www.onetricks.gg/pt/champions/ranking/{championName}").content
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.find_all("img", class_="utils_iconBoxWhite__BU70S")
    td = soup.find_all("td", class_="name sticky-col")
    ranks = get_rank(imgs)
    names = get_name(td)
    servers = get_server(td)

    return names, ranks, servers
