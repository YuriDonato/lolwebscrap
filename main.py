import customtkinter as tk
from pages import *


class MainApplication(tk.CTk):
    def __init__(self):
        tk.CTk.__init__(self)
        self.title("MonoChampion App")
        self.geometry("600x400")

        tk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        tk.set_default_color_theme("green")

        self.sidebar = tk.CTkFrame(self, width=100)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        self.pages = {
            "Main Page": MainPage(self),
            "Top Laner": Page1(self),
            "Jungler": Page2(self),
            "Mid Laner": Page3(self),
            "Bot Laner": Page4(self),
            "Support": Page5(self)
        }

        self.current_page = None
        self.change_page("Main Page")

        for page_name in self.pages:
            button = tk.CTkButton(
                self.sidebar, text=page_name, command=lambda name=page_name: self.change_page(name)
            )
            button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    def change_page(self, page_name):
        new_page = self.pages[page_name]
        if self.current_page is not None:
            self.current_page.pack_forget()
        self.current_page = new_page
        self.current_page.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
