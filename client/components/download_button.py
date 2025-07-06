import tkinter as tk


class DownloadButton(tk.Frame):
    """Кнопка загрузки."""
    def __init__(self, master, on_click):
        super().__init__(master)
        self.button = tk.Button(self, text="Скачать статьи", command=lambda: on_click())
        self.button.pack()
