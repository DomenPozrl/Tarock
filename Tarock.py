import random
import copy

class Tarock:
    def __init__(self):
        self.id_to_cards = {
            4: "1\u2665",
            3: "2\u2665",
            2: "3\u2665",
            1: "4\u2665",
            5: "B\u2665",
            6: "C\u2665",
            7: "Q\u2665",
            8: "K\u2665",
            14: "1\u2666",
            13: "2\u2666",
            12: "3\u2666",
            11: "4\u2666",
            15: "B\u2666",
            16: "C\u2666",
            17: "Q\u2666",
            18: "K\u2666",
            21: "7\u2660",
            22: "8\u2660",
            23: "9\u2660",
            24: "10\u2660",
            25: "B\u2660",
            26: "C\u2660",
            27: "Q\u2660",
            28: "K\u2660",
            31: "7\u2663",
            32: "8\u2663",
            33: "9\u2663",
            34: "10\u2663",
            35: "B\u2663",
            36: "C\u2663",
            37: "Q\u2663",
            38: "K\u2663",
            40: "I",
            41: "II",
            42: "III",
            43: "IV",
            44: "V",
            45: "VI",
            46: "VII",
            47: "VIII",
            48: "IX",
            49: "X",
            50: "XI",
            51: "XII",
            52: "XIII",
            53: "XIV",
            54: "XV",
            55: "XVI",
            56: "XVII",
            57: "XVIII",
            58: "XIX",
            59: "XX",
            60: "XXI",
            61: "ŠKIS",
        }
        self.cards_to_id = {
            "1\u2665": 4,
            "2\u2665": 3,
            "3\u2665": 2,
            "4\u2665": 1,
            "B\u2665": 5,
            "C\u2665": 6,
            "Q\u2665": 7,
            "K\u2665": 8,
            "1\u2666": 14,
            "2\u2666": 13,
            "3\u2666": 12,
            "4\u2666": 11,
            "B\u2666": 15,
            "C\u2666": 16,
            "Q\u2666": 17,
            "K\u2666": 18,
            "7\u2660": 21,
            "8\u2660":22,
            "9\u2660": 23,
            "10\u2660": 24,
            "B\u2660": 25,
            "C\u2660": 26,
            "Q\u2660": 27,
            "K\u2660": 28,
            "7\u2663": 31,
            "8\u2663": 32,
            "9\u2663": 33,
            "10\u2663": 34,
            "B\u2663": 35,
            "C\u2663": 36,
            "Q\u2663": 37,
            "K\u2663": 38,
            "I": 40,
            "II": 41,
            "III": 42,
            "IV": 43,
            "V": 44,
            "VI": 45,
            "VII": 46,
            "VIII": 47,
            "IX": 48,
            "X": 49,
            "XI": 50,
            "XII": 51,
            "XIII": 52,
            "XIV": 53,
            "XV": 54,
            "XVI": 55,
            "XVII": 56,
            "XVIII": 57,
            "XIX": 58,
            "XX": 59,
            "XXI":60,
            "ŠKIS":61,
        }

    
    def isHeart(self, karta_id):
        return karta_id >= 1 and karta_id <= 8
    
    def isDiamond(self, karta_id):
        return karta_id >= 11 and karta_id <= 18
    
    def isSpade(self, karta_id):
        return karta_id >= 21 and karta_id <= 28
    
    def isClub(self, karta_id):
        return karta_id >= 31 and karta_id <= 38
    
    def isTarock(self, karta_id):
        return karta_id >= 40 and karta_id <= 61
    
    def is_same_color(self, karta1, karta2):
        return (self.isHeart(karta1) and self.isHeart(karta2)) or (self.isSpade(karta1) and self.isSpade(karta2)) or (self.isClub(karta1) and self.isClub(karta2)) or (self.isDiamond(karta1) and self.isDiamond(karta2)) or (self.isTarock(karta1) and self.isTarock(karta2))
    
    def deal_cards(self):
        
        #copy the keys of all the cards and so represent the entire deck
        cards = copy.deepcopy(list(self.id_to_cards.keys()))
        
        #shuffle the deck
        random.shuffle(cards)
        
        
        #dealt cards
        dealt_cards = []
        
        for i in range(0, len(cards), 16):
            dealt_cards.append(cards[i:i + 16])
        
        
        return dealt_cards
    
    def print_dealt_cards(self, dealt_cards):
        for i in range(len(dealt_cards)):
            if i < 3:
                print("Hand #" + str(i + 1) + ":")
            else:
                print("Talon:")
            for card in dealt_cards[i]:
                print("    " + self.id_to_cards[card])

    def print_hand(self, hand):
        for card in hand:
            print(self.id_to_cards[card])
            
    def legal_moves(self, opener, hand):
        legal_cards = []
        for card in hand:
            if self.is_same_color(opener, card) or self.isTarock(card):
                legal_cards.append(card)
        
        if not legal_cards:
            legal_cards = hand
        
        return legal_cards
    
    def play_card(self, hand, card):
        hand.remove(card)
        return card

if __name__ == "__main__":
    tarok = Tarock()
    karte = tarok.deal_cards()
    player1 = karte[0]
    player2 = karte[1]
    player3 = karte[2]
    
    tarok.print_hand(player1)
    print("---------------------------")
    legal = tarok.legal_moves(5, player1)
    print([tarok.id_to_cards[x] for x  in legal])
    tarok.play_card(player1, legal[0])
    tarok.print_hand(player1)
    print("---------------------------")
    tarok.print_dealt_cards(karte)
