import tkinter as tk
from tkinter import ttk

# Colors and fonts
BG_COLOR = "#26292D"
PRIMARY_COLOR = "#5E23F0"
TEXT_COLOR = "#FFFFFF"
FONT_FAMILY = "Inter"
FONT_SIZE = 10
FONT = (FONT_FAMILY, FONT_SIZE)


APP_WIDTH = 620
APP_HEIGHT = 600


def configure_styles(root):
    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("TLabel",
                    background=BG_COLOR,
                    foreground=TEXT_COLOR,
                    font=FONT)
    style.configure("TButton",
                    background=PRIMARY_COLOR,
                    foreground=TEXT_COLOR,
                    font=FONT,
                    borderwidth=0,
                    padding=6)
    style.map("TButton",
              background=[("active", "#4819B9")])

    style.configure("TCheckbutton",
                    background=BG_COLOR,
                    foreground=TEXT_COLOR,
                    font=FONT)

    style.configure("TRadiobutton",
                    background=BG_COLOR,
                    foreground=TEXT_COLOR,
                    font=FONT)

    root.configure(bg=BG_COLOR)
    root.resizable(False, False)
    # root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")    # Disable for auto-fitting
