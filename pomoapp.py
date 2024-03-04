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

        self.timer_label = tk.Label(self.r, text="", font=("TKDefaultFont", 40))
        self.timer_label.pack(pady=20)

        self.start_b = ttk.Button(self.r, text="Start", command=self.start_timer)
        self.start_b.pack(pady=5)

        self.stop_b = ttk.Button(self.r, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_b.pack(pady=5)

        self.work_time, self.break_time = work_t,short_b
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.r.mainloop()

    def start_timer(self):
        self.start_b.config(state=tk.DISABLED)
        self.stop_b.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        self.start_b.config(state=tk.NORMAL)
        self.stop_b.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time :
                self.is_work_time -= 1
                if self.work_time == 0:
                    self.is_work_timer = False
                    self.pomodoros_completed += 1
                    self.break_time = long_b if self.pomodoros_completed % 4 == 0 else short_b
                    messagebox.showinfo("Great Job!" if self.pomodoros_completed % 4 == 0
                                        else "Good Job!", "Take a long break you earned it!"
                                        if self.pomodoros_completed % 4 == 0
                                        else "Take a short break!")
                    
            else:
                self.break_time -= 1
                if self.break_time ==0:
                    self.is_work_time, self.work_time = True,work_t
                    messagebox.showinfo("Work Time", "Get back to work!")
            minutes,seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.r.after(1000,self.update_timer)

PomoTimer()
