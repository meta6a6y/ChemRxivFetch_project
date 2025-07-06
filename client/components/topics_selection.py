import tkinter as tk
from ..styles import PRIMARY_COLOR, TEXT_COLOR


class TopicTile(tk.Frame):
    """Одна плитка для выбора темы."""
    def __init__(self, master, text, on_toggle):
        super().__init__(master, bd=1, relief="solid", bg=master["bg"])
        self.text = text
        self.on_toggle = on_toggle
        self.selected = False

        self.label = tk.Label(self, text=text, bg=master["bg"], fg=TEXT_COLOR, padx=10, pady=5)
        self.label.pack(expand=True, fill="both")

        self.config(highlightbackground=TEXT_COLOR, highlightthickness=1, bd=0)
        self.label.bind("<Button-1>", self.toggle)

        self.configure_cursor()

    def configure_cursor(self):
        self.label.config(cursor="hand2")

    def toggle(self, event):
        self.selected = not self.selected
        if self.selected:
            self.config(bg=PRIMARY_COLOR)
            self.label.config(bg=PRIMARY_COLOR)
        else:
            self.config(bg=self.master["bg"])
            self.label.config(bg=self.master["bg"])
        self.on_toggle(self.text, self.selected)


class TopicsSelection(tk.Frame):
    """Компонент выбора тем плитками."""
    def __init__(self, master, options, on_change):
        super().__init__(master, bg=master["bg"])
        tk.Label(self, text="Выберите темы:", bg=master["bg"], fg=TEXT_COLOR).pack(anchor="w", pady=5)

        self.selected_topics = set()
        self.on_change = on_change

        grid_frame = tk.Frame(self, bg=master["bg"])
        grid_frame.pack()

        columns = 2
        for index, topic in enumerate(options):
            tile = TopicTile(grid_frame, topic, self.handle_toggle)
            tile.grid(row=index // columns, column=index % columns, padx=5, pady=5, sticky="nsew")

    def handle_toggle(self, topic, is_selected):
        if is_selected:
            self.selected_topics.add(topic)
        else:
            self.selected_topics.discard(topic)
        self.on_change(list(self.selected_topics))
