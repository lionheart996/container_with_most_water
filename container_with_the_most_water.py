from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:

        temp_list = height.copy()

        max_number1 = max(height)
        max_number1_index = height.index((max_number1))

        if len(height) == 2:
            return min(height)

        for i in range((len(height))):
            if temp_list[i] == max_number1:
                temp_list[i] = -1

        max_number2 = max(temp_list)
        max_number2_index = height.index((max_number2))

        new_list = height[max_number1_index:max_number2_index]

        max_area = max_number2 * (len(new_list) )

        return max_area


the_height = [1,8,6,2,5,4,8,3,7]
container = Solution().maxArea(the_height)
print(container)
