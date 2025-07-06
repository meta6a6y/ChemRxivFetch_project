import tkinter as tk


class DateRangeSelection(tk.Frame):
    """Компонент выбора диапазона дат (только один вариант)."""
    def __init__(self, master, options, on_change):
        super().__init__(master)
        tk.Label(self, text="Выберите диапазон дат:").pack(anchor="w")
        self.var = tk.StringVar()
        self.var.set(options[0])

        for opt in options:
            rb = tk.Radiobutton(self, text=opt, variable=self.var, value=opt, command=self._notify_change)
            rb.pack(anchor="w")

        self.on_change = on_change

    def _notify_change(self):
        self.on_change(self.var.get())
