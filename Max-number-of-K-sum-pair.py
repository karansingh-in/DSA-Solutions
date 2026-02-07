class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = int(0)
        sorted_copy = sorted(nums)
        for i in range(len(sorted_copy)):
            if sorted_copy[i] >= k:
                sorted_copy = sorted_copy[0:i]
                break
        for i in range(len(sorted_copy)):
            if sorted_copy[i] == 0:
                pass
            for j in range(i+1, len(sorted_copy)):
                if sorted_copy[i] + sorted_copy[j] == k:
                    if sorted_copy[j] == 0:
                        pass
                    else:
                        counter += 1
                        sorted_copy[i] = 0
                        sorted_copy[j] = 0
        return counter