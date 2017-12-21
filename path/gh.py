from tkinter import*
import os
from PIL import Image, ImageTk
import random
from tkinter import messagebox

class View:
    """defines class for Input and Output View"""

    @staticmethod
    def login(name):
        """gets player's name and returns it (string)"""
        members = View.load_members()
        if name in members.keys():
            tries = members[name][0]
            wins = members[name][1]
            winrate = 100 * wins / tries if tries > 0 else 0
            chips = members[name][2]
            return (name, tries, wins, chips)
        else:
            members[name] = (0,0,0)
            return name, 0, 0, 0

    @staticmethod
    def load_members():
        if os.path.exists("members.txt"):
            file = open("members.txt", "r")
            members = {}
            for line in file:
                member = line.strip('\n').split(',')
                members[member[0]] = (int(member[1]), float(member[2]), int(member[3]))
            file.close()
            return members
        else:
            file = open("members.txt", "a+")
            members = {}
            for line in file:
                member = line.strip('\n').split(',')
                members[member[0]] = (int(member[1]), float(member[2]), int(member[3]))
            file.close()
            return members

    @staticmethod
    def store_members(members):
        file = open("members.txt", "w")
        names = members.keys()
        for name in names:
            tries, wins, chips = members[name]
            line = name + ',' + str(tries) + ',' + \
                   str(wins) + ',' + str(chips) + '\n'
            file.write(line)
        file.close()

    @staticmethod
    def show_top5():
        members = View.load_members()
        sorted_members = sorted(members.items(),\
                                key=lambda x: x[1][2],\
                                reverse=True)
        #sorted_members=[[a,(1,23,31)],[b,(213,4,5)]]
        s = []
        if len(sorted_members) < 5:
            for i in range(len(sorted_members)):
                s.append(sorted_members[i])
        else:
            for i in range(5):
                s.append(sorted_members[i])
        return s

class Hand:
    """defines Hand class"""
    def __init__(self, name="Dealer"):
        """creates player/dealer's empty hand
        argument: name -- player's name in string (default: 'Dealer')
        """
        self.__name = name

    @property
    def name(self):
        """its name : either player's name or 'Dealer'"""
        return self.__name

class BlackjackController:
    """defines Blackjack game controller class"""
    def __init__(self, name, chips):
        """creates player/dealer's empty hand and a deck of cards
        argument: name -- player' name in string (default: 'Dealer')
        """
        self.__player = Hand(name)
        self.__dealer = Hand()
        self.__deck = Deck()
        self.__tries = 0
        self.__wins = 0
        self.__chips = chips

    @property
    def tries(self):
        return self.__tries

    @property
    def wins(self):
        return self.__wins

    @property
    def chips(self):
        return self.__chips

class Play:
    name = ""

    @staticmethod
    def getName(name):
        Play.name = name

class Login(Frame):
    def __init__(self, master):
        super().__init__(master, height = 700, width = 700)
        master.geometry('600x600')
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        image = Image.open("casino_bg.gif")
        self.imageP = ImageTk.PhotoImage(image)
        l = Label(self, image=self.imageP)
        l.image = self.imageP
        l.place(x = 0, y = 0)
        self.title = Label(self, text="Welcome to SMaSH Casino!", font = ("Times", "30"), bg = "black", fg = "white")
        self.title.place(x=130,y=200)
        self.name = Label(self, text="Name", font = ("Times", "24"), bg  = "black" ,fg = "white")
        self.name.place(x=110,y=260)
        self.login_entry = Entry(self, width=20, bg = "black", fg = "white", highlightbackground = "black")
        self.login_entry.place(x=210,y=265)
        self.login_photo = PhotoImage(file = "login.gif")
        self.button_login = Button(self, image = self.login_photo ,command = self.game_login, highlightbackground = "black")
        self.button_login.place(x=440,y=260)
        self.summary_window = Text(self, width = 25, height = 6, wrap = WORD, bg = "black", fg = "white", font = ("Times", "20"))
        self.summary_window.place(x=180,y=310)
        self.start_photo = PhotoImage(file = "start.gif")
        self.button_play = Button(self, image = self. start_photo , command = self.game_start, highlightbackground = "black")
        self.button_play.place(x=75,y=500)


    def game_login(self):
        name = Play.getName(self.login_entry.get())
        name, tries, wins, chips = View.login(Play.name)
        self.__tries = tries
        self.__wins = wins
        self.__chips = chips
        self.game = BlackjackController(name, chips)
        record = "Name : " + Play.name + "\n"
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

