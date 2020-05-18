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
        self.id_to_points = {
            4: 0,
            3: 0,
            2: 0,
            1: 0,
            5: 2,
            6: 3,
            7: 4,
            8: 5,
            14: 0,
            13: 0,
            12: 0,
            11: 0,
            15: 2,
            16: 3,
            17: 4,
            18: 5,
            21: 0,
            22: 0,
            23: 0,
            24: 0,
            25: 2,
            26: 3,
            27: 4,
            28: 5,
            31: 0,
            32: 0,
            33: 0,
            34: 0,
            35: 2,
            36: 3,
            37: 4,
            38: 5,
            40: 5,
            41: 0,
            42: 0,
            43: 0,
            44: 0,
            45: 0,
            46: 0,
            47: 0,
            48: 0,
            49: 0,
            50: 0,
            51: 0,
            52: 0,
            53: 0,
            54: 0,
            55: 0,
            56: 0,
            57: 0,
            58: 0,
            59: 0,
            60: 5,
            61: 5,
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
        s = "| "
        for card in hand:
            s += self.id_to_cards[card] + " (" + str(card) + ")" + " | "
        print(s)
    
    def legal_moves(self, opener, hand):
        legal_cards = []
        for card in hand:
            if self.is_same_color(opener, card):
                legal_cards.append(card)
        
        if not legal_cards:
            for card in hand:
                if self.isTarock(card):
                    legal_cards.append(card)
        
        if not legal_cards:
            legal_cards = hand
        
        return legal_cards
    
    def play_card(self, hand, card):
        hand.remove(card)
        return card

    def eval_stack(self, stack):
        stack_evaled = [self.id_to_points[c] for c in stack]
        if stack_evaled.count(0) == 0:
            return sum(stack_evaled) - 2
        if stack_evaled.count(0) == 1:
            return sum(stack_evaled) - 1
        if stack_evaled.count(0) == 2:
            return sum(stack_evaled)
        if stack_evaled.count(0) == 3:
            return 1

    #returns true if c2 beats c1
    def winning_card(self, c1, c2):
        if self.is_same_color(c1, c2):
            return c2 > c1
        elif self.isTarock(c1):
            return False
        elif self.isTarock(c2):
            return True
        else:
            return False


    def winning_player(self, stack):
        
        first = stack[0]
        second = stack[1]
        third = stack[2]

        if self.is_same_color(first, second) and self.is_same_color(first, third):
            #returns the number of the winning player
            return stack.index(max(stack)) + 1
        elif self.isTarock(first) or self.isTarock(second) or self.isTarock(third):
            return stack.index(max(stack)) + 1
        elif self.is_same_color(first, second):
            return 1 if first > second else 2
        elif self.is_same_color(first,third):
            return 1 if first > third else 3
        else:
            return 1


    def get_platlci(self, hand):
        return [c for c in hand if "Q" not in self.id_to_cards[c] and "K" not in self.id_to_cards[c] and "B" not in self.id_to_cards[c] and "C" not in self.id_to_cards[c] and c < 40]

    def get_pobi(self, hand):
        return [c for c in hand if "B" in self.id_to_cards[c]]

    def get_cavali(self, hand):
        return [c for c in hand if "C" in self.id_to_cards[c]]

    def get_dame(self,hand):
        return [c for c in hand if "Q" in self.id_to_cards[c]]

    def get_kralje(self, hand):
        return [c for c in hand if "K" in self.id_to_cards[c] and c != 61]

    def get_taroke(self, hand):
        return [c for c in hand if self.isTarock(c)]
    def skrt_igrane_karte(self, player, c, discard):
        
        #look back at played hands
        for prvi, drugi, tretji in discard:
            player1 = prvi[1]
            player2 = drugi[1]
            player3 = tretji[1]

            karta1 = prvi[0]
            karta2 = drugi[0]
            karta3 = tretji[0]

            
            #samo ce ni prvi igralec nam pove a je skrt al ni
            if player != player1:

                #ce je nas player igralec 2 in je prva karta igrana iste barve kot karta za katero gledamo ce je skrt
                if player == player2 and self.is_same_color(karta1, c):
                    
                    #ce najdemo da je igral karto k ni iste barve potem return je skrt
                    if not self.is_same_color(karta2, karta1):
                        return True
                if player == player3 and self.is_same_color(karta1, c):

                    if not self.is_same_color(karta3, karta1):
                        return True
        return False

    def get_state(self, stack, player_id, player2, player3, stack_value, legal_moves, hand, discard):
        """state_labels1 = [("vrednost igranih kart", [1,2,3]), #1 = runing sum 1, 2 = running sum <= 3, 3 = running sum > 3
                    ("skrt igrane karte", [0,1]), 
                    ("lahko poberes igrane karte", [0,1]),
                    ("player2 skrt igrane karte", [0,1]),
                    ("player3 skrt igrane karte", [0,1]),
                    ("imam se tarokov", [0,1]),
                    ("player2 nima vec tarokov", [0,1]),
                    ("player3 nima vec tarokov", [0,1])]"""
        state = []
        
        if stack:
            
            #state value
            if stack_value == 0:
                state.append((0,1))
            else:
                if stack_value <= 3:
                    state.append((0,2))
                else:
                    state.append((0,3))

            #skrt igrane karte
            prva_karta = stack[0]

            skrt = 1

            for c in hand:
                if self.is_same_color(c, prva_karta):
                    skrt = 0
            state.append((1,skrt))


            #lahko poberes igrane karte
            poberes = 0
            if len(stack) == 1:
                for c in legal_moves:
                    if self.winning_card(prva_karta, c):
                        poberes = 1
                state.append((2,poberes))
            elif len(stack) == 2:
                poberejo_prvo = []
                for c in legal_moves:
                    if self.winning_card(prva_karta, c):
                        poberejo_prvo.append(c)
                for c in poberejo_prvo:
                    if self.winning_card(stack[1], c):
                        poberes = 1
                state.append((2,poberes))

            #player2 skrt igrane karte
            if self.skrt_igrane_karte(player2, prva_karta, discard):
                state.append((3, 1))
            else:
                state.append((3,0))

            #player3 skrt igrane karte
            if self.skrt_igrane_karte(player3, prva_karta, discard):
                state.append((4, 1))
            else:
                state.append((4,0))

            #imam se tarokov
            seTarokov = 0
            for c in hand:
                if self.isTarock(c):
                    seTarokov = 1
            state.append((5,seTarokov))

            #player2 nima vec tarokov
            #da nimas vec tarokov, je isto kot da si skrt tarokov
            #zato damo za igrano karto vedno taroka in ce pride da je skrt te barve potem pomeni, da nima vec tarokov
            if self.skrt_igrane_karte(player2, 61, discard):
                state.append((6, 1))
            else:
                state.append((6,0))

            #player3 nima vec tarokov
            if self.skrt_igrane_karte(player3, 61, discard):
                state.append((7, 1))
            else:
                state.append((7,0))

            return state

        else:
            """state_labels2 = [("imas kralja", [0,1]), 
                ("imas damo", [0,1]),
                ("imas pob/caval", [0,1]),
                ("imas platlca", [0,1]),
                ("imam se tarokov", [0,1]),
                ("player2 nima vec tarokov", [0,1]),
                ("player3 nima vec tarokov", [0,1])]"""
            
            #imas kralja
            kralj = 0
            for c in hand:
                if "K" in self.id_to_cards[c] and c != 61:
                    kralj=1
            state.append((0,kralj))

            #imas damo
            dama = 0
            for c in hand:
                if "Q" in self.id_to_cards[c]:
                    dama=1
            state.append((1,dama))

            #imas pob/caval
            pobc = 0
            for c in hand:
                if "B" in self.id_to_cards[c] or "C" in self.id_to_cards[c]:
                    pobc=1
            state.append((2,pobc))

            #imas platlca
            platlc = 0
            for c in hand:
                ime = self.id_to_cards[c]
                if c < 40 and "B" not in ime and "C" not in ime and "Q" not in ime and "K" not in ime:
                    platlc = 1
            state.append((3,platlc))

            #imam se tarokov
            seTarokov = 0
            for c in hand:
                if self.isTarock(c):
                    seTarokov = 1
            state.append((4,seTarokov))

            #player2 nima vec tarokov
            #da nimas vec tarokov, je isto kot da si skrt tarokov
            #zato damo za igrano karto vedno taroka in ce pride da je skrt te barve potem pomeni, da nima vec tarokov
            if self.skrt_igrane_karte(player2, 61, discard):
                state.append((5, 1))
            else:
                state.append((5,0))

            #player3 nima vec tarokov
            if self.skrt_igrane_karte(player3, 61, discard):
                state.append((6, 1))
            else:
                state.append((6,0))

            return state


    def get_state_wrapper(self, **args):
        #(self, stack, player_id, player2, player3 stack_value, legal_moves, hand, discard):
        player_id = args["player_id"]
        player2 = args["player2"]
        player3 = args["player3"]
        stack_value = args["stack_value"]
        stack = args["current_stack"]
        legal_moves = args["legal_moves"]
        hand = args["hand"]
        discard = args["discard"]                                                               
                                                                
        return self.get_state(stack, player_id, player2, player3, stack_value, legal_moves, hand, discard)

    def search_discard(self, discard, card):
        
        #[[(card, player), (card, player), (card, player)], [(card, player), (card, player), (card, player)]]
        
        for play in discard:

            for card1, player in play:
                if card1 == card:
                    return True
        return False

    def search_mega_taroka(self, discard, hand):

        #0 -> oba discard True True False False
        #1 -> 1 nasprotnik 1 discard    True False False False/ False True False False
        #2 -> 1 nasprotnik 1 jaz False False True False
        #3 -> 2 nasprotnik False False False False
        #4 -> 1 jaz 1 discard True False True False
        #5 -> 2 jaz False False True True

        mond_discard = self.search_discard(discard, 60)
        skis_discard = self.search_discard(discard, 61)

        mond_hand = 60 in hand
        skis_hand = 61 in hand
        
        mond_opponent = not mond_discard and not mond_hand
        skis_opponent = not skis_discard and not skis_hand

        if mond_discard and skis_discard:
            return 0
        if (mond_opponent and skis_discard) or (mond_discard and skis_opponent):
            return 1
        if (mond_opponent and skis_hand) or (mond_hand and skis_opponent):
            return 2
        if mond_opponent and skis_opponent:
            return 3
        if (mond_hand and skis_discard) or (mond_discard and skis_hand):
            return 4
        if mond_hand and skis_hand:
            return 5

    def get_new_state(self, hand, discard, stack, player2, player3):
        
        #0 -> v discardu, 1-> enemy, 2-> in hand
        new_states = [("herc kralj", [0,1,2]),
              ("herc dama", [0,1,2]),
              ("kara kralj", [0,1,2]),
              ("kara dama", [0,1,2]),
              ("pik kralj", [0,1,2]),
              ("pik dama", [0,1,2]),
              ("kriz kralj", [0,1,2]),
              ("kriz dama", [0,1,2]),
              ("mega taroka", [0,1,2,3,4,5]),
              ("pagat", [0,1,2]),
              ("player2 brez tarokov", [0, 1]),
              ("player3 brez tarokov", [0, 1]),
              ("vrednost stacka", [0,1,2])]
        
        #herckral 8
        #herc dama 7
        #kara kral 18
        #kara dama 17
        #pik kral 28
        #pik dama 27
        #kriz kral 38
        #kriz dama 37

        #inicializiramo da imajo vse nasprotniki
        state = [1 for i in range(len(new_states))]
        
        #herc kral
        state[0] = 0 if self.search_discard(discard, 8) else 1
        state[0] = 2 if 8 in hand else 1

        #herc dama
        state[1] = 0 if self.search_discard(discard, 7) else 1
        state[1] = 2 if 7 in hand else 1

        #kara kral
        state[2] = 0 if self.search_discard(discard, 18) else 1
        state[2] = 2 if 18 in hand else 1

        #kara dama
        state[3] = 0 if self.search_discard(discard, 17) else 1
        state[3] = 2 if 17 in hand else 1

        #pik kral
        state[4] = 0 if self.search_discard(discard, 28) else 1
        state[4] = 2 if 28 in hand else 1

        #pik dama
        state[5] = 0 if self.search_discard(discard, 27) else 1
        state[5] = 2 if 27 in hand else 1

        #kriz kral
        state[6] = 0 if self.search_discard(discard, 38) else 1
        state[6] = 2 if 38 in hand else 1

        #kriz dama
        state[7] = 0 if self.search_discard(discard, 37) else 1
        state[7] = 2 if 37 in hand else 1

        #mega tarok
        state[8] = self.search_mega_taroka(discard, hand)

        #pagat
        state[9] = 0 if self.search_discard(discard, 40) else 1
        state[9] = 2 if 40 in hand else 1

        #player2 brez tarokov
        state[10] = 1 if self.skrt_igrane_karte(player2, 61, discard) else 0

        #player3 brez tarokov
        state[11] = 1 if self.skrt_igrane_karte(player3, 61, discard) else 0


        if self.eval_stack(stack) == 1:
            state[12] = 0
        elif self.eval_stack(stack) <= 3:
            state[12] = 1
        else:
            state[12] = 2

        return tuple(state)

    def choose_card_play(self, stack, legal_moves, action):
        #     0           1               2              3
        #["spustis", "poberes min", "poberes mid", "poberes max"]
        #spustis -> najmanjso legal karto igras
        #poberes min -> najmanjso karto, ki se pobere
        #poberes mid -> srednje mocno karto, ki se pobere
        #poberes max -> najmocnejso karto, ki pobere

        #vse karte iz legal moves, ki poberejo stack

        karte_ki_poberejo_stack = []
        for c in legal_moves:

            if len(stack) == 1:
                if self.winning_card(stack[0], c):
                    karte_ki_poberejo_stack.append(c)
            if len(stack) == 2:
                if self.winning_card(stack[0], c) and self.winning_card(stack[1], c):
                    karte_ki_poberejo_stack.append(c)
        """print("stack")
        self.print_hand(stack)
        print("legal moves")
        self.print_hand(legal_moves)
        print("poberejo stack")
        self.print_hand(karte_ki_poberejo_stack)
        print("***************************************")"""

        karte_ki_poberejo_stack = list(sorted(karte_ki_poberejo_stack))

        if action == 0:
            return list(sorted(legal_moves))[0]
        elif action == 1:
            return karte_ki_poberejo_stack[0]
        elif action == 2:
            return karte_ki_poberejo_stack[len(karte_ki_poberejo_stack)//2]
        else:
            return karte_ki_poberejo_stack[-1]

    def choose_card_lead(self, legal_moves, action):
        #       0                  1               2             3                4
        #["igras platlca", "igras pob/caval", "igras damo", "igras kralja", "igras tarok"]
        platlci = self.get_platlci(legal_moves)
        pobi = self.get_pobi(legal_moves)
        cavali = self.get_cavali(legal_moves)
        dame = self.get_dame(legal_moves)
        kralji = self.get_kralje(legal_moves)
        taroki = self.get_taroke(legal_moves)
        
        if action == 0:
            return random.choice(platlci)
        elif action == 1:
            return random.choice(pobi + cavali)
        elif action == 2:
            return random.choice(dame)
        elif action == 3:
            return random.choice(kralji)
        else:
            return random.choice(taroki)

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
