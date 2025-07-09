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
        if not validate_all():
            messagebox.showerror("Error", "Please fix all errors before downloading")
            return

        print(f"Topics selected: {selected_topics}")
        print(f"Date range selected: {selected_date}")
        print(f"Number of articles to download: {count}")
        messagebox.showinfo("Downloading...", "Files downloaded!")

    styles.configure_styles(root)

    # Initialization components
    topics = ["Agriculture and Food Chemistry", "Analytical Chemistry", "Biological and Medicinal Chemistry"]
    date_options = ["Last week", "Last month", "Last 3 months", "Last 6 months"]

    # Save links to components
    topics_component = TopicsSelection(root, topics, update_topics)
    date_component = DateRangeSelection(root, date_options, update_date)
    input_field = InputField(root, update_count)

    topics_component.pack(pady=5, padx=10, anchor="w")
    date_component.pack(pady=5, padx=10, anchor="w")
    input_field.pack(pady=5, padx=10, anchor="w")
    DownloadButton(root, download).pack(pady=20)

    def validate_all():
        valid = True

        # Check topics
        if not selected_topics:
            topics_component.set_error_state()
            valid = False
        else:
            topics_component.set_normal_state()

        # Check date
        if not selected_date:
            date_component.set_error_state()
            valid = False
        else:
            date_component.set_normal_state()

        # Check the number
        if not count or not count.isdigit() or int(count) <= 0:
            input_field.set_error_state()
            valid = False
        else:
            input_field.set_normal_state()

        return valid

    root.mainloop()


if __name__ == "__main__":
    main()
