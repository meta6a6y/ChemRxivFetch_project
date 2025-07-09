import tkinter as tk
from ..styles import TEXT_COLOR, FONT


class InputField(tk.Frame):
    """Input field for specifying number of articles to download."""

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
        self.error_state = False
        self.original_highlight = entry_frame["highlightbackground"]

        def handle_change(event):
            value = self.entry.get()
            if self.validate_number(value):
                self.set_normal_state()
            else:
                self.set_error_state()
            on_change(value)

        self.entry.bind("<KeyRelease>", handle_change)
        self.entry.bind("<FocusOut>", lambda e: self.validate_number(self.entry.get()))

    def validate_number(self, value):
        """Checks that a value is a natural number"""
        if not value:
            return False
        return value.isdigit() and int(value) > 0

    def set_error_state(self):
        if not self.error_state:
            self.error_state = True
            self.entry.master.config(highlightbackground="red", highlightthickness=1)

    def set_normal_state(self):
        if self.error_state:
            self.error_state = False
            self.entry.master.config(highlightbackground=TEXT_COLOR, highlightthickness=1)
