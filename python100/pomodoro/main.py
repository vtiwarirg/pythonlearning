import time
import tkinter as tk
from tkinter import messagebox

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
ROUNDS_BEFORE_LONG_BREAK = 4

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x600")
        self.root.config(padx=50, pady=50)
        self.rounds = 0
        self.is_running = False
        self.timer = None

        self.label = tk.Label(root, text="Pomodoro Timer", font=("Arial", 24))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.time_label = tk.Label(root, text="25:00", font=("Arial", 48))
        self.time_label.grid(row=1, column=0, columnspan=2, pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.session_label = tk.Label(root, text="Session: Work", font=("Arial", 16))
        self.session_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.minutes = WORK_MIN
        self.seconds = 0

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.count_down()

    def reset_timer(self):
        if self.timer:
            self.root.after_cancel(self.timer)
        self.is_running = False
        self.rounds = 0
        self.minutes = WORK_MIN
        self.seconds = 0
        self.time_label.config(text=f"{WORK_MIN:02d}:00")
        self.session_label.config(text="Session: Work")

    def count_down(self):
        if self.minutes == 0 and self.seconds == 0:
            self.is_running = False
            self.rounds += 1
            if self.rounds % (ROUNDS_BEFORE_LONG_BREAK * 2) == 0:
                self.start_session(LONG_BREAK_MIN, "Long Break")
            elif self.rounds % 2 == 0:
                self.start_session(WORK_MIN, "Work")
            else:
                self.start_session(SHORT_BREAK_MIN, "Short Break")
            return

        time_str = f"{self.minutes:02d}:{self.seconds:02d}"
        self.time_label.config(text=time_str)
        if self.seconds == 0:
            if self.minutes > 0:
                self.minutes -= 1
                self.seconds = 59
        else:
            self.seconds -= 1
        self.timer = self.root.after(1000, self.count_down)

    def start_session(self, minutes, session_type):
        self.minutes = minutes
        self.seconds = 0
        self.session_label.config(text=f"Session: {session_type}")
        messagebox.showinfo("Pomodoro", f"{session_type} time!")
        self.start_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()