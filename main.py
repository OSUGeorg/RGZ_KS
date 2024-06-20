import tkinter as tk
from tkcalendar import Calendar
import psycopg2

# Подключение к PostgreSQL
conn = psycopg2.connect(
    dbname="RGZ_KS",
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5432"
)
cur = conn.cursor()

# Функция для добавления билета в базу данных
def add_ticket():
    # Здесь должен быть код добавления билета в базу данных

    pass

# Функция для изменения билета в базе данных
def update_ticket():
    # Здесь должен быть код изменения билета в базе данных
    pass

# Создание графического интерфейса с помощью tkinter
root = tk.Tk()
root.title("Продажа билетов в авиарейсы")

# Добавление кнопок для добавления и изменения билетов
btn_add = tk.Button(root, text="Добавить билет", command=add_ticket)
btn_add.pack()

btn_update = tk.Button(root, text="Изменить билет", command=update_ticket)
btn_update.pack()

root.geometry("500x500")
root.mainloop()
