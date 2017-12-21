# from tkinter import*
# from bjcard import Deck
# from bjhand import *
# from bjview import *
# from blackjack import*

# class Login(Frame):
# 	def __init__(self, master):
# 		super().__init__(master)
# 		master.geometry('300x300')
# 		self.master = master
# 		self.pack(padx=20, pady=20)
# 		self.create_widgets()

# 	def create_widgets(self):
# 		self.title = Label(self, text="Welcome to smash Casino!").grid(row=0, column=1)
# 		self.name = Label(self, text="Name").grid(row=2, column=1)
# 		self.login_entry = Entry(self, width=10)
# 		self.login_entry.grid(row=3, column=1)
# 		self.button_login = Button(self, text="login", command=self.game_login)
# 		self.button_login.grid(row=4, column=1)
# 		self.summary = Text(self, width=20, height=10, wrap=WORD)
# 		self.summary.grid(row=5, column =1)
# 		self.button_play = Button(self, text="Play!!", command=self.game_start).grid(row=6, column=1)

# 	def game_login(self):
# 		name = Play.getName(self.login_entry.get())
# 		name, tries, wins, chips = View.login(Play.name)
# 		self.game = BlackjackController(name, chips)
# 		record = "Name : "+Play.name +"\n"
# 		record += "Game Tries : "+ str(tries)+"\n"
# 		record += "Win Games : "+ str(wins)
# 		# record += "Winning Rate : "+round((str(wins)/str(tries))*100,2)
# 		self.summary.insert(0.0, record)
# 		self.button_login.destroy()
# 		# Game(self.master)

# 	def game_start(self):
# 		# game = self.game
# 		# name, tries, wins, chips = View.login(Play.name)
# 		# while True:
# 		# 	game.play()
# 		# 	if not View.ox("Play more, "+ Play.name +"? (o/x) "):
# 		# 		break
# 		# print('-----')
# 		# print('You played', game.tries, 'games and won', game.wins, 'of them.')
# 		# members = View.load_members()
# 		# members[Play.name] = (tries+game.tries, wins+game.wins, game.chips)
# 		# View.store_members(members)
# 		# View.show_top5()
# 		# print("Bye, "+Play.name+"!")
# 		self.destroy()
# 		Game(self.master)
# 		# Play.main(Play.name, chips)

# class Game(Frame):
# 	def __init__(self,master):
# 		super().__init__(master)
# 		master.geometry('400x400')
# 		# self.pack(padx=20,pady=20)
# 		self.pack()
# 		self.create_widgets()
# 		Label(self,text="Dealer").grid(row=0,column=1)
# 		Label(self,text="Player").grid(row=4,column=1)
# 		wall=PhotoImage(file="casino.gif")
# 		wall_label=Label(image=wall)
# 		wall_label.place(x=0,y=0)



# 	def create_widgets(self):
# 		# image = Image.open("casino.gif")
# 		image = image.resize((250, 250), Image.path)
# 		self.imageP = ImageTk.PhotoImage(image)
# 		l = Label(self, image=self.imageP)
# 		l.image = self.imageP
# 		l.grid()

# 		PhotoImage(file=path)
# 		file="{}{}.gif".format(number,symbol)

# root=Tk()
# root.title("Blackjack")
# root.geometry("300x300")
# Login(root)
# root.mainloop()

from tkinter import*
import os
from PIL import Image, ImageTk
import random

class View:
    """defines class for Input and Output View"""

    @staticmethod
    def login(name):
        """gets player's name and returns it (string)"""
        # name = input("Enter your name : (4 letters max) ") 
        # while len(name) > 4:
        #     name = input("Enter your name : (4 letters max) ")
        members = View.load_members()
        if name in members.keys():
            tries = members[name][0]
            wins = members[name][1]
            winrate = 100 * wins / tries if tries > 0 else 0
            chips = members[name][2]
            return name, tries, wins, chips
        else:
            members[name] = (0,0,0)
            return name, 0, 0, 0

    @staticmethod
    def ox(message):
        """returns True if player inputs 'o' or 'O', 
                   False if player inputs 'x' or 'X'"""
        response = input(message).lower()
        while not (response == 'o' or response == 'x'):
            response = input(message).lower()
        return response == 'o'

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
        print('-----')
        sorted_members = sorted(members.items(),\
                                key=lambda x: x[1][2],\
                                reverse=True)
        print("All-time Top 5")
        rank = 1
        for member in sorted_members[:5]:
            chips = member[1][2]
            if chips <= 0:
                break
            print(rank, '.', member[0], ':', chips)
            rank += 1

    # @staticmethod
    # def get_number(message,low,high):
    #     response = input(message)
    #     while not (response.isdigit() and low <= int(response) <= high):
    #         response = input(message)
    #     return int(response)

class Hand:
    """defines Hand class"""
    def __init__(self, name="Dealer"):
        """creates player/dealer's empty hand
        argument: name -- player's name in string (default: 'Dealer')
        """
        self.__name = name
        self.__hand = []
        
    def __str__(self):
        """returns its string representation"""
        if len(self.__hand) == 0:
            show = "empty"
        else:
            show = ""
            for card in self.__hand:
                show += str(card) + " "
        return show

    @property
    def name(self):
        """its name : either player's name or 'Dealer'"""
        return self.__name

    @property
    def total(self):
        """the total value of its hand"""
        point = 0
        number_of_ace = 0
        for card in self.__hand:
            if card.rank == 'A':
                point += 11
                number_of_ace += 1
            else:
                point += card.value
        while point > 21 and number_of_ace > 0:
            point -= 10
            number_of_ace -= 1
        return point

    def get(self, card):
        """gets a card from deck and puts the card into its hand"""
        self.__hand.append(card)

    def clear(self):
        """empties its hand"""
        self.__hand = []

    def open(self):
        """turns all of its hand's cards' faces up"""
        for card in self.__hand:
            if not card.face_up:
                card.flip()

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


    def play(self):
        """plays a round of blackjack game"""
        print("== new game ==")
        self.__tries += 1
        player = self.__player
        dealer = self.__dealer
        deck = self.__deck
        player.get(deck.next())
        dealer.get(deck.next())
        player.get(deck.next())
        dealer.get(deck.next(open=False))
        print("Dealer :", dealer)
        print(player.name, ":", player)
        if player.total == 21:
            print("Blackjack!", player.name, "wins.")
            self.__chips += 2
            self.__wins += 1
        else:
            while player.total < 21 and View.ox(Play.name + ": Hit?(o/x) "):
                player.get(deck.next())
                print(player.name, ":", player)
            if player.total > 21:
                print(player.name, "busts!")
                self.__chips -= 1
            else:
                while dealer.total <= 16:
                    dealer.get(deck.next())
                if dealer.total > 21:
                    print("Dealer busts!")
                    self.__chips += 1
                    self.__wins += 1
                elif dealer.total == player.total:
                    print("We draw.")
                    self.__wins += 0.5
                elif dealer.total > player.total:
                    print(player.name, "loses.")
                    self.__chips -= 1
                else:
                    print(player.name, "wins.")
                    self.__chips += 1
                    self.__wins += 1
            dealer.open()
            print("Dealer :", dealer)
        print("Your have", self.__chips, "chips.")
        player.clear()
        dealer.clear()

class Play:
    name = ""

    @staticmethod
    def getName(name):
        Play.name = name

class Login(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry('600x600')
        self.master = master
        self.pack(padx=20,pady=20)
        self.create_widgets()
        self.configure(bg='black')
        self.__tries = 0

    @property
    def tries(self):
        return self.__tries

    def create_widgets(self):
        image = Image.open("casino.gif")
        image = image.resize((400, 180), Image.ANTIALIAS)
        self.imageP = ImageTk.PhotoImage(image)
        l = Label(self, image=self.imageP, bg = "black")
        l.image = self.imageP
        l.grid()
        self.title = Label(self, text="Welcome to SMaSH Casino!", bg = "black", fg = "white").grid(row=4, column=0)
        self.name = Label(self, text="Name", bg  = "black" ,fg = "white").grid(row=5, column=0)
        self.login_entry = Entry(self, width=10, bg = "black", fg = "white")
        self.login_entry.grid(row=6, column=0)
        self.login_photo = PhotoImage(file = "login.gif")
        self.button_login = Button(self, text="login",command = self.game_login, bg = "black",pady=5)
        self.button_login.grid(row=7,column=0)
        self.summary_window = Text(self, width = 20, height = 10, wrap = WORD, bg = "black", fg = "white",pady=5)
        self.summary_window.grid(row = 8, column = 0)
        self.start_photo = PhotoImage(file = "start.gif")
        self.button_play = Button(self, text="Start!!", command = self.game_start, bg = "black",pady=5)
        self.button_play.grid(row = 9, column = 0)


    def game_login(self):
        name = Play.getName(self.login_entry.get())
        name, tries, wins, chips = View.login(Play.name)
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
        self.button_login.destroy()

    def game_start(self):
        self.__tries+=1
        self.destroy()
        Game(self.master)

class Game(Frame):
    __rank=('A','2','3','4','5','6','7','8','9','10','J','K','Q')
    def __init__(self,master):
        super().__init__(master,width=500,height=500,bg="black")
        master.geometry('500x500')
        # self.configure(bg="black")
        # self.pack(padx=20,pady=20)
        self.__deck = Card.fresh_deck()
        self.pack()
        self.create_widgets()
        name, tries, wins, chips = View.login(Play.name)
        self.__player = Hand(Play.name)
        self.__dealer = Hand()
        self.__tries = 0
        self.__wins = 0
        self.__chips = chips
        self.i = 2
        self.j = 2

    @property
    def value(self):
        print(self.s1[0].rank)
        print(Game.__rank.index(self.s1[0].rank))
        self.__value = Game.__rank.index(self.s1[0].rank) + 1
        if self.__value > 10:
            self.__value = 10
        return self.__value

    @property
    def value1(self):
        self.value1 = Game.__rank.index(self.s[0].rank) + 1
        if self.__value1 > 10:
            self.__value1 = 10
        return self.value1

    @property
    def tries(self):
        return self.__tries

    @property
    def wins(self):
        return self.__wins

    @property
    def chips(self):
        return self.__chips


    def dealer_total(self):
        """the total value of its hand"""
        point = 0
        number_of_ace = 0
        for card in self.dealer_deck:
            if card.rank == 'A':
                point += 11
                number_of_ace += 1
            else:
                point += self.value1
        while point > 21 and number_of_ace > 0:
            point -= 10
            number_of_ace -= 1
        return point


    def player_total(self):
        point = 0
        number_of_ace = 0
        for card in self.player_deck:
            if card.rank == 'A':
                point += 11
                number_of_ace += 1
            else:
                point += self.value
        while point > 21 and number_of_ace > 0:
            point -= 10
            number_of_ace -= 1
        return point


    # def create_widgets(self):
    #     Label(self,text="Dealer's card",width=10,bg="black", fg="white").place(x=100,y=100)

    def create_widgets(self):
        # image = image.resize((400, 180), Image.ANTIALIAS)
        # self.imageP = ImageTk.PhotoImage(image)
        self.dealer_deck = []
        self.deck_photo1=[None] * 10
        for i in range(2):
            self.s = self.__deck.pop()
            self.dealer_deck.append(self.s[0])
            if i == 1:
                self.deck_photo1[i] = PhotoImage(file="back192.gif")
            else:
                self.deck_photo1[i] = PhotoImage(file=self.s[1])
            self.out_photo1 = Label(self,image=self.deck_photo1[i])
            self.out_photo1.grid(row=50,column=i)

        self.deck_photo=PhotoImage(file="back192.gif")
        self.dealer_space = Label(self,text="Dealer's card",width=10,bg="black", fg="white")
        self.dealer_space.grid(row=0,column=0)

        # self.s = self.__deck.pop()
        # self.deck_photo1 = PhotoImage(file=self.__deck[0][1])
        # self.out_photo1 = Label(self,image=self.deck_photo1)
        # self.out_photo1.grid(row=50,column=0)


        self.deck_button = Button(self,image = self.deck_photo,command=self.hit)
        self.deck_button.grid(row=150,column=0,pady=70)

        self.stop_button = Button(self,text="STOP", command=self.stop)
        self.stop_button.grid(row=150,column=20)

        self.player_deck = []
        self.deck_photo2=[None] * 10
        for k in range(2):
            self.s1 = self.__deck.pop()
            self.player_deck.append(self.s1[0])
            self.deck_photo2[k] = PhotoImage(file=self.s1[1])
            self.out_photo2 = Label(self,image=self.deck_photo2[k])
            self.out_photo2.grid(row=170,column=k)

        self.player_space = Label(self,text=Play.name+"'s card",width=10,bg="black",fg="white")
        self.player_space.grid(row=200,column=0)

    def hit(self):
        if self.player_total() == 21:
            Label(self,text="BLACKJACK!!").grid(row=170,column=0)
            self.__chips += 2
            self.__wins += 1
        else:
            if self.player_total() < 21:
                self.s1 = self.__deck.pop()
                self.player_deck.append(self.s1[0])
                self.deck_photo2[self.i] = PhotoImage(file=self.s1[1])
                self.out_photo2 = Label(self,image=self.deck_photo2[self.i])
                self.out_photo2.grid(row=170,column=self.i)
                self.i+=1
            if self.player_total() > 21:
                Label(self,text="You Bust").pack()
                self.__chips -= 1
            else:
                if self.dealer_total() <= 16:
                    self.s = self.__deck.pop()
                    self.dealer_deck.append(self.s[0])
                    self.deck_photo1[self.j] = PhotoImage(file=self.s[1])
                    self.out_photo1 = Label(self,image=self.deck_photo1[self.j])
                    self.out_photo1.grid(row=50,column=self.j)
                    self.j+=1
                if self.dealer_total() > 21:
                    Label(self,text="Dealer Bust!").grid(row=170,column=0)
                    self.__chips += 1
                    self.__wins += 1
                elif self.dealer_total() == self.player_total():
                    Label(self,text="Draw").grid(row=170,column=0)
                    self.__wins += 0.5
                elif self.dealer_total() > self.player_total():
                    Label(self,text="You Lose").grid(row=170,column=0)
                    self.__chips -= 1
                else:
                    Label(self,text="You Win!").grid(row=170,column=0)
                    self.__chips += 1
                    self.__wins += 1
    def stop(self):
        if self.dealer_total() > 21:
            Label(self,text="Dealer Bust!").grid(row=170,column=0)
            self.__chips += 1
            self.__wins += 1
        elif self.dealer_total() == self.player_total():
            Label(self,text="Draw").grid(row=170,column=0)
            self.__wins += 0.5
        elif self.dealer_total() > self.player_total():
            Label(self,text="You Lose").grid(row=170,column=0)
            self.__chips -= 1
        else:
            Label(self,text="You Win!").grid(row=170,column=0)
            self.__chips += 1
            self.__wins += 1

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
    def face_up(self):
        """its face_up value : True or False"""
        return self.__face_up

    @property
    def value(self):
        """its face value according to blackjack rule"""
        return self.__rank

    def flip(self):
        """flips itself"""
        self.__face_up = not self.__face_up


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
                image_path = 'path/'+s+v+".gif"
                cards.append(new_card)
                cardsImage.append(image_path)
                cards_match.append((new_card, image_path))
        random.shuffle(cards_match)
        return cards_match

    # @staticmethod
    # def match_image():



class Deck:
    """defines Deck class"""
    def __init__(self):
        """creates a deck object consisting of 52 shuffled cards 
        with all face down"""
        self.__deck = Card.fresh_deck()

    # def pop(self):
    #     return self.__deck.pop()

    def next(self, open=True):
        """removes a card from deck and returns the card
        with its face up if open == True, or 
        with its face down if open == False
        """
        if self.__deck == []:
            self.__deck = Card.fresh_deck()
        card = self.__deck.pop()
        if open :
            card.flip()
        return card
                

root=Tk()
root.title("Blackjack")
root.resizable(width=False, height=False)
root.configure(bg = "black")
Login(root)
root.mainloop()