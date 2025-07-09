import tkinter as tk
from tkinter import messagebox
import client.styles as styles
from client.components.input_field import InputField
from client.components.topics_selection import TopicsSelection
from client.components.date_range_selection import DateRangeSelection
from client.components.download_button import DownloadButton


def main():
    root = tk.Tk()
    root.title("ChemRxiv Fetcher MVP")

    selected_topics = []
    selected_date = []
    count = "5"

    def update_topics(topics):
        nonlocal selected_topics
        selected_topics = topics

    def update_date(date):
        nonlocal selected_date
        selected_date = date

    def update_count(new_count):
        nonlocal count
        count = new_count

    def download():
        # Пока заглушка вместо взаимодействия с API
        print(f"Topics selected: {selected_topics}")
        print(f"Date range selected: {selected_date}")
        print(f"Number of articles to download: {count}")
        messagebox.showinfo("Downloading...", "Files downloaded!")

    styles.configure_styles(root)

    # Initializing components
    topics = ["Agriculture and Food Chemistry", "Analytical Chemistry", "Biological and Medicinal Chemistry"]
    date_options = ["Last week", "Last month", "Last 3 months", "Last 6 months"]

    TopicsSelection(root, topics, update_topics).pack(pady=5, padx=10, anchor="w")
    DateRangeSelection(root, date_options, update_date).pack(pady=5, padx=10, anchor="w")
    InputField(root, update_count).pack(pady=5, padx=10, anchor="w")
    DownloadButton(root, download).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
