from suit import Suit
from face import Face


class Card(object):
    """Class to represent a playing card."""

    def __init__(self, suit, face):
        self._suit = -1
        for s in Suit:
            if suit in {s, s.value}:
                self._suit = s
                break
        if self._suit < 0:
            self._suit = Suit.spades
        for f in Face:
            if face in {f, f.value}:
