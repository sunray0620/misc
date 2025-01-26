from typing import List


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
        nums = sorted(nums)
        
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
        nums = sorted(nums)
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
        nums = sorted(nums)
        rst = False
        perms = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2], [1, 2, 0, 3], [1, 3, 0, 2], [2, 3, 0, 1]]
        for i1, i2, i3, i4 in perms:
            [n1, p1], [n2, p2], [n3, p3], [n4, p4] = nums[i1], nums[i2], nums[i3], nums[i4]
            # Add
            rst = rst or self.go3([[n1 + n2, f'({p1})+({p2})'], [n3, p3], [n4, p4]], cards)
            # Sub
            if n1 >= n2: rst = rst or self.go3([[n1 - n2, f'({p1})-({p2})'], [n3, p3], [n4, p4]], cards)
            if n2 >= n1: rst = rst or self.go3([[n2 - n1, f'({p2})-({p1})'], [n3, p3], [n4, p4]], cards)
            # Mul
            rst = rst or self.go3([[n1 * n2, f'({p1})*({p2})'], [n3, p3], [n4, p4]], cards)
            # Div
            if n2 != 0: rst = rst or self.go3([[n1 / n2, f'({p1})/({p2})'], [n3, p3], [n4, p4]], cards)
            if n1 != 0: rst = rst or self.go3([[n2 / n1, f'({p2})/({p1})'], [n3, p3], [n4, p4]], cards)
        return rst

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
    
                
if __name__ == "__main__":
    main()