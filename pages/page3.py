import customtkinter as tk


class Page3(tk.CTkFrame):
    def __init__(self, parent):
        tk.CTkFrame.__init__(self, parent)

        label = tk.CTkLabel(self, text="Página 1")
        label.pack(padx=10, pady=10)

        # Adicione os elementos e lógica específicos para a página 1

        # Exemplo: Botão na página 1
        button = tk.CTkButton(self, text="Botão na Página 3")
        button.pack()