class Game(Frame):
    __rank=('A','2','3','4','5','6','7','8','9','10','J','K','Q')
    def __init__(self,master):
        super().__init__(master,width=800,height=600)
        master.geometry('800x600')
        self.master = master
        self.__deck = Card.fresh_deck()
        self.pack()
        self.create_widgets()

        self.pack()

        name, tries, wins, chips = View.login(Play.name)

        self.__player = Hand(Play.name)
        self.__dealer = Hand()
        self.__tries = tries
        self.__wins = wins
        self.__chips = chips
        self.__tries += 1
        self.i = 2
        self.j = 2
        self.a = 1
        self.click_hit = 0
        self.point_dealer = 0
        self.point_player = 0
        self.__value = 0
        self.__value1 = 0


    def dealer_total(self):
        self.point_dealer = 0
        for i in range(len(self.dealer_deck)):
            self.__value = Game.__rank.index(self.dealer_deck[i][0].rank) + 1
            if self.__value > 10:
                self.__value = 10
            number_of_ace = 0
            if self.dealer_deck[i][0].rank == 'A':
                self.point_dealer += 11
                number_of_ace += 1
            else:
                self.point_dealer += self.__value
            while self.point_dealer > 21 and number_of_ace > 0:
                self.point_dealer -= 10
                number_of_ace -= 1
        print("dealer point",self.point_dealer)
        return self.point_dealer

    def player_total(self):
        self.point_player = 0
        for i in range(len(self.player_deck)):
            self.__value1 = Game.__rank.index(self.player_deck[i][0].rank) + 1
            if self.__value1 > 10:
                self.__value1 = 10
            number_of_ace = 0
            if self.player_deck[i][0].rank == 'A':
                self.point_player += 11
                number_of_ace += 1
            else:
                self.point_player += self.__value1
            while self.point_player > 21 and number_of_ace > 0:
                self.point_player -= 10
                number_of_ace -= 1
        return self.point_player

    @property
    def tries(self):
        return self.__tries

    @property
    def wins(self):
        return self.__wins

    @property
    def chips(self):
        return self.__chips


    def create_widgets(self):
        self.dealer_deck = []
        self.deck_photo1=[None] * 10
        for i in range(2):
            self.s = self.__deck.pop()
            self.dealer_deck.append(self.s)
            if i == 0:
                self.deck_photo1[i] = PhotoImage(file="back192.gif")
            else:
                self.deck_photo1[i] = PhotoImage(file=self.s[1])
            self.out_photo1 = Label(self,image=self.deck_photo1[i])
            self.out_photo1.place(x = 200 + i * 20, y = 80)

        self.deck_photo=PhotoImage(file="back192.gif")
        self.dealer_space = Label(self,text="Dealer's card", font = ("Times", "30"), width=10,bg="black", fg="white")
        self.dealer_space.place(x = 170, y = 10)

        self.deck_button = Button(self,image = self.deck_photo,command=self.hit)
        self.deck_button.place(x = 205, y = 210)

        self.stop_photo = PhotoImage(file = "stop.gif")
        self.stop_button = Button(self, image = self.stop_photo, command=self.stop, highlightbackground = "white")
        self.stop_button.place(x = 100, y = 220)

        self.quit_photo = PhotoImage(file = "exit.gif")
        self.quit_button = Button(self, image = self.quit_photo, command=self.quit, highlightbackground = "white")
        self.quit_button.place(x=20,y=450)

        self.player_deck = []
        self.deck_photo2=[None] * 10
        for k in range(2):
            self.s1 = self.__deck.pop()
            self.player_deck.append(self.s1)
            self.deck_photo2[k] = PhotoImage(file=self.s1[1])
            self.out_photo2 = Label(self,image=self.deck_photo2[k])
            self.out_photo2.place(x = 200 + k * 20, y = 350)

        self.player_space = Label(self,text=Play.name+"'s card", font = ("Times", "30"), width=10,bg="black",fg="white")
        self.player_space.place(x = 170, y = 460)

        player_total = self.player_total()
        dealer_total = self.dealer_total()
        print("player total0 : ",player_total)
        print("dealer total0 : ",dealer_total)

        if player_total == 21 and dealer_total != 21:
            text = "BLACKJACK! You WIN!!"
            messagebox.showinfo("GAME RESULT" , text)
            self.__chips += 2
            self.__wins += 1
            self.stop2()

        elif player_total == 21 and dealer_total == 21:
            self.stop2()
            text = "Draw"
            messagebox.showinfo("GAME RESULT" , text)
            self.__wins += 0.5


    def hit(self):
        self.click_hit += 1
        self.s1 = self.__deck.pop()
        self.player_deck.append(self.s1)
        self.deck_photo2[self.i] = PhotoImage(file=self.s1[1])
        self.out_photo2 = Label(self,image=self.deck_photo2[self.i])
        self.out_photo2.place(x = 220 + self.click_hit * 20, y = 350)
        self.i += 1
        player_total = 0
        player_total = self.player_total()
        print("player total1 : ",player_total)
        dealer_total = self.dealer_total()
        if player_total > 21:
            self.stop2()
            text = "Burst! You LOSE;()"
            messagebox.showinfo("GAME RESULT" , text)
            self.__chips -= 1

    def stop2(self):
        self.stop_button.destroy()
        self.more_photo = PhotoImage(file = "replay.gif")
        self.more_button = Button(self,image = self.more_photo,command=self.more)
        self.more_button.place(x = 100, y = 250)
        self.deck_button.destroy()
        self.deck_photo1[0] = PhotoImage(file=self.dealer_deck[0][1])
        self.out_photo1 = Label(self,image=self.deck_photo1[0])
        self.out_photo1.place(x = 100, y = 80)
        dealer_total = self.dealer_total()
        if dealer_total == 21:
            text = "Dealer BLACKJACK! You LOSE;()"
            messagebox.showinfo("GAME RESULT", text)
            self.__chips -= 1
        while dealer_total < 17:
            self.s = self.__deck.pop()
            self.dealer_deck.append(self.s)
            self.deck_photo1[self.j] = PhotoImage(file=self.s[1])
            self.out_photo1 = Label(self,image=self.deck_photo1[self.j])
            self.out_photo1.place(x = 220 + self.a * 20, y = 80)
            self.j += 1
            self.a += 1
            dealer_total = 0
            dealer_total = self.dealer_total()

    def stop(self):
        self.stop2()
        player_total = self.player_total()
        dealer_total = self.dealer_total()
        if dealer_total > 21:
            text = "Dealer Burst! You WIN!!"
            messagebox.showinfo("GAME RESULT" , text)
            self.__chips += 1
            self.__wins += 1
        elif dealer_total < 21:
            if dealer_total == player_total:
                text = "Draw"
                messagebox.showinfo("GAME RESULT" , text)
                self.__wins += 0.5
            elif dealer_total > player_total:
                text = "I'm sorry. You LOSE;()"
                messagebox.showinfo("GAME RESULT" , text)
                self.__chips -= 1
            else:
                text = "Congretulation! You WIN!!"
                messagebox.showinfo("GAME RESULT" , text)
                self.__chips += 1
                self.__wins += 1


    def more(self):
        self.__tries += 1
        self.click_hit = 0
        self.i = 2
        self.j = 2
        self.a = 1
        self.more_button.destroy()
        self.__deck = Card.fresh_deck()
        self.create_widgets()

    def quit(self):
        members = View.load_members()
        members[Play.name] = (self.tries,self.wins,self.chips)
        print(members[Play.name])
        View.store_members(members)
        ls = View.show_top5()
        text = ""
        for i in range(len(ls)) :
            text += str(i+1) + ". " + "name : " + ls[i][0] + " , tries : " + str(ls[i][1][0]) + " , wins : " + str(ls[i][1][1]) + " , chips : " + str(ls[i][1][2]) +"\n"
        messagebox.showinfo("RANKING" , text)
        root.quit()




class Card:

    """returns a brand-new deck of shuffled cards with all face down"""
    __suit=('Diamond','Heart','Clover','Spade')
    __rank=('A','2','3','4','5','6','7','8','9','10','J','K','Q')

    def __init__(self, cardImage, rank):
        self.__rank = rank
        self.__cardImage = cardImage

    @property
    def rank(self):
        return self.__rank

    @property
    def suit(self):
        """its suit value in Card.__suits"""
        return self.__suit

    @property
    def cardImage(self):
        return self.__cardImage

    @staticmethod
    def fresh_deck():
        cards = []
        cardsImage = []
        cards_match = []
        for s in Card.__suit:
            for v in Card.__rank:
                new_card = Card(s,v)
                image_path = s+v+".gif"
                cards.append(new_card)
                cardsImage.append(image_path)
                cards_match.append((new_card, image_path))
        random.shuffle(cards_match)
        return cards_match

class Deck:
    """defines Deck class"""
    def __init__(self):
        """creates a deck object consisting of 52 shuffled cards
        with all face down"""
        self.__deck = Card.fresh_deck()

root=Tk()
root.title("Blackjack")
root.resizable(width=False, height=False)
#root.configure(bg = "black")
Login(root)
root.mainloop()
