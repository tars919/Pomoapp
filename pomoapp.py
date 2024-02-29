#Pomodoro Timer app
"""
Wireframe 
work time = 25
short break = 5
long break = 15
"""

#needed imports 
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style

#Set the defaults for the intervals 
work_t = 25 * 60
short_b = 5 * 60
long_b = 15 * 60

class PomoTimer:
    def __init__(self):
        self.r = tk.Tk()
        self.r.geometry("200x200")
        self.r.title("Pomodoro Timer")
        self.s = Style(theme="simplex")
        self.s.theme_use()

        self.timer_l = tk.Label(self.r, text="", font=("TKDefaultFont", 40))
        self.timer_l.pack(pady=20)

        self.start_b = ttk.Button(self.r, text="Start", command=self.start_timer)
        self.start_b.pack(pady=5)

        self.stop_b = ttk.button(self.r, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_b.pack(pady=5)

        self.work_time, self.break_time = work_t,short_b
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()
