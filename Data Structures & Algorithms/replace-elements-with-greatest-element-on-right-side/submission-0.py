class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_list = []
        for i in range(0, len(arr)):
            if i == len(arr)-1:
                new_list.append(-1)
                return new_list
            new_list.append(sorted(arr[i+1::])[-1])