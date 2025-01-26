from typing import List
import time


class TwentyFourCalculator:
    def __init__(self):
        self.cards = {}
    
    def cal_24(self, nums: List[int]) -> bool:
        nums = [[num, f'{num}'] for num in nums]
        nums = sorted(nums)
        n1 = [num[0] for num in nums]
        cards_hash = self.get_hash(n1)
        if cards_hash in self.cards:
            return self.cards[cards_hash]
        
        rst = self.go4(nums, n1)
        sln = 'None'
        if rst:
            sln = self.cards[cards_hash]
        return sln
        

    def go1(self, nums, cards):
        rst = False
        if len(nums) == 1:
            # rst = nums[0][0] == 24
            rst = abs(nums[0][0] - 24) < 0.0001
        else:
            abc # should never gets here.
        
        cards_hash = self.get_hash(cards)
        if rst:
            self.cards[cards_hash] = nums[0][1]
        return rst

    def go2(self, nums, cards):
        
        rst = False
        [n1, p1], [n2, p2] = nums[0], nums[1]
        # Add
        rst = rst or self.go1([[n1 + n2, f'({p1})+({p2})']], cards)
        # Sub
        if n1 >= n2: rst = rst or self.go1([[n1 - n2, f'({p1})-({p2})']], cards)
        if n2 >= n1: rst = rst or self.go1([[n2 - n1, f'({p2})-({p1})']], cards)
        # Mul
        rst = rst or self.go1([[n1 * n2, f'({p1})*({p2})']], cards)
        # Div
        if n2 != 0: rst = rst or self.go1([[n1 / n2, f'({p1})/({p2})']], cards)
        if n1 != 0: rst = rst or self.go1([[n2 / n1, f'({p2})/({p1})']], cards)
        return rst

    def go3(self, nums, cards):
        rst = False
        perms = [[0, 1, 2], [0, 2, 1], [1, 2, 0]]
        for i1, i2, i3 in perms:
            [n1, p1], [n2, p2], [n3, p3] = nums[i1], nums[i2], nums[i3]
            # Add
            rst = rst or self.go2([[n1 + n2, f'({p1})+({p2})'], [n3, p3]], cards)
            # Sub
            if n1 >= n2: rst = rst or self.go2([[n1 - n2, f'({p1})-({p2})'], [n3, p3]], cards)
            if n2 >= n1: rst = rst or self.go2([[n2 - n1, f'({p2})-({p1})'], [n3, p3]], cards)
            # Mul
            rst = rst or self.go2([[n1 * n2, f'({p1})*({p2})'], [n3, p3]], cards)
            # Div
            if n2 != 0: rst = rst or self.go2([[n1 / n2, f'({p1})/({p2})'], [n3, p3]], cards)
            if n1 != 0: rst = rst or self.go2([[n2 / n1, f'({p2})/({p1})'], [n3, p3]], cards)
        return rst

    def go4(self, nums, cards):
        k = len(nums)
        rst = False
        perms = self.get_perms(k)
        for perm in perms:
            # First 2 will be inlcuded in the next operation.
            [n1, p1], [n2, p2] = nums[perm[0]], nums[perm[1]]
            others = [nums[perm[i]] for i in range(2, len(perm))]

            # Add
            rst = rst or self.go3([[n1 + n2, f'({p1})+({p2})']] + others, cards)
            # Sub
            if n1 >= n2: rst = rst or self.go3([[n1 - n2, f'({p1})-({p2})']] + others, cards)
            if n2 >= n1: rst = rst or self.go3([[n2 - n1, f'({p2})-({p1})']] + others, cards)
            # Mul
            rst = rst or self.go3([[n1 * n2, f'({p1})*({p2})']] + others, cards)
            # Div
            if n2 != 0: rst = rst or self.go3([[n1 / n2, f'({p1})/({p2})']] + others, cards)
            if n1 != 0: rst = rst or self.go3([[n2 / n1, f'({p2})/({p1})']] + others, cards)
        return rst

    def get_perms(self, k):
        if k == 4: return [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2], [1, 2, 0, 3], [1, 3, 0, 2], [2, 3, 0, 1]]
        if k == 3: return [[0, 1, 2], [0, 2, 1], [1, 2, 0]]
        if k == 2: return [[0, 1]]
        raise Exception('Unexpected input value.')

    def get_hash(self, nums):
        return '='.join([f'{num}' for num in nums])


def main1():
    cards = [5, 5, 7, 11]
    twenty_four_calculator = TwentyFourCalculator()
    rst = twenty_four_calculator.cal_24(cards)
    print(rst)
    
def main():
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