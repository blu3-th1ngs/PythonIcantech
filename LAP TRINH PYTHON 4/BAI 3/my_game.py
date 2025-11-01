import random

class Game:
    def __init__(self, type='xúc xắc'):
        self.type = type
        self.score_list = []

    @property
    def score(self):
        if self.type == 'đồng xu':
            return random.randint(0, 1)
        elif self.type == 'xúc xắc':
            return random.randint(1, 6)

    @property
    def quantity(self):
        return len(self.score_list)

    @quantity.setter
    def quantity(self, new_quantity):
        for _ in range(new_quantity):
            self.score_list.append(self.score)

    @quantity.deleter
    def quantity(self):
        self.score_list = []

    @property
    def total_score(self):
        return sum(self.score_list)

    @property
    def average_score(self):
        if len(self.score_list) == 0:
            return 0
        return sum(self.score_list) / len(self.score_list)

    @property
    def max_score(self):
        if len(self.score_list) == 0:
            return None
        return max(self.score_list)

    @property
    def min_score(self):
        if len(self.score_list) == 0:
            return None
        return min(self.score_list)

    def play(self, quantity=0):
        del self.quantity
        self.quantity = quantity
        print(f"Điểm {self.quantity} lần gieo {self.type}: {self.score_list}")
        print(f"Tổng điểm {self.type}: {self.total_score}")
        print(f"Điểm trung bình: {self.average_score:.2f}")
        print(f"Điểm cao nhất: {self.max_score}")
        print(f"Điểm thấp nhất: {self.min_score}\n")


game1 = Game(type='đồng xu')
game1.play(quantity=5)

game2 = Game(type='xúc xắc')
game2.play(quantity=3)
