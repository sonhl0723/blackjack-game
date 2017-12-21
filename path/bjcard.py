import random

class Card:
    """defines Card class"""
    __suits = ("Diamond", "Heart", "Spade", "Clover")
    __ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    
    def __init__(self, suit, rank, face_up=True):
        """creates a playing card object 
        arguments:
        suit -- must be in Card.__suits
        rank -- must be in Card.__ranks
        face_up -- True or False (defaut True)
        """
        if suit in Card.__suits and rank in Card.__ranks:
            self.__suit = suit
            self.__rank = rank
            self.__face_up = face_up
        else:
            print("Error: Not a valid card")
        self.__value = Card.__ranks.index(self.__rank) + 1
        if self.__value > 10:
            self.__value = 10

    def __str__(self):
        """returns its string representation"""
        if self.__face_up:
            return self.__suit + "." + self.__rank
        else:
            return "xxxxx" + "." + "xx"

    @property
    def suit(self):
        """its suit value in Card.__suits"""
        return self.__suit

    @property
    def rank(self):
        """its rank value in Card.__ranks"""
        return self.__rank

    @property
    def face_up(self):
        """its face_up value : True or False"""
        return self.__face_up

    @property
    def value(self):
        """its face value according to blackjack rule"""
        return self.__value

    def flip(self):
        """flips itself"""
        self.__face_up = not self.__face_up

    @staticmethod
    def fresh_deck():
        """returns a brand-new deck of shuffled cards with all face down"""
        cards = []
        for s in Card.__suits:
            for r in Card.__ranks:
                cards.append(Card(s,r,False))
        random.shuffle(cards)
        return cards

class Deck:
    """defines Deck class"""
    def __init__(self):
        """creates a deck object consisting of 52 shuffled cards 
        with all face down"""
        self.__deck = Card.fresh_deck()
        print("<< A brand-new deck of card! >>")


    def next(self, open=True):
        """removes a card from deck and returns the card
        with its face up if open == True, or 
        with its face down if open == False
        """
        if self.__deck == []:
            self.__deck = Card.fresh_deck()
            print("<< A brand-new deck of card! >>")
        card = self.__deck.pop()
        if open :
            card.flip()
        return card
