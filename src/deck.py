from card import Card
from suit import Suit
from face import Face
from random import shuffle


class Deck(object):

    def __init__(self):
        self._ctnr = []
        for suit in Suit:
            for face in Face:
                self._ctnr.append(Card(suit, face))
        self._shuffle()

    def _shuffle(self):
        shuffle(self._ctnr)

    def deal(self):
        return self._ctnr.pop

    def __str__(self):
        return '\n'.join(str(card) for card in self._ctnr)
