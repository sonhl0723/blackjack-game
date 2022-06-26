from conf import *

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
        """ match card attribute and card image"""
        cards = []
        cardsImage = []
        cards_match = []
        for s in Card.__suit:
            for v in Card.__rank:
                new_card = Card(s,v)
                image_path = "./card_img/"+s+v+".gif"
                cards.append(new_card)
                cardsImage.append(image_path)
                cards_match.append((new_card, image_path))
        random.shuffle(cards_match)
        return cards_match