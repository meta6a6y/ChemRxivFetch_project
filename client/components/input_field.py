import tkinter as tk


class InputField(tk.Frame):
    """Компонент ввода количества статей."""

    def __init__(self, master, on_change):
        super().__init__(master)
        self.label = tk.Label(self, text="Количество статей:")
        self.label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self)
        self.entry.insert(0, "5")  # По умолчанию 5
        self.entry.pack(side=tk.LEFT)

        def handle_change(event):
            on_change(self.entry.get())

        self.entry.bind("<KeyRelease>", handle_change)