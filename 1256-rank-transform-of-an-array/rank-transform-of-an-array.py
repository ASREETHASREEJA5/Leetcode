class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Sort the array and remove duplicates
        l1 = sorted(set(arr))
        
        # Step 2: Create a dictionary that maps each value to its rank
        rank_dict = {value: rank + 1 for rank, value in enumerate(l1)}
        
        # Step 3: Replace each element in the original array with its rank using the dictionary
        return [rank_dict[num] for num in arr]
