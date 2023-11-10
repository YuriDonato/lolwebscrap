from bs4 import BeautifulSoup
import requests
import tkinter as tk


def getName(names):
    nameArray = []
    for name in names:
        a = name.find("a")
        nameArray.append(a.contents)
    return nameArray


def getRank(ranks):
    rankArray = []
    for rank in ranks:
        rankArray.append(rank.get("alt"))
    return rankArray


def getServer(servers):
    serverArray = []
    for server in servers:
        small = server.find("small")
        serverArray.append(small.contents[0])
    return serverArray


def get_data(championName):
    html = requests.get(f"https://www.onetricks.gg/pt/champions/ranking/{championName}").content
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.find_all("img", class_="utils_iconBoxWhite__BU70S")
    td = soup.find_all("td", class_="name sticky-col")
    ranks = getRank(imgs)
    names = getName(td)
    servers = getServer(td)

    return names, ranks, servers


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("LoL Top 20")

        self.champion_name_entry = tk.Entry(self)
        self.champion_name_entry.grid(row=0, column=0)

        self.get_data_button = tk.Button(self, text="Get Data", command=self.get_data)
        self.get_data_button.grid(row=0, column=1)

        self.top_20_listbox = tk.Listbox(self)
        self.top_20_listbox.pack_propagate(False)
        self.top_20_listbox.grid(row=1, column=0, columnspan=2)

        self.challenger_label = tk.Label(self, text="Challenger:")
        self.challenger_label.grid(row=2, column=0)

        self.challenger_count_label = tk.Label(self, text="")
        self.challenger_count_label.grid(row=2, column=1)

        self.master_label = tk.Label(self, text="Master:")
        self.master_label.grid(row=3, column=0)

        self.master_count_label = tk.Label(self, text="")
        self.master_count_label.grid(row=3, column=1)

        self.grandmaster_label = tk.Label(self, text="Grandmaster:")
        self.grandmaster_label.grid(row=4, column=0)

        self.grandmaster_count_label = tk.Label(self, text="")
        self.grandmaster_count_label.grid(row=4, column=1)


    def get_data(self):
        champion_name = self.champion_name_entry.get()

        names, ranks, servers = get_data(champion_name)

        self.top_20_listbox.delete(0, tk.END)
        for i, name in enumerate(names):
            self.top_20_listbox.insert(i, f"{i} - {name} - {ranks[i]} - {servers[i]}")

        challenger_count = 0
        master_count = 0
        grandmaster_count = 0

        for rank in ranks:
            rank_geral_count = challenger_count + master_count + grandmaster_count
            len_name = len(names)
            if rank_geral_count == len_name-1:
                break
            if rank == "Challenger":
                challenger_count += 1
            elif rank == "Master":
                master_count += 1
            elif rank == "Grandmaster":
                grandmaster_count += 1

        self.challenger_count_label.config(text=challenger_count)
        self.master_count_label.config(text=master_count)
        self.grandmaster_count_label.config(text=grandmaster_count)

if __name__ == "__main__":
    app = App()
    app.mainloop()