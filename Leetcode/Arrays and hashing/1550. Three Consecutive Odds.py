class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        cnt = 0
        for n in arr:
            if n%2:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False