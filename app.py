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
    selected_date = ""
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
        print(f"Выбрано тем: {selected_topics}")
        print(f"Выбран диапазон: {selected_date}")
        print(f"Количество статей: {count}")
        messagebox.showinfo("Скачивание", "Файлы скачаны!")

    styles.configure_styles(root)

    # Инициализация компонентов
    topics = ["Organic Chemistry", "Physical Chemistry", "Physics", "Materials Science"]
    date_options = ["Последняя неделя", "Последний месяц"]

    TopicsSelection(root, topics, update_topics).pack(pady=5, padx=10, anchor="w")
    DateRangeSelection(root, date_options, update_date).pack(pady=5, padx=10, anchor="w")
    InputField(root, update_count).pack(pady=5, padx=10, anchor="w")
    DownloadButton(root, download).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
