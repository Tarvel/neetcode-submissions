class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}
        for number in nums:
            arr[number] = arr.get(number, 0) + 1
        sorted_arr = dict(sorted(arr.items(), key= lambda item: item[1] )) #lambda is like writing a function in line (like list comprehensions), so like def get_item(item) return item[1] cos for the arr.items() converts our dict to a tuple e.g. {"A": 1. "B": 2} becomes [("A", 1), ("B", 2)] so the key placeholder in the sorted function helps to point to how the items should be sorted and here its by the values (tem[1]) 
        return list(sorted_arr.keys())[-k:]