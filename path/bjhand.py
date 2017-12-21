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




