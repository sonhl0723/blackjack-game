# Blackjack Game Contoller
from bjcard import Deck
from bjhand import *
from bjview import *

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

    @staticmethod
    def main():
      # main procedure
        print("Welcome to SMaSH Casino!")
        name, tries, wins, chips = View.login()
        game = BlackjackController(name, chips)
        while True:
            game.play()
            if not View.ox("Play more, " + name + "? (o/x) "):
                break
        print('-----')
        print('You played', game.tries, 'games and won', game.wins, 'of them.')
        members = View.load_members()
        members[name] = (tries + game.tries, wins + game.wins, game.chips)
        View.store_members(members)
        View.show_tvop5()
        print("Bye, " + name + "!")