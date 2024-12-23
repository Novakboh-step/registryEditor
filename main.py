from tkinter import *
import winreg

def getKey():
    key = keyEntry.get()
    if key == "HKEY_CLASSES_ROOT":
        return winreg.HKEY_CLASSES_ROOT
    elif key == "HKEY_CURRENT_USER":
        return winreg.HKEY_CURRENT_USER
    elif key == "HKEY_LOCAL_MACHINE":
        return winreg.HKEY_LOCAL_MACHINE
    elif key == "HKEY_USERS":
        return winreg.HKEY_USERS
    elif key == "HKEY_CURRENT_CONFIG":
        return winreg.HKEY_CURRENT_CONFIG

def create():
    listbox.delete(0, END)
    try:
        key = winreg.CreateKey(getKey(), subkeyEntry.get())
        winreg.SetValueEx(key, nameEntry.get(), 0, winreg.REG_SZ, valueEntry.get())
        winreg.CloseKey(key)
        listbox.insert(END, "Created successfully")
    except WindowsError:
        listbox.insert(END, "ERROR")

def delete():
    listbox.delete(0, END)
    try:
        key = winreg.CreateKey(getKey(), subkeyEntry.get())
        winreg.DeleteValue(key, nameEntry.get())
        winreg.CloseKey(key)
        listbox.insert(END, "Deleted successfully")
    except WindowsError:
        listbox.insert(END, "ERROR")

def showInfo():
    listbox.delete(0, END)
    try:
        key = winreg.OpenKey(getKey(), subkeyEntry.get(), 0, winreg.KEY_READ)
        i = 0
        while True:
            try:
                programName, programPath, a = winreg.EnumValue(key, i)
                listbox.insert(END, f"{i + 1}) {programName}")
                i += 1
            except WindowsError:
                break
        winreg.CloseKey(key)
    except WindowsError:
        listbox.insert(END, "ERROR")

root = Tk()
root.geometry("300x350")
root.title("Registry Editor")
Label(text="Key:").grid(row=0, column=0)
keyEntry = Entry(width=30)
keyEntry.grid(row=0, column=1)
Label(text="Subkey:").grid(row=1, column=0)
subkeyEntry = Entry(width=30)
subkeyEntry.grid(row=1, column=1)
Button(text="Info", width=5, command=showInfo).grid(row=1, column=2)
Label(text="Name:").grid(row=2, column=0)
nameEntry = Entry(width=30)
nameEntry.grid(row=2, column=1)
Button(text="Delete", width=5, command=delete).grid(row=2, column=2)
Label(text="Value:").grid(row=3, column=0)
valueEntry = Entry(width=30)
valueEntry.grid(row=3, column=1)
Button(text="Create", width=5, command=create).grid(row=3, column=2)
listbox = Listbox(selectmode=EXTENDED, height=15, width=30)
listbox.grid(row=4, column=1)
root.mainloop()