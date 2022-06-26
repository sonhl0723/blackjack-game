from conf import *
import conf
from card import Card
from play import *

class Game(Frame):
    __rank=('A','2','3','4','5','6','7','8','9','10','J','K','Q')
    def __init__(self,master):
        """create a frame of new window for playing game"""
        super().__init__(master, width=600,height=600)
        master.geometry('600x600')
        self.master = master
        self.__deck = Card.fresh_deck()
        self.pack()
        self.create_widgets()
        self.pack()

        _, tries, wins, chips = View.get_record(Player.name)

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
        """calculate dealer's total"""
        self.point_dealer = 0
        number_of_ace = 0
        for i in range(len(self.dealer_deck)):
            self.__value = Game.__rank.index(self.dealer_deck[i][0].rank) + 1
            if self.__value > 10:
                self.__value = 10
            if self.dealer_deck[i][0].rank == 'A':
                self.point_dealer += 11
                number_of_ace += 1
            else:
                self.point_dealer += self.__value
            while self.point_dealer > 21 and number_of_ace > 0:
                self.point_dealer -= 10
                number_of_ace -= 1
        print(self.point_dealer)
        return self.point_dealer

    def player_total(self):
        """calculate player total"""
        self.point_player = 0
        number_of_ace = 0
        for i in range(len(self.player_deck)):
            self.__value1 = Game.__rank.index(self.player_deck[i][0].rank) + 1
            if self.__value1 > 10:
                self.__value1 = 10
            if self.player_deck[i][0].rank == 'A':
                self.point_player += 11
                number_of_ace += 1
            else:
                self.point_player += self.__value1
            while self.point_player > 21 and number_of_ace > 0:
                self.point_player -= 10
                number_of_ace -= 1
        print(self.point_player)
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
        """Give two cards to dealer and player make dealer deck and player deck 
        Create stop button and hit button Distinct that player is blackjack or draw"""
        self.dealer_deck = []
        self.deck_photo1=[None] * 10
        for i in range(2):
            self.s = self.__deck.pop()
            self.dealer_deck.append(self.s)
            if i == 0:
                self.deck_photo1[i] = PhotoImage(file="./card_img/back192.gif")
            else:
                self.deck_photo1[i] = PhotoImage(file=self.s[1])
            self.out_photo1 = Label(self,image=self.deck_photo1[i])
            self.out_photo1.place(x = 230 + i * 20, y = 80)

        self.deck_photo=PhotoImage(file="./card_img/back192.gif")
        self.dealer_space = Label(self,text="Dealer's card", font = ("Times", "30"), width=10,bg="black", fg="white")
        self.dealer_space.place(x = 200, y = 10)

        self.deck_button = Button(self,image = self.deck_photo,command=self.hit)
        self.deck_button.place(x = 240, y = 210)

        self.stop_photo = PhotoImage(file = "./game_img/stop.gif")
        self.stop_button = Button(self, image = self.stop_photo, command=self.stop, highlightbackground = "white")
        self.stop_button.place(x = 100, y = 220)


        self.player_deck = []
        self.deck_photo2=[None] * 10
        for k in range(2):
            self.s1 = self.__deck.pop()
            self.player_deck.append(self.s1)
            self.deck_photo2[k] = PhotoImage(file=self.s1[1])
            self.out_photo2 = Label(self,image=self.deck_photo2[k])
            self.out_photo2.place(x = 230 + k * 20, y = 350)

        self.player_space = Label(self,text=Player.name+"'s card", font = ("Times", "30"), width=10,bg="black",fg="white")
        self.player_space.place(x = 200, y = 500)

        player_total = self.player_total()
        dealer_total = self.dealer_total()

        if player_total == 21 and dealer_total != 21:
            self.stop2()
            text = "BLACKJACK! You WIN!!"
            messagebox.showinfo("GAME RESULT" , text)
            self.__chips += 2
            self.__wins += 1

        elif player_total == 21 and dealer_total == 21:
            self.stop2()
            text = "Draw"
            messagebox.showinfo("GAME RESULT" , text)
            self.__wins += 0.5


    def hit(self):
        """Give random card to player deck carculate player total and dealer total
        Distinct that player is burst"""
        self.click_hit += 1
        self.s1 = self.__deck.pop()
        self.player_deck.append(self.s1)
        self.deck_photo2[self.i] = PhotoImage(file=self.s1[1])
        self.out_photo2 = Label(self,image=self.deck_photo2[self.i])
        self.out_photo2.place(x = 250 + self.click_hit * 20, y = 350)
        self.i += 1
        player_total = 0
        player_total = self.player_total()
        dealer_total = self.dealer_total()
        if player_total > 21:
            self.flip()
            text = "Burst! You LOSE;("
            messagebox.showinfo("GAME RESULT" , text)
            self.__chips -= 1

    def stop2(self):
        """Destroy stop button and flip dealer's first card"""
        self.flip()
        dealer_total = self.dealer_total()
        if dealer_total == 21:
            text = "Dealer BLACKJACK! You LOSE;("
            messagebox.showinfo("GAME RESULT", text)
            self.__chips -= 1
        while dealer_total < 17:
            self.s = self.__deck.pop()
            self.dealer_deck.append(self.s)
            self.deck_photo1[self.j] = PhotoImage(file=self.s[1])
            self.out_photo1 = Label(self,image=self.deck_photo1[self.j])
            self.out_photo1.place(x = 250 + self.a * 20, y = 80)
            self.j += 1
            self.a += 1
            dealer_total = 0
            dealer_total = self.dealer_total()

    def stop(self):
        """Distinct that dealer is burst or Compare dealer total and player total"""
        self.stop2()
        player_total = self.player_total()
        dealer_total = self.dealer_total()
        if dealer_total > 21:
            text = "Dealer Burst! You WIN!!"
            time.sleep(0.5)
            messagebox.showinfo("GAME RESULT" , text)
            self.__chips += 1
            self.__wins += 1
        elif dealer_total <= 21:
            if dealer_total == player_total:
                text = "Draw"
                time.sleep(0.5)
                messagebox.showinfo("GAME RESULT" , text)
                self.__wins += 0.5
            elif dealer_total > player_total:
                time.sleep(0.5)
                text = "I'm sorry. You LOSE;("
                messagebox.showinfo("GAME RESULT" , text)
                self.__chips -= 1
            else:
                time.sleep(0.5)
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
        self.quit_button.destroy()
        self.__deck = Card.fresh_deck()
        self.create_widgets()

    def quit(self):
        members = View.load_members()
        members[Player.name] = (self.tries,self.wins,self.chips)
        View.store_members(members)
        ls = View.show_top5()
        text = ""
        for i in range(len(ls)) :
            text += str(i+1) + ". " + "Name: " + ls[i][0] + " , Tries: " + str(ls[i][1][0]) + " , Wins: " + str(ls[i][1][1]) + " , Chips: " + str(ls[i][1][2]) +"\n"
        messagebox.showinfo("RANKING" , text)

        conf.root.quit()

    def flip(self):
        self.stop_button.destroy()
        self.more_photo = PhotoImage(file = "./game_img/replay.gif")
        self.more_button = Button(self,image = self.more_photo,command=self.more)
        self.more_button.place(x = 160, y = 250)
        self.quit_photo = PhotoImage(file = "./game_img/exit.gif")
        self.quit_button = Button(self, image = self.quit_photo, command=self.quit, highlightbackground = "white")
        self.quit_button.place(x=300,y=240)

        self.deck_button.destroy()
        self.deck_photo1[0] = PhotoImage(file=self.dealer_deck[0][1])
        self.out_photo1 = Label(self,image=self.deck_photo1[0])
        self.out_photo1.place(x = 140, y = 80)