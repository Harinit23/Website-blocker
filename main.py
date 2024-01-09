from tkinter import *
import os
import platform
from datetime import datetime, timedelta
import ctypes
import sys  # Import the sys module

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    root = Tk()
    root.geometry('500x400')
    root.resizable(0, 0)
    root.title("Website Blocker")

    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    ip_address = '127.0.0.1'

    Label(root, text='Website Blocker', font='arial 20 bold').pack()

    Label(root, text='Enter Website :', font='arial 13 bold').place(x=5, y=60)

    Websites = Text(root, font='arial 10', height='2', width='40')
    Websites.place(x=140, y=60)

    def block_websites(websites):
        try:
            with open(host_path, 'a') as host_file:
                for website in websites:
                    host_file.write(ip_address + " " + website.strip() + '\n')
            Label(root, text="Blocked", font='arial 12 bold').place(x=230, y=200)
        except PermissionError:
            Label(root, text='Permission Denied. Run as Administrator.', font='arial 12 bold').place(x=150, y=200)

    def unblock_websites(websites):
        try:
            with open(host_path, 'r') as host_file:
                lines = host_file.readlines()

            with open(host_path, 'w') as host_file:
                for line in lines:
                    if all(website.strip() not in line for website in websites):
                        host_file.write(line)
            Label(root, text="Unblocked", font='arial 12 bold').place(x=230, y=200)
        except PermissionError:
            Label(root, text='Permission Denied. Run as Administrator.', font='arial 12 bold').place(x=150, y=200)

    block = Button(root, text='Block', font='arial 12 bold', pady=5, command=lambda: block_websites(Websites.get(1.0, END).split(',')), width=6,
                   bg='royal blue1', activebackground='sky blue')
    block.place(x=230, y=150)

    unblock = Button(root, text='Unblock', font='arial 12 bold', pady=5, command=lambda: unblock_websites(Websites.get(1.0, END).split(',')), width=8,
                     bg='lightcoral', activebackground='indianred')
    unblock.place(x=330, y=150)

    root.mainloop()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)