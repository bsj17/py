import tkinter as tk


class StopwatchApp:
    def __init__(self):
        master = tk.Tk()
        self.master = master
        self.master.title("Stopwatch App")

        self.current_time = 0
        self.is_running = False

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")

        self.label = tk.Label(master,
                              textvariable=self.time_var,
                              font=("Helvetica", 48))
        self.label.grid(row=0, column=0, columnspan=3, pady=20)

        self.start_button = tk.Button(master,
                                      text="Start",command=self.start_stopwatch)
        self.start_button.grid(row=1, column=0, padx=5)

        self.stop_button = tk.Button(master,
                                     text="Stop",
                                     state=tk.DISABLED,command=self.stop_stopwatch)
        self.stop_button.grid(row=1, column=1, padx=5)

        self.restart_button = tk.Button(master,
                                        text="Restart",
                                        state=tk.DISABLED,command=self.restart_stopwatch)
        self.restart_button.grid(row=1, column=2, padx=5)

    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.update_time()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.restart_button.config(state=tk.NORMAL)

    def stop_stopwatch(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.restart_button.config(state=tk.NORMAL)

    def restart_stopwatch(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.DISABLED)
        self.current_time = 0
        self.time_var.set(self.format_time(self.current_time))

    def update_time(self):
        if self.is_running:
            self.current_time = self.current_time + 1
            self.time_var.set(self.format_time(self.current_time))
            self.master.after(1000, self.update_time)

    def format_time(self, time):
        hours, remainder = divmod(time, 3600)
        minutes, seconds = divmod(remainder, 60)
        return "{:02}:{:02}:{:02}".format(int(hours),
                                          int(minutes),
                                          int(seconds))

    def mainloop(self):
        self.master.mainloop()
