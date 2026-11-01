class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I think the smart way to approach this is for every value in the list, we do target - nums.value.
        # May also be smart to put them in a set so for example 7-3 = 4. Is 4 in set no, okay add 3 to set and then next one.
        # 7-4 = 3 is 3 in set yes. return the two indexes. Should be a dict not set so i can pput the index as the value too.
        # a Kinda formula to help x = target - number

        checker = {}
        for index, number in enumerate(nums):
            
            x = target - number

            if x in checker:
                return [checker[x], index]
            checker[number] = index

        

