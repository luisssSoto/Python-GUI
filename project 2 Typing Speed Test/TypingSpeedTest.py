import tkinter as tk
from tkinter import messagebox
import os, random
import pandas as pd
from dotenv import load_dotenv

# CONSTANTS
BLUE = "#306998"
LIGHT_BLUE = "#4B8BBE"
YELLOW = "#FFD43B"
LIGHT_YELLOW = "#FFE873"
GRAY = "#646464"
FONT_NAME = "Courier"

load_dotenv()
CURR_DIR = os.getenv('CURR_DIR')
print(CURR_DIR)
print()

class TypingSpeedTest():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Typing Speed Test")
        self.window.config(padx=20, pady=20, bg=BLUE)
        self.timer = None

        # Prepare data
        curr_dir = os.getcwd()
        print(F"current dir: {curr_dir}")
        df = pd.read_csv(f'{curr_dir}\\unigram_freq.csv')
        self.words = df['word']
        self.data = self.words.to_list()
        self.data = self.data[:1000]
        self.next_words = random.choices(self.data, k=200)

    # ------------ UI CONTROLS -------------
        # Buttons
        self.controls = tk.Frame(self.window)
        self.controls.pack(pady=20)
        self.controls.config(bg=LIGHT_YELLOW)
        self.start_btn = tk.Button(self.controls, text='Start', command=self.start, bg=YELLOW,).grid(row=0, column=0, padx=5, pady=5)
        self.restart_btn = tk.Button(self.controls, text="Restart", command=self.restart, bg=BLUE).grid(row=0, column=2, padx=5, pady=5)

        # Timer
        self.timer_controls = tk.Frame(self.window)
        self.timer_controls.pack(pady=20)
        self.timer_controls.config(bg=LIGHT_YELLOW)      
        self.time_canvas = tk.Canvas(self.timer_controls, width=300, height=50, bg=LIGHT_YELLOW, highlightthickness=0)
        self.time_canvas.grid(row=1, column=1)
        self.timer_text = self.time_canvas.create_text(150, 10, text="01:00", font=(FONT_NAME, 18, "bold"), fill="black")
        
        # Random Words
        self.random_words_controls = tk.Frame(self.window)
        self.random_words_controls.pack(pady=20)
        self.random_words_controls.config(bg=LIGHT_YELLOW) 
        self.random_words_canvas = tk.Canvas(self.random_words_controls, width=600, height=50, bg=LIGHT_YELLOW, highlightthickness=0)
        self.random_words_canvas.grid(row=2, column=0)
        self.random_words_text = self.random_words_canvas.create_text(300, 10, text="READY?!", font=(FONT_NAME, 15, "bold"), fill="black")

        # Written Words
        self.written_words_controls = tk.Frame(self.window)
        self.written_words_controls.pack(pady=20)
        self.written_words_controls.config(bg=LIGHT_YELLOW) 
        self.text_entry = tk.Entry(self.written_words_controls, width=25)
        self.text_entry.config(font=(FONT_NAME, 15))
        self.text_entry.grid(row=0, column=1, padx=5, pady=5)
        self.text_entry.insert(0, "Your text here")
        self.text_entry.bind('<Button-1>', self.click )

        # Record
        self.words_written = 0
        

    # ----------- FUNCTIONS -----------------

    def compare_words(self, event):
        self.random_word = self.next_words[-1]
        self.random_words_canvas.itemconfig(self.random_words_text, text=f"{self.random_word}")
        self.user_word = self.text_entry.get()
        if self.user_word == self.random_word:
            print(f"They are equal: {self.user_word}")
            self.words_written += 1
            self.next_words.pop()
            self.random_words_canvas.itemconfig(self.random_words_text, text=f"{self.next_words[-1]}")
            self.text_entry.delete(0, 100)
        else:
            self.random_words_canvas.itemconfig(self.random_words_text, text=f"{self.random_word}")
            messagebox.showinfo("Failed", f"Try again, words don't match")

    def click(self, event):
        self.text_entry.delete(0, 100)

    # ----------- START -------------------
    def start(self):
        self.text_entry.config(state='normal')
        self.text_entry.delete(0, 100)
        self.text_entry.focus() 
        self.random_words_canvas.itemconfig(self.random_words_text, text=f"{self.next_words[-1]}")
        self.text_entry.bind("<Return>", self.compare_words)
        self.count_down(59)

# ---------------------------- COUNT DOWN TIME ------------------------------- #
    def count_down(self, count):
        if count == 0:
            count = "00"
            self.text_entry.config(state='disabled')
        elif count < 10:
            count = f"0{count}"
        self.time_canvas.itemconfig(self.timer_text, text=f"{count}")
        if int(count) > 0:
            self.timer = self.window.after(1000, self.count_down, int(count) - 1 )
        else:
            self.time_canvas.itemconfig(self.timer_text, text=f"The time is over!")
            self.time_canvas.itemconfig(self.timer_text, text=f"You typed: {self.words_written} words!")

    # ---------------------------- TIMER RESTART ------------------------------- #
    def restart(self):
        self.window.after_cancel(self.timer)
        self.next_words = random.choices(self.data, k=200)
        self.time_canvas.itemconfig(self.timer_text, text="01:00")
        self.random_words_canvas.itemconfig(self.random_words_text, text="READY?!")
        self.text_entry.insert(0, "Your text here")
        self.words_written = 0