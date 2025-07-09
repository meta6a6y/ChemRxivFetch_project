import tkinter as tk
from ..styles import PRIMARY_COLOR, TEXT_COLOR, FONT


class DateTile(tk.Frame):
    """One tile to select a date range."""
    def __init__(self, master, text, on_toggle):
        super().__init__(master, bd=1, relief="solid", bg=master["bg"])

        self.text = text
        self.on_toggle = on_toggle
        self.selected = False

        self.label = tk.Label(self, text=text, bg=master["bg"], fg=TEXT_COLOR, padx=10, pady=5, font=FONT)
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


class DateRangeSelection(tk.Frame):
    """Tile date range selection component allowing multiple selections."""
    def __init__(self, master, options, on_change):
        super().__init__(master, bg=master["bg"])

        self.selected_dates = set()
        self.on_change = on_change
        self.label = tk.Label(self, text="Date range selected:", bg=master["bg"], fg=TEXT_COLOR, font=FONT)
        self.label.pack(anchor="w", pady=5)
        self.error_state = False

        grid_frame = tk.Frame(self, bg=master["bg"])
        grid_frame.pack()

        columns = 2
        for index, date_option in enumerate(options):
            tile = DateTile(grid_frame, date_option, self.handle_toggle)
            tile.grid(row=index // columns, column=index % columns, padx=5, pady=5, sticky="nsew")

    def handle_toggle(self, date_option, is_selected):
        if is_selected:
            self.selected_dates.add(date_option)
        else:
            self.selected_dates.discard(date_option)
        self.on_change(list(self.selected_dates))

    def set_error_state(self):
        if not self.error_state:
            self.error_state = True
            self.label.config(fg="red")

    def set_normal_state(self):
        if self.error_state:
            self.error_state = False
            self.label.config(fg=TEXT_COLOR)

    def has_selection(self):
        return len(self.selected_dates) > 0
