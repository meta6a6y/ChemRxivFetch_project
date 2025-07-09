import tkinter as tk
from ..styles import PRIMARY_COLOR, TEXT_COLOR, FONT


class DownloadButton(tk.Frame):
    """Styled download button matching app design."""

    def __init__(self, master, on_click):
        super().__init__(master, bg=master["bg"])

        self.button = tk.Label(
            self,
            text="Download articles",
            bg=master["bg"],
            fg=TEXT_COLOR,
            padx=10,
            pady=5,
            font=FONT
        )
        self.button.pack(expand=True, fill="both")

        self.config(
            highlightbackground=TEXT_COLOR,
            highlightthickness=1,
            bd=0
        )

        self.button.bind("<Button-1>", lambda e: on_click())
        self.button.bind("<Enter>", self.on_hover)
        self.button.bind("<Leave>", self.on_leave)
        self.configure_cursor()

    def configure_cursor(self):
        self.button.config(cursor="hand2")

    def on_hover(self, event):
        self.config(bg=PRIMARY_COLOR)
        self.button.config(bg=PRIMARY_COLOR)

    def on_leave(self, event):
        self.config(bg=self.master["bg"])
        self.button.config(bg=self.master["bg"])
