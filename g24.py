'''
A class to calculate solution for 24 game.
Also iterate all combinations to see how many has at least one solution.
'''
from typing import List
import time

class TwentyFourCalculator:
    '''This class is a 24 game calculator. It returns a solution, or None if no solution.'''
    def __init__(self):
        self.cards = {}

    def cal_24(self, nums: List[int]) -> bool:
        '''public method to calculate a solution for 4 cards.'''
        cards_hash = self.get_hash(nums)
        if cards_hash in self.cards:
            return self.cards[cards_hash]

        rst = self.go4([[num, f'{num}'] for num in nums], nums)
        sln = self.cards[cards_hash] if rst else 'None'
        return sln

    def go4(self, nums, cards):
        '''Recursive. Calculate towards 24.'''
        k = len(nums)
        if k == 1:
            rst = abs(nums[0][0] - 24) < 0.0001
            if rst:
                cards_hash = self.get_hash(cards)
                sln_path = nums[0][1][1:-1]
                self.cards[cards_hash] = sln_path
            return rst

        rst = False
        perms = self.get_perms(k)
        for perm in perms:
            # First 2 will be inlcuded in the next operation.
            [n1, p1], [n2, p2] = nums[perm[0]], nums[perm[1]]
            others = [nums[perm[i]] for i in range(2, len(perm))]

            # Add
            rst = rst or self.go4([[n1 + n2, self.get_expression(p1, p2, '+')]] + others, cards)
            # Sub
            if n1 >= n2:
                rst = rst or self.go4([[n1 - n2, self.get_expression(p1, p2, '-')]] + others, cards)
            if n2 >= n1:
                rst = rst or self.go4([[n2 - n1, self.get_expression(p2, p1, '-')]] + others, cards)
            # Mul
            rst = rst or self.go4([[n1 * n2, self.get_expression(p1, p2, '*')]] + others, cards)
            # Div
            if n2 != 0:
                rst = rst or self.go4([[n1 / n2, self.get_expression(p1, p2, '/')]] + others, cards)
            if n1 != 0:
                rst = rst or self.go4([[n2 / n1, self.get_expression(p2, p1, '/')]] + others, cards)
        return rst

    def get_expression(self, path1, path2, ops):
        return f'({path1}{ops}{path2})'

    def get_perms(self, k):
        '''Get permutation of possible operations.'''
        if k == 4:
            return [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2],
                    [1, 2, 0, 3], [1, 3, 0, 2], [2, 3, 0, 1]]
        if k == 3:
            return [[0, 1, 2], [0, 2, 1], [1, 2, 0]]
        if k == 2:
            return [[0, 1]]
        raise ValueError('Unexpected input value.')

    def get_hash(self, nums):
        '''Get the hash value of 4 cards.'''
        return '='.join([f'{num}' for num in nums])


def main1():
    '''Calculate one single combination.'''
    cards = [5, 5, 7, 11]
    twenty_four_calculator = TwentyFourCalculator()
    rst = twenty_four_calculator.cal_24(cards)
    print(rst)

def main():
    '''Iterate all combination and calculate solution.'''
    twenty_four_calculator = TwentyFourCalculator()
    total_ct = 0
    sln_ct = 0
    start_time = time.time()

    for card1 in range(1, 14):
        for card2 in range(card1, 14):
            for card3 in range(card2, 14):
                for card4 in range(card3, 14):
                    total_ct += 1
                    cards = [card1, card2, card3, card4]
                    rst = twenty_four_calculator.cal_24(cards)
                    rst_str = f'[{card1}, {card2}, {card3}, {card4}]: '
                    if rst == 'None':
                        rst_str += 'Impossible'
                    else:
                        sln_ct += 1
                        rst_str += rst
                    print(rst_str)
    print('Total: ', total_ct)
    print('Solution: ', sln_ct)
    print()

    end_time = time.time()
    time_elap = end_time - start_time
    if total_ct == 1820 and sln_ct == 1362:
        print('All results look good.')
    else:
        print('Result number has ERROR.')
    print("It took", time_elap, "seconds!")


if __name__ == "__main__":
    main()
