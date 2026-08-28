class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}
        for number in nums:
            arr[number] = arr.get(number, 0) + 1
        sorted_arr = dict(sorted(arr.items(), key= lambda item: item[1] ))
        return list(sorted_arr.keys())[-k:]