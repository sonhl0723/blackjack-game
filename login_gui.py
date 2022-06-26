from conf import *
from play import Player
from game_logic import *

class LoginGui(Frame):
    """Login Frame"""
    def __init__(self, master):
        super().__init__(master, height = 700, width = 700)
        master.geometry('600x600')
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        image = Image.open("./game_img/casino_bg.gif")
        self.imageP = ImageTk.PhotoImage(image)
        l = Label(self, image=self.imageP)
        l.image = self.imageP
        l.place(x = 0, y = 0)
        self.title = Label(self, text="Welcome to BlackJack Board!", font = ("Times", "30"), bg = "black", fg = "white")
        self.title.place(x=130,y=200)
        self.name = Label(self, text="Name", font = ("Times", "24"), bg  = "black" ,fg = "white")
        self.name.place(x=110,y=260)
        self.login_entry = Entry(self, width=20, bg = "black", fg = "white", highlightbackground = "black")
        self.login_entry.place(x=210,y=265)
        self.login_photo = PhotoImage(file = "./game_img/login.gif")
        self.button_login = Button(self, image = self.login_photo ,command = self.game_login, highlightbackground = "black")
        self.button_login.place(x=440,y=260)
        self.summary_window = Text(self, width = 25, height = 6, wrap = WORD, bg = "black", fg = "white", font = ("Times", "20"))
        self.summary_window.place(x=180,y=310)
        self.start_photo = PhotoImage(file = "./game_img/start.gif")
        self.button_play = Button(self, image = self. start_photo , command = self.game_start, highlightbackground = "black")
        self.button_play.place(x=75,y=500)

    def game_login(self):
        Player.name = self.login_entry.get()
        _, tries, wins, chips = View.get_record(Player.name)
        self.__tries = tries
        record = "Name : " + Player.name + "\n"
        record += "Game Tries : " + str(tries) + "\n"
        record += "Win Games : "+ str(wins) + "\n"
        if tries == 0:
            record += "Winning Rate : 0.0" + "\n"
        else:
            record += "Winning Rate : " + str(round((wins/tries)*100,2)) + "\n"
        record += "Chips : " + str(chips)
        self.summary_window.insert(0.0, record)
        self.name.destroy()
        self.login_entry.destroy()
        self.button_login.destroy()

    def game_start(self):
        self.__tries+=1
        self.destroy()
        Game(self.master)