# import tkinter as tk
# from tkinter import ttk

# from tkcalendar import Calendar, DateEntry
# # test
# def example1():
#     def print_sel():
#         print(cal.selection_get())

#     top = tk.Toplevel(root)

#     cal = Calendar(top,
#                    font="Arial 14", selectmode='day',
#                    cursor="hand1", year=2018, month=2, day=5)
#     cal.pack(fill="both", expand=True)
#     ttk.Button(top, text="ok", command=print_sel).pack()

# def example2():
#     top = tk.Toplevel(root)

#     ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

#     cal = DateEntry(top, width=12, background='darkblue',
#                     foreground='white', borderwidth=2)
#     cal.pack(padx=10, pady=10)

# root = tk.Tk()
# s = ttk.Style(root)
# s.theme_use('clam')

# ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
# ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)
# root.geometry("500x500")
# root.mainloop()

# """
# conn = psycopg2.connect(
#     dbname="RGZ_KS",
#     user="postgres",
#     password="1234",
#     host="127.0.0.1",
#     port="5432"
# )

# """
import tkinter as tk
import tkinter.ttk as ttk

class App(ttk.Frame):

    def __init__(self, parent=None, *args, **kwargs):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        # Create Treeview 
        self.tree = ttk.Treeview(self, column=('A','B'), selectmode='none', height=7)
        self.tree.grid(row=0, column=0, sticky='nsew')

        # Setup column heading
        self.tree.heading('#0', text=' Pic directory', anchor='center')
        self.tree.heading('#1', text=' A', anchor='center')
        self.tree.heading('#2', text=' B', anchor='center')
        # #0, #01, #02 denotes the 0, 1st, 2nd columns

        # Setup column
        self.tree.column('A', anchor='center', width=100)
        self.tree.column('B', anchor='center', width=100)

        # Insert image to #0 
        self._img = tk.PhotoImage(file="38.png") #change to your file path
        self.tree.insert('', 'end', text="#0's text", image=self._img,
                         value=("A's value", "B's value"))


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('450x180+300+300')

    app = App(root)
    app.grid(row=0, column=0, sticky='nsew')

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    root.mainloop()