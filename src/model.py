class Game:
    def __init__(self, pocket, community, opponent_num, opponent_cards):
        self.pocket = pocket
        self.community = community
        self.opponent_cards = opponent_cards
        self.opponent_num = opponent_num
        if len(community) == 0:
            self.state = "pre-flop"
        elif len(community) == 3:
            self.state = "flop"
        elif len(community) == 4:
            self.state = "turn"
        else:
            self.state = "river"
    def print_game(self):
        print("game state: ", self.state)
        print("number of opponents: ", self.opponent_num)
        print("player cards:")
        print("    ", self.pocket[0].string, self.pocket[1].string)
        print("community cards:")
        print("    ", end = " ")
        for card in self.community:
            print(card.string, end = " ")
        print()
        if len(self.opponent_cards) != 0:
            print("opponent cards:")
            for i in range(len(self.opponent_cards)):
                print("    ", self.opponent_cards[i][0].string, self.opponent_cards[i][1].string)

class Card:
    def __init__(self, string):
        # string is card representation, e.g. TD = ten of diamoondS
        RANK_BIT = {
            "A" : 4096,
            "K": 2048,
            "Q": 1024,
            "J": 512,
            "T": 256,
            "9": 128,
            "8": 64,
            "7": 32,
            "6": 16,
            "5": 8,
            "4": 4,
            "3": 2,
            "2": 1,
        }
        SUIT = {
            "C" : 8,
            "D": 4,
            "H": 2,
            "S": 1,
        }
        RANK = {
            "A" : 12,
            "K": 11,
            "Q": 10,
            "J": 9,
            "T": 8,
            "9": 7,
            "8": 6,
            "7": 5,
            "6": 4,
            "5": 3,
            "4": 2,
            "3": 1,
            "2": 0,
        }
        PRIME = {
            "A": 41,
            "K": 37,
            "Q": 31,
            "J": 29,
            "T": 23,
            "9": 19,
            "8": 17,
            "7": 13,
            "6": 11,
            "5": 7,
            "4": 5,
            "3": 3,
            "2": 2,
        }
        rank_char = string[0]
        suit_char = string[1]
        self.rank_bit = RANK_BIT.get(rank_char)
        self.suit = SUIT.get(suit_char)
        self.rank = RANK.get(rank_char)
        self.prime = PRIME.get(rank_char)
        self.string = string