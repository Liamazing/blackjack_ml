from suit import Suit
from face import Face


class Card(object):
    """Class to represent a playing card."""

    def __init__(self, suit, face):
        self._suit = Suit.spades
        for s in Suit:
            if suit in {s, s.value, s.name}:
                self._suit = s
                break
        self._face = Face.ace
        self._face = -1
        for f in Face:
            if face in {f, f.value, s.name}:
                self._face = f

    def __str__(self):
        return self._face.name + " of " + self._suit.name

