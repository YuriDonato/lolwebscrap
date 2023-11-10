import customtkinter as tk
from engine import retrieveData


class Page1(tk.CTkFrame):
    def __init__(self, master):
        tk.CTkFrame.__init__(self, master)

        self.champion_list = tk.CTkScrollableFrame(master=self)
        self.champion_list.pack(fill=tk.BOTH, expand=True)

        championData, championName = retrieveData("top")


        for champion in championName:


            champion_frame = tk.CTkFrame(self.champion_list)
            champion_frame.pack(padx=10, pady=10)

            pontuacao_total = championData[champion]['points']['totalPoints']

            champion_label = tk.CTkLabel(champion_frame, text=f"Campeão: {champion}")
            champion_label.pack()

            # Labels com detalhes do campeão
            # Substitua os valores fictícios pelos valores reais obtidos em get_data()
            placement_label = tk.CTkLabel(champion_frame, text=f"Colocação: {pontuacao_total}")
            placement_label.pack()

            challengers_label = tk.CTkLabel(champion_frame, text="Número de Challengers: 2")
            challengers_label.pack()

            grandmasters_label = tk.CTkLabel(champion_frame, text="Número de Grandmasters: 10")
            grandmasters_label.pack()

            masters_label = tk.CTkLabel(champion_frame, text="Número de Masters: 15")
            masters_label.pack()

            total_score_label = tk.CTkLabel(champion_frame, text=f"Pontuação total: {pontuacao_total}")
            total_score_label.pack()

            # Botão para a página específica do campeão
            champion_button = tk.CTkButton(champion_frame, text="Detalhes do Campeão", command=lambda name=champion: self.show_champion_details(name))
            champion_button.pack()

    def show_champion_details(self, champion_name):
        # Adicione a lógica para mostrar os detalhes específicos do campeão
        print(f"Detalhes do campeão {champion_name}")


if __name__ == "__main__":
    root = tk.CTk()
    root.geometry("600x400")
    root.title("Toplane Champions")
    page1 = Page1(root)
    page1.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
