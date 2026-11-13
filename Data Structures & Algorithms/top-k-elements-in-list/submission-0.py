class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element = {}
        res = []
        for num in nums:
            element[num] = element.get(num, 0) + 1
        element = dict(sorted(element.items(), key=lambda item: item[1], reverse=True))
        top_k_element = list(element)[:k]
        return top_k_element
        