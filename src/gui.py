import tkinter as tk
import time
from config.config import Config

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{800}x{600}")
        self.root.configure(bg='white')
        self.root.title("Serial Position Effect Experiment")
        self.label = tk.Label(self.root, text='', bg='white', fg='black')
        self.label.pack(expand=True)
        self.var = tk.StringVar()

    def show_instructions(self, text, wait=True):
        self.label.config(text=text)
        self.root.update()
        if wait:
            self.root.bind('<Return>', lambda e: self.var.set('x'))
            self.root.wait_variable(self.var)
            self.var.set('')

    def show_stimulus(self, word):
        self.label.config(text=word)
        self.root.update()
        time.sleep(1)
        self.label.config(text='')
        self.root.update()
        time.sleep(0.5)

    def show_recall_prompt(self):
        self.label.config(text='Type the words you remember, separated by spaces:')
        entry = tk.Entry(self.root)
        entry.pack(pady=5)
        entry.focus()
        self.root.update()
        self.root.bind('<Return>', lambda e: self.var.set(entry.get()))
        self.root.wait_variable(self.var)
        text = self.var.get()
        entry.destroy()
        self.label.config(text='')
        return text.strip().lower().split()