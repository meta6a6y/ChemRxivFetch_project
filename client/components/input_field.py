import tkinter as tk
from ..styles import PRIMARY_COLOR, TEXT_COLOR, FONT


class InputField(tk.Frame):
    """Styled input field for specifying number of articles to download."""

    def __init__(self, master, on_change):
        super().__init__(master, bg=master["bg"])

        label = tk.Label(
            self,
            text="Number of articles to download:",
            bg=master["bg"],
            fg=TEXT_COLOR,
            pady=5,
            font=FONT
        )
        label.pack(anchor="w", pady=5)

        entry_frame = tk.Frame(self, bg=master["bg"], highlightbackground=TEXT_COLOR, highlightthickness=1, bd=0)
        entry_frame.pack(anchor="w", padx=5, pady=5)

        self.entry = tk.Entry(
            entry_frame,
            bg=master["bg"],
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief="flat",
            highlightthickness=0,
            width=12,
            font=FONT
        )
        self.entry.insert(0, "5")  # Default value
        self.entry.pack(padx=10, pady=5)

        def handle_change(event):
            on_change(self.entry.get())

        self.entry.bind("<KeyRelease>", handle_change)
        self.entry.config(cursor="xterm")
