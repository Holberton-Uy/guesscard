class Card:

    __suits = {'CLUBS': {'symbol':'\u2663', 'color': 'black'}, 
               'HEARTS': {'symbol':'\u2665', 'color': 'red'}, 
               'DIAMONDS': {'symbol':'\u2666', 'color': 'red'}, 
               'SPADES': {'symbol':'\u2660', 'color': 'black'}}
    __orders = {'ACE':1, 'QUEEN':10, 'JACK':11, 'KING':12}

    def __init__(self, **kwargs):
        global suits, orders
        if kwargs:
            self.__value = kwargs['value']
            self.__suit = Card.__suits[kwargs['suit']]
            self.__code = kwargs['code']
            try:
                self.__order = int(self.__value)
            except ValueError:
                self.__order = Card.__orders[self.__value]

    @property
    def value(self):
        return self.__value
    
    @property
    def suit(self):
        return self.__suit
    
    @property
    def order(self):
        return self.__order

    def __str__(self):
        return f"{self.value} {self.suit['symbol']}"

    # Redefine comparadores
    def __eq__(self, __value):
        return self.order == __value.order
    
    def __ge__(self, __value):
        return self.order >= __value.order

    def __le__(self, __value):
        return self.order <= __value.order
    
    def __gt__(self, __value):
        return self.order > __value.order
    
    def __lt__(self, __value):
        return self.order < __value.order