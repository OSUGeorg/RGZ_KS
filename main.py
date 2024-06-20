import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox
from time import sleep
from tkcalendar import DateEntry
from threading import Thread

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
    name = entry_name.get()
    date_start = cal.get_date()
    
    # Добавление билета в базу данных
    cur.execute("INSERT INTO tickets (name, date_start) VALUES (%s, %s)", (name, date_start))
    conn.commit()
    messagebox.showinfo("Успех", "Билет успешно добавлен")

# Функция для обновления билета в базе данных
def update_ticket():
    name = entry_name.get()
    date_start = cal.get_date()
    
    # Обновление билета в базе данных
    cur.execute("UPDATE tickets SET date_start = %s WHERE name = %s", (date_start, name))
    conn.commit()
    messagebox.showinfo("Успех", "Билет успешно обновлен")

# Создание графического интерфейса с помощью tkinter
root = tk.Tk()
root.title("Продажа билетов в авиарейсы")

# Добавление полей ввода и кнопок для добавления и обновления билетов
label_name = tk.Label(root, text="Название:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_date_start = tk.Label(root, text="Дата вылета:")
label_date_start.pack()

cal = DateEntry(root,width=30,bg="darkblue",fg="white",year=2010)
cal.pack()

btn_add = tk.Button(root, text="Добавить билет", command=add_ticket)
btn_add.pack()

btn_update = tk.Button(root, text="Обновить билет", command=update_ticket)
btn_update.pack()

tree = ttk.Treeview(root, columns=("ID", "Place", "Date"))
tree.heading("ID", text="ID")
tree.heading("Place", text="Место")
tree.heading("Date", text="Дата Вылета")
# tree.heading("Picture", text="Картинка")

tree.pack(pady=10)

# def get_id_tree(a: str, lenght: int):
#     if not a: return a
#     integ = int(a[1:], 16)
#     integ += lenght
#     return "I" + str(hex(integ)[2:]).upper().zfill(3)


# def get_url_image(q):
#     url = 'https://www.google.com/search?q={0}&tbm=isch'.format(q)
#     content = requests.get(url).content
#     soup = BeautifulSoup(content,'lxml')
#     images = soup.findAll('img')
#     for i in images:
#         if not i["src"].endswith(".gif"):
#             url = i["src"]
#             print(url)
#             u = urllib.request.urlopen(url)
#             raw_data = u.read()
#             u.close()
#             im = Image.open(BytesIO(raw_data)).resize((38, 38))
#             return ImageTk.PhotoImage(im)


def test():
    while root.state() == "normal":
        # foc = tree.focus()
        tree.delete(*tree.get_children())
        # print(foc)
        cur.execute("SELECT * FROM tickets")
        rows = cur.fetchall()
        for i in rows:
            # im = get_url_image(i[1])
            # print(im)
            # im = Image.open("38.png")
            tree.insert("", tk.END, values=i) # tk.PhotoImage(data=base64.b64decode(requests.get(get_url_image(i[1])).content))
        # tree.focus(get_id_tree(foc, len(rows)))
        sleep(3)

# style = ttk.Style(root)
# style.configure("Treeview", rowheight=38)

Thread(target=test).start()
root.mainloop()
