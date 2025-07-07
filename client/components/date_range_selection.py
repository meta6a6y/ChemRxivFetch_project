import tkinter as tk
from ..styles import PRIMARY_COLOR, TEXT_COLOR


class DateRangeSelection(tk.Frame):
    """Компонент выбора диапазона дат."""

    def __init__(self, master, options, on_change):
        super().__init__(master, bd=0, relief="solid", bg=master["bg"])

        label = tk.Label(self, text="Выберите диапазон дат:", bg=master["bg"], fg=TEXT_COLOR, pady=5)
        label.pack(anchor="w", pady=5)

        self.var = tk.StringVar()
        self.var.set(options[0])

        self.radio_buttons = []
        for opt in options:
            rb = tk.Radiobutton(
                self,
                text=opt,
                variable=self.var,
                value=opt,
                command=self._notify_change,
                bg=self["bg"],
                fg=TEXT_COLOR,
                selectcolor="#26292D",
                activebackground=PRIMARY_COLOR,
                activeforeground=TEXT_COLOR,
                padx=10,
                pady=5
            )
            rb.pack(anchor="w", padx=5, pady=2)
            self.radio_buttons.append(rb)

        self.on_change = on_change

    def _notify_change(self):
        self.on_change(self.var.get())
