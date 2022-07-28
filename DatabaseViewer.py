import os
import pandas as pd
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk


# ----backend ------------
def connection():
    try:
        temp = tk.Tk()
        temp.title("Open")
        temp_width = 100
        temp_height = 100
        temp_screen_width = temp.winfo_screenwidth()
        temp_screen_height = temp.winfo_screenheight()
        a = int((temp_screen_width/2) - (temp_width/2))
        b = int((temp_screen_height/2) - (temp_height/2))
        temp.geometry("{}x{}+{}+{}".format(temp_width, temp_height, a, b))
        database_connect = filedialog.askopenfilename(defaultextension=".db", filetypes=(("SQLite Database", ".db"),
                                                                                                ("All files", "*")))
        connect_route = os.path.abspath(database_connect)
        conn = sqlite3.connect(connect_route)

        temp.destroy()
        return conn

    except sqlite3.OperationalError:
        temp.destroy()
        quit()



def search_rs(ID):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE ID=?""", (ID,))
    results = cur.fetchone()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results


def search_pos(POS):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE POS=?""", (POS,))
    results = cur.fetchone()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results


def search_qual(QUAL):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE QUAL=?""", (QUAL,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def search_freq(FREQ):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE FREQ=?""", (FREQ,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def search_geneinfo(GENEINFO):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE GENEINFO=?""", (GENEINFO,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        df = pd.DataFrame(results)
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def search_clnvi(CLNVI):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE CLNVI=?""", (CLNVI,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def search_clnorigin(CLNORIGIN):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE CLNORIGIN=?""", (CLNORIGIN,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def search_clnsig(CLNSIG):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE CLNSIG=?""", (CLNSIG,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def search_clndisdb(CLNDISDB):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE CLNDISDB=?""", (CLNDISDB,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def search_clndn(CLNDN):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE CLNDN=?""", (CLNDN,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def search_clnrevstat(CLNREVSTAT):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE CLNREVSTAT=?""", (CLNREVSTAT,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        df = pd.DataFrame(results)
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def search_clnacc(CLNACC):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE CLNACC=?""", (CLNACC,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def search_clnhgvs(CLNHGVS):
    cur = con.cursor()
    cur.execute("""SELECT * FROM VCF_data WHERE CLNHGVS=?""", (CLNHGVS,))
    results = cur.fetchall()

    if results is None:
        return
    else:
        con.commit()
        saved = filedialog.asksaveasfile(defaultextension='.csv', 
        filetypes=[('Comma-Separated Values', '.csv')])
        if saved is None:
            return results
        else:
            df = pd.DataFrame(results)
            df.to_csv(saved, index=False)
            return results

def disconnect():
    con.close()

# ------menubar function---------
def leave():
    if messagebox.askyesno(message="Cancel Current Session ?"):
        disconnect()
        window.destroy()
    else:
        return


def about():
    about_window = tk.Toplevel()
    about_window.resizable(0, 0)
    about_window.title("Licence")
    about_window_width = 500
    about_window_height = 400
    about_screen_width = about_window.winfo_screenwidth()
    about_screen_height = about_window.winfo_screenheight()
    x = int((about_screen_width/2) - (about_window_width/2))
    y = int((about_screen_height/2) - (about_window_height/2))
    about_window.geometry("{}x{}+{}+{}".format(about_window_width, about_window_height, x, y))
    licence = Label(about_window, text="""MIT License Copyright (c) 2022 Cheng-Wei Liu

    Permission is hereby granted, free of charge, 
    to any person obtaining a copy of this software and 
    associated documentation files (the "Software"), 
    to deal in the Software without restriction, 
    including without limitation the rights to use, 
    copy, modify, merge, publish, distribute, sublicense, 
    and/or sell copies of the Software, and to permit persons to whom 
    the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included 
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
    WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
    PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
    OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
    THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.""")
    licence.pack()


# ------------button function---------
def clear_tab1():
    rsID_entry.delete(0, END)
    pos_entry.delete(0, END)


def clear_tab2():
    qual_entry.delete(0, END)
    freq_entry.delete(0, END)
    geneinfo_entry.delete(0, END)
    clnvi_entry.delete(0, END)
    clnorigin_entry.delete(0, END)
    clnsig_entry.delete(0, END)
    clndisdb_entry.delete(0, END)
    clndn_entry.delete(0, END)
    clnrevstat_entry.delete(0, END)
    clnacc_entry.delete(0, END)
    clnhgvs_entry.delete(0, END)


def get_from_pos():
    if len(POS.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_pos(POS.get())

        if data is None:
            new_window.destroy()
        else:
            dataview.insert(tk.END, data, str(""))
            dataview.pack()


def get_from_rs():
    if len(ID.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_rs(ID.get())
        if data is None:
            new_window.destroy()
        else:
            dataview.insert(tk.END, data, str(""))
            dataview.pack()


def get_from_qual():
    if len(QUAL.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_qual(ID.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()


def get_from_freq():
    if len(FREQ.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_freq(FREQ.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()

def get_from_geneinfo():
    if len(GENEINFO.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_geneinfo(GENEINFO.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()


def get_from_clnvi():
    if len(CLNVI.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_clnvi(CLNVI.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()


def get_from_clnorigin():
    if len(CLNORIGIN.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_clnorigin(CLNORIGIN.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()


def get_from_clnsig():
    if len(CLNSIG.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("800x1000+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_clnsig(CLNSIG.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()


def get_from_clndisdb():
    if len(CLNDISDB.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("800x1000+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_clndisdb(CLNDISDB.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()


def get_from_clndn():
    if len(CLNDN.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_clndn(CLNDN.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()


def get_from_clnrevstat():
    if len(CLNREVSTAT.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_clnrevstat(CLNREVSTAT.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()


def get_from_clnacc():
    if len(CLNACC.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_clnacc(CLNACC.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()


def get_from_clnhgvs():
    if len(CLNHGVS.get()) == 0:
        return
    else:
        new_window = Toplevel()
        new_window.title("View")
        new_window.geometry("1000x600+0+0")
        new_window.resizable(0, 0)
        vertical_scrollbar = Scrollbar(new_window)
        horizontal_scrollbar = Scrollbar(new_window)
        dataview = Listbox(new_window, height=35, width=100, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        data = search_clnhgvs(CLNHGVS.get())
        if data is None:
            new_window.destroy()
        else:
            for i in data:
                dataview.insert(tk.END, i, str(""))
            dataview.pack()


# --------------------------
con = connection()
window = tk.Tk()
window.title("VCF Data Viewer")
window_width = 750
window_height = 540
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
z = int((screen_width/2) - (window_width/2))
w = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, z, w))
window.config(bg="#f5d847", bd=6)
window.resizable(0, 0)
# ----------------Frame setting----------------------
display = ttk.Notebook(window)

tab1 = tk.Frame(display, bd=3)
tab2 = tk.Frame(display, bd=3)

display.add(tab1, text="Specific Search")
display.add(tab2, text="General Search")
display.pack(expand=True, fill="both")

# -----------tab1 variables--------
POS = tk.StringVar(window)
ID = StringVar(tab1)

#-----------tab2 variables-------
QUAL = StringVar(tab2)
FREQ = StringVar(tab2)
GENEINFO = StringVar(tab2)
CLNVI = StringVar(tab2)
CLNORIGIN = StringVar(tab2)
CLNSIG = StringVar(tab2)
CLNDISDB = StringVar(tab2)
CLNDN = StringVar(tab2)
CLNREVSTAT = StringVar(tab2)
CLNACC = StringVar(tab2)
CLNHGVS = StringVar(tab2)

# -------------Specific Search label-------------
specific_label = tk.Label(tab1, text="Specific\nSearch", font=("Arial", 25, "bold"), bg='#e6d1b5')
specific_label.grid(row=0, column=0)

tk.Label(tab1, text="").grid(row=1, column=0)
tk.Label(tab1, text="").grid(row=2, column=0)
rsID_label = tk.Label(tab1, text="By rsID (with 'rs') ", font=("Arial", 25))
rsID_label.grid(row=3, column=0)
rsID_entry = tk.Entry(tab1, textvariable=ID, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=30)
rsID_entry.grid(row=3, column=1)
rs_btn = tk.Button(tab1, text="Submit", command=get_from_rs)
rs_btn.grid(row=3, column=2)

tk.Label(tab1, text="").grid(row=4, column=0)
tk.Label(tab1, text="").grid(row=5, column=0)

pos_label = tk.Label(tab1, text="By Position ", font=("Arial", 25))
pos_label.grid(row=6, column=0)
pos_entry = tk.Entry(tab1, textvariable=POS, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=30)
pos_entry.grid(row=6, column=1)
pos_btn = tk.Button(tab1, text="Submit", command=get_from_pos)
pos_btn.grid(row=6, column=2)

tk.Label(tab1, text="").grid(row=7, column=0)
tk.Label(tab1, text="").grid(row=8, column=0)
clear_btn = tk.Button(tab1, text="Clear", command=clear_tab1)
clear_btn.grid(row=9, column=1)

# -------------------General Search label-------
general_label = tk.Label(tab2, text="General\nSearch", font=("Arial", 25, "bold"), bg='#e6d1b5')
general_label.grid(row=0, column=0)
tk.Label(tab2, text="").grid(row=1, column=0)

qual = tk.Label(tab2, text="QUAL")
qual.grid(row=2, column=0)
qual_entry = tk.Entry(tab2, textvariable=QUAL, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
qual_entry.grid(row=2, column=1)
qual_btn = tk.Button(tab2, text="Submit", command=get_from_qual)
qual_btn.grid(row=2, column=2)

freq = tk.Label(tab2, text="FREQ")
freq.grid(row=2, column=3)
freq_entry = tk.Entry(tab2, textvariable=FREQ, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
freq_entry.grid(row=2, column=4)
freq_btn = tk.Button(tab2, text="Submit", command=get_from_freq)
freq_btn.grid(row=2, column=5)

geneinfo = tk.Label(tab2, text="GENEINFO")
geneinfo.grid(row=3, column=0)
geneinfo_entry = tk.Entry(tab2, textvariable=GENEINFO, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
geneinfo_entry.grid(row=3, column=1)
geneinfo_btn = tk.Button(tab2, text="Submit", command=get_from_geneinfo)
geneinfo_btn.grid(row=3, column=2)

clnvi = tk.Label(tab2, text="CLNVI")
clnvi.grid(row=3, column=3)
clnvi_entry = tk.Entry(tab2, textvariable=CLNVI, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
clnvi_entry.grid(row=3, column=4)
clnvi_btn = tk.Button(tab2, text="Submit", command=get_from_clnvi)
clnvi_btn.grid(row=3, column=5)

clnorigin = tk.Label(tab2, text="CLNORIGIN")
clnorigin.grid(row=4, column=0)
clnorigin_entry = tk.Entry(tab2, textvariable=CLNORIGIN, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
clnorigin_entry.grid(row=4, column=1)
clnorigin_btn = tk.Button(tab2, text="Submit", command=get_from_clnorigin)
clnorigin_btn.grid(row=4, column=2)

clnsig = tk.Label(tab2, text="CLNSIG")
clnsig.grid(row=4, column=3)
clnsig_entry = tk.Entry(tab2, textvariable=CLNSIG, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
clnsig_entry.grid(row=4, column=4)
clnsig_btn = tk.Button(tab2, text="Submit", command=get_from_clnsig)
clnsig_btn.grid(row=4, column=5)

clndisdb = tk.Label(tab2, text="CLNDISDB")
clndisdb.grid(row=5, column=0)
clndisdb_entry = tk.Entry(tab2, textvariable=CLNDISDB, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
clndisdb_entry.grid(row=5, column=1)
clndisdb_btn = tk.Button(tab2, text="Submit", command=get_from_clndisdb)
clndisdb_btn.grid(row=5, column=2)

clndn = tk.Label(tab2, text="CLNDN")
clndn.grid(row=5, column=3)
clndn_entry = tk.Entry(tab2, textvariable=CLNDN, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
clndn_entry.grid(row=5, column=4)
clndn_btn = tk.Button(tab2, text="Submit", command=get_from_clndn)
clndn_btn.grid(row=5, column=5)

clnrevstat = tk.Label(tab2, text="CLNREVSTAT")
clnrevstat.grid(row=6, column=0)
clnrevstat_entry = tk.Entry(tab2, textvariable=CLNREVSTAT, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
clnrevstat_entry.grid(row=6, column=1)
clnrevstat_btn = tk.Button(tab2, text="Submit", command=get_from_clnrevstat)
clnrevstat_btn.grid(row=6, column=2)

clnacc = tk.Label(tab2, text="CLNACC")
clnacc.grid(row=6, column=3)
clnacc_entry = tk.Entry(tab2, textvariable=CLNACC, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
clnacc_entry.grid(row=6, column=4)
clnacc_btn = tk.Button(tab2, text="Submit", command=get_from_clnacc)
clnacc_btn.grid(row=6, column=5)

clnhgvs = tk.Label(tab2, text="CLNHGVS")
clnhgvs.grid(row=7, column=0)
clnhgvs_entry = tk.Entry(tab2, textvariable=CLNHGVS, justify=CENTER, bd=3, relief=SUNKEN, takefocus=1, width=15)
clnhgvs_entry.grid(row=7, column=1)
clnhgvs_btn = tk.Button(tab2, text="Submit", command=get_from_clnhgvs)
clnhgvs_btn.grid(row=7, column=2)

tk.Label(tab2, text="").grid(row=8, column=0)
clear_all_btn = Button(tab2, text="Clear All", command=clear_tab2)
clear_all_btn.grid(row=9, column=2)
# -----------menubar ------------------
menubar = tk.Menu(window)
window.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=leave)
about_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Licence", command=about)
# ------------------------------------

window.mainloop()
