class Card:
    def __init__(self):
        self.card_name = ""
        self.card_id = ""
        self.card_sets = []
        self.card_prints = []

    def set_card_data(self, card_name, card_id):
        self.card_name = card_name
        self.card_id = card_id

    def set_card_sets(self, card_sets):
        self.card_sets = card_sets

    def set_card_prints(self, card_prints):
        self.card_prints = card_prints
