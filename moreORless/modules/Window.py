import tkinter as tk
import modules.useful_fct as use
from modules.GuessGame import GuessGame

BPARAM = {
    "relief" : tk.RAISED, 
    "bg" : "#555555",
    "fg" : "#FFFFFF",
    "font" : ("Helvetica",10),
    "width" : 8
}
LPARAM = {
    "bg" : "#333333",
    "fg" : "#FFFFFF",
    "font" : ("Helvetica",10)
}

class Window:
    def __init__(self, game_data:GuessGame) -> None:
        self.root = tk.Tk()
        self.root.title("Guess The Number")
        self.root.configure(bg="#333333")
        # exit shortcut
        self.root.bind("<Escape>", self.exit)

        self.root.iconbitmap("assets/question.ico")
        
        self.guess_game = game_data
        self.result = None
        self.loose = False

        # init here to avoid a "not initialized" error in main_menu()
        self.main_frame = tk.Frame(self.root, bg="#333333")

        self.main_menu()
        
    def main_menu(self):
        use.clear(self.main_frame)
        self.main_frame.pack(fill="both")
        
        self.display_title(self.main_frame,"Guess The Number")

        self.B_start = tk.Button(self.main_frame, text="Start", **BPARAM, command=self.game_menu)
        self.B_settings = tk.Button(self.main_frame, text="Settings", **BPARAM, command=self.settings_menu)
        self.B_exit = tk.Button(self.main_frame, text="Exit", **BPARAM, command=self.exit)

        self.B_start.pack(pady=10)
        self.B_settings.pack(pady=10)
        self.B_exit.pack(pady=10)

        use.set_geometry(self.root)
    
    def settings_menu(self):
        use.clear(self.main_frame)
        self.display_title(self.main_frame,"Guess The Number - Settings")
        self.main_frame.pack(fill="both")
        #Top frame for widgets in the body
        body_frame = tk.Frame(self.main_frame, bg="#333333")
        body_frame.pack()

        # subdivision left and right for great align text and input
        LeftFrame = tk.Frame(body_frame, bg="#333333")
        LeftFrame.pack(side="left", fill="both")

        RightFrame = tk.Frame(body_frame, bg="#333333")
        RightFrame.pack(side="left", fill="both")

        self.L_start = tk.Label(LeftFrame, text="Start (min:0) :", **LPARAM)
        self.L_end = tk.Label(LeftFrame, text="End (>Start) :", **LPARAM)
        self.L_difficulty = tk.Label(LeftFrame, text="Difficulty (>0) :", **LPARAM)
        self.L_max_attempts = tk.Label(LeftFrame, text="Max Attempts ( 0< X <End) :", **LPARAM)
        self.L_start.pack()
        self.L_end.pack()
        self.L_max_attempts.pack()

        self.E_start = tk.Entry(RightFrame)
        self.E_end = tk.Entry(RightFrame)
        self.E_max_attempts = tk.Entry(RightFrame)
        self.E_start.pack(pady=1)
        self.E_end.pack(pady=2)
        self.E_max_attempts.pack(pady=1)

        self.E_start.insert(0, self.guess_game.start)
        self.E_end.insert(0, self.guess_game.end)
        self.E_max_attempts.insert(0, self.guess_game.max_attempts)

        bottom_frame = tk.Frame(self.main_frame)
        bottom_frame.pack(side="right", fill="x")

        self.B_save = tk.Button(bottom_frame, text="Save",command=self.save_settings, **BPARAM)
        self.B_save.pack(side="left")

        self.B_back = tk.Button(bottom_frame, text="Back", command=self.main_menu, **BPARAM)
        self.B_back.pack(side="left")

        use.set_geometry(self.root)
    
    def game_menu(self):
        use.clear(self.main_frame)
        self.display_title(self.main_frame, "Guess The Number - Game")
        self.main_frame.pack(fill="both", expand=True)

        self.guess_game.generate_number()
        self.result = None
        self.loose = False

        self.body_frame = tk.Frame(self.main_frame, bg="#333333")
        self.body_frame.pack(fill="both", expand=True)

        self.display_body()

        bottom_frame = tk.Frame(self.main_frame, bg="#333333")
        bottom_frame.pack(side="bottom", fill="x")

        self.B_back = tk.Button(bottom_frame, text="Back", command=self.main_menu, **BPARAM)
        self.B_back.pack(side="right")

        use.set_geometry(self.root)
    
    def display_body(self):
        use.clear(self.body_frame)

        left_frame = tk.Frame(self.body_frame, bg="#333333")
        left_frame.pack(fill="both", expand=True, side="left")

        if self.result==False and not self.guess_game.ItsMore():
            bg = "#FF0000"
            fg = "#FFFFFF"
            font = "Helvetica"
            font_s = 30
            label = tk.Label(left_frame, text="-", bg=bg, fg=fg, font=(font,font_s), width=1, height=1)
            label.pack()

        center_frame = tk.Frame(self.body_frame, bg="#333333")
        center_frame.pack(fill="both", expand=True, side="left")

        self.E_guess = tk.Entry(center_frame)
        self.E_guess.pack()
        self.E_guess.insert(0,self.guess_game.nb_answer)
        self.E_guess.bind("<Return>", self.play)
        self.E_guess.focus()

        L_attempts = tk.Label(center_frame, text=f"Attemps : {self.guess_game.nb_attempts} / {self.guess_game.max_attempts}", **LPARAM)
        L_attempts.pack()

        L_best_attempts = tk.Label(center_frame, text=f"Best Attemps : {self.guess_game.best_attempts}", **LPARAM)
        L_best_attempts.pack()

        if self.result:
            L_win = tk.Label(center_frame, text="You win !", **LPARAM)
            L_win.pack()
            B_restart = tk.Button(center_frame, text="Restart", command=self.restart, **BPARAM)
            B_restart.pack()
        elif self.loose:
            L_win = tk.Label(center_frame, text="You Loose", **LPARAM)
            L_win.pack()
            B_restart = tk.Button(center_frame, text="Restart", command=self.game_menu, **BPARAM)
            B_restart.pack()
        else:
            B_play = tk.Button(center_frame, text="Play", command=self.play)
            B_play.pack()

        right_frame = tk.Frame(self.body_frame, bg="#333333")
        right_frame.pack(fill="both", expand=True, side="right")

        if self.result==False and self.guess_game.ItsMore():
            bg = "#00FF00"
            fg = "#FFFFFF"
            font = "Helvetica"
            font_s = 30
            label = tk.Label(right_frame, text="+", bg=bg, fg=fg, font=(font,font_s), width=1, height=1)
            label.pack()

        use.set_geometry(self.root)
    
    def play(self, e=None):
        if self.guess_game.nb_attempts >= self.guess_game.max_attempts:
            self.game_menu()
        else:
            try:
                self.guess_game.nb_answer = int(self.E_guess.get())
            except:
                self.guess_game.nb_answer = 0
            self.result = self.guess_game.check_answer()
            self.guess_game.nb_attempts += 1
            if self.guess_game.nb_attempts == self.guess_game.max_attempts:
                self.loose = True
            self.display_body()

    def restart(self):
        if self.guess_game.nb_attempts > self.guess_game.best_attempts:
            self.guess_game.best_attempts = self.guess_game.nb_attempts
        self.game_menu()

    def save_settings(self):
        start = int(self.E_start.get())
        end = int(self.E_end.get())
        max_attempts = int(self.E_max_attempts.get())
        if start >= 0 and end > start and max_attempts > 0:
            self.guess_game.modify(start,end,max_attempts)
            return self.main_menu()
        self.popup_error("Incorrect Inputs")
    
    def popup_error(self, text:str):
        popup = tk.Toplevel(bg="#333333")
        popup.title("Error Input")

        label = tk.Label(popup, text=text, font=("Helvetica",30), fg="#AA0000",bg="#333333")
        label.pack()

        use.set_geometry(popup, 50, 20)

    def display_title(self, frame:tk.Tk|tk.Frame, text:str):
        self.title = tk.Label(frame, text=text, bg="#333333", fg="#FFFFFF", font=("Helvetica",15))
        self.title.pack(pady=5)

    def exit(self, event=None):
        self.root.quit()
        self.root.destroy()

    def run(self):
        self.root.mainloop()