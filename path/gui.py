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
        sorted_members = sorted(members.items(),\
                                key=lambda x: x[1][2],\
                                reverse=True)
        #sorted_members=[[a,(1,23,31)],[b,(213,4,5)]]
        s = []
        if len(sorted_members) < 5:
            for i in range(len(sorted_members)):
                s.append(sorted_members[i][0])
        else:
            for i in range(5):
                s.append(sorted_members[i][0])
        # rank = 1
        # for member in sorted_members[:5]:
        #     chips = member[1][2]
        #     if chips <= 0:
        #         break
        #     rank += 1
        return s

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


    # def play(self):
    #     """plays a round of blackjack game"""
    #     print("== new game ==")
    #     self.__tries += 1
    #     player = self.__player
    #     dealer = self.__dealer
    #     deck = self.__deck
    #     player.get(deck.next())
    #     dealer.get(deck.next())
    #     player.get(deck.next())
    #     dealer.get(deck.next(open=False))
    #     print("Dealer :", dealer)
    #     print(player.name, ":", player)
    #     if player.total == 21:
    #         print("Blackjack!", player.name, "wins.")
    #         self.__chips += 2
    #         self.__wins += 1
    #     else:
    #         while player.total < 21 and View.ox(Play.name + ": Hit?(o/x) "):
    #             player.get(deck.next())
    #             print(player.name, ":", player)
    #         if player.total > 21:
    #             print(player.name, "busts!")
    #             self.__chips -= 1
    #         else:
    #             while dealer.total <= 16:
    #                 dealer.get(deck.next())
    #             if dealer.total > 21:
    #                 print("Dealer busts!")
    #                 self.__chips += 1
    #                 self.__wins += 1
    #             elif dealer.total == player.total:
    #                 print("We draw.")
    #                 self.__wins += 0.5
    #             elif dealer.total > player.total:
    #                 print(player.name, "loses.")
    #                 self.__chips -= 1
    #             else:
    #                 print(player.name, "wins.")
    #                 self.__chips += 1
    #                 self.__wins += 1
    #         dealer.open()
    #         print("Dealer :", dealer)
    #     print("Your have", self.__chips, "chips.")
    #     player.clear()
    #     dealer.clear()

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
    #     self.__tries = 0
    #     self.__wins = 0

    # @property
    # def tries(self):
    #     return self.__tries

    # @property
    # def wins(self):
    #     return self.__wins

    # @property
    # def chips(self):
    #     return self.__chips

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
        super().__init__(master,width=500,height=500)
        master.geometry('800x600')
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
        self.click_hit = 0
        self.click_stop = 0
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
        self.dealer_space = Label(self,text="Dealer's card",width=10,bg="black", fg="white")
        self.dealer_space.place(x = 200, y = 10)

        self.deck_button = Button(self,image = self.deck_photo,command=self.hit)
        self.deck_button.place(x = 205, y = 210)

        self.stop_button = Button(self,text="STOP", command=self.stop)
        self.stop_button.place(x = 100, y = 250)

        self.quit_button = Button(self, text="QUIT", command=self.quit)
        self.quit_button.place(x=440,y=465)

        self.player_deck = []
        self.deck_photo2=[None] * 10
        for k in range(2):
            self.s1 = self.__deck.pop()
            self.player_deck.append(self.s1)
            self.deck_photo2[k] = PhotoImage(file=self.s1[1])
            self.out_photo2 = Label(self,image=self.deck_photo2[k])
            self.out_photo2.place(x = 200 + k * 20, y = 350)

        self.player_space = Label(self,text=Play.name+"'s card",width=10,bg="black",fg="white")
        self.player_space.place(x = 200, y = 480)

        player_total = self.player_total()
        dealer_total = self.dealer_total()
        print("player total0 : ",player_total)
        print("dealer total0 : ",dealer_total)

        if player_total == 21:
            text = "BLACKJACK! You WIN!!"
            messagebox.showinfo("GAME RESULT" , text)
            self.__chips += 2
            self.__wins += 1
            self.deck_photo1[0] = PhotoImage(file=self.dealer_deck[0][1])
            self.out_photo1 = Label(self,image=self.deck_photo1[0])
            self.out_photo1.place(x = 100, y = 80)
            self.stop2()

    def hit(self):
        self.click_hit += 1
        player_total = self.player_total()
        dealer_total = self.dealer_total()
        if player_total < 21:
            self.s1 = self.__deck.pop()
            self.player_deck.append(self.s1)
            print(self.i)
            self.deck_photo2[self.i] = PhotoImage(file=self.s1[1])
            self.out_photo2 = Label(self,image=self.deck_photo2[self.i])
            self.out_photo2.place(x = 220 + self.click_hit * 20, y = 350)
            self.i += 1
            player_total = 0
            player_total = self.player_total()
            print("palyer total",player_total)
        if player_total > 21:
            self.p_burst = Label(self,text="You Burst")
            self.p_burst.place(x = 300, y = 280)
            self.__chips -= 1
            self.deck_photo1[0] = PhotoImage(file=self.dealer_deck[0][1])
            print(self.dealer_deck[0][1])
            self.out_photo1 = Label(self,image=self.deck_photo1[0])
            self.out_photo1.place(x = 100, y = 80)
            self.stop2()

    def stop2(self):
        self.stop_button.destroy()
        self.more_button = Button(self,text="MORE?",command=self.more)
        self.more_button.place(x = 100, y = 250)
        self.deck_button.destroy()
        self.deck_photo1[0] = PhotoImage(file=self.dealer_deck[0][1])
        self.out_photo1 = Label(self,image=self.deck_photo1[0])
        self.out_photo1.place(x = 100, y = 80)

    def stop(self):
        self.stop_button.destroy()
        self.more_button = Button(self,text="MORE?",command=self.more)
        self.more_button.place(x = 100, y = 250)
        self.deck_button.destroy()
        self.deck_photo1[0] = PhotoImage(file=self.dealer_deck[0][1])
        self.out_photo1 = Label(self,image=self.deck_photo1[0])
        self.out_photo1.place(x = 100, y = 80)
        player_total = self.player_total()
        dealer_total = self.dealer_total()
        self.click_stop += 1
        if dealer_total == 21:
            self.dealer_blackjack = Label(self, text="Dealer Blackjack")
            self.dealer_blackjack.place(x = 300, y = 280)
            self.__chips -= 2
            self.__wins -= 1
        if dealer_total > 21:
            print("dealer total >21 ",dealer_total)
            self.dealer_burst = Label(self,text="Dealer Bust!")
            self.dealer_burst.place(x = 300, y = 280)
            self.__chips += 1
            self.__wins += 1
        else:
            while dealer_total < 17:
                self.s = self.__deck.pop()
                self.dealer_deck.append(self.s)
                self.deck_photo1[self.j] = PhotoImage(file=self.s[1])
                self.out_photo1 = Label(self,image=self.deck_photo1[self.j])
                self.out_photo1.place(x = 220 + self.click_stop * 20, y = 80)
                self.click_stop = 0
                self.j += 1
                dealer_total = 0
                dealer_total = self.dealer_total()
            if dealer_total > 21:
                print("dealer total >21 ",dealer_total)
                self.dealer_burst = Label(self,text="Dealer Bust!")
                self.dealer_burst.place(x = 300, y = 280)
                self.__chips += 1
                self.__wins += 1
            elif dealer_total == player_total:
                self.draw1 = Label(self,text="Draw")
                self.draw1.place(x = 300, y = 280)
                self.__wins += 0.5
            elif dealer_total > player_total:
                self.lose1 = Label(self,text="You Lose!!!")
                self.lose1.place(x = 300, y = 280)
                self.__chips -= 1
            else:
                self.win1 = Label(self,text="You Win!")
                self.win1.place(x = 300, y = 280)
                self.__chips += 1
                self.__wins += 1


    def more(self):
        self.__tries += 1
        self.box = Label(self,text="@@@@@@@@@@@@@@@",bg="white",fg="white")
        self.click_stop = 0
        self.click_hit = 0
        self.box.place(x = 300, y = 280)
        self.more_button.destroy()
        self.__deck = Card.fresh_deck()
        self.i=2
        self.j=2
        self.create_widgets()

    def quit(self):
        members = View.load_members()
        members[Play.name] = (self.tries,self.wins,self.chips)
        View.store_members(members)
        ls = View.show_top5()
        text = ""
        # 1. Yang
        for i in range(len(ls)) :
            text += str(i+1) + ". " + ls[i] +"\n"
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
    def face_up(self):
        """its face_up value : True or False"""
        return self.__face_up

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

    def pop(self):
        return self.__deck.pop()

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
#root.configure(bg = "black")
Login(root)
root.mainloop()
