class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(start, temp, total):
            # if not temp:
            #     return []
            if total == target:
                result.append(temp.copy())
                return
            if total > target or start >= len(nums):
                return
            temp.append(nums[start])
            dfs(start, temp, total + nums[start])
            temp.pop()
            dfs(start + 1, temp, total)

                
        dfs(0, [], 0)
        return result