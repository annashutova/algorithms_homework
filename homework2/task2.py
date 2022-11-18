"""Сложность: O(n)"""


def getMaximumGenerated(n: int) -> int:
    if n == 0:
        return 0
    nums = [0] * (n + 1)  # создаем список нулей длины (n + 1)
    nums[1] = 1
    for i in range(2, n + 1):
        # заполняем список в соответствии с условием
        if i % 2 == 0:
            nums[i] = nums[i // 2]
        else:
            nums[i] = nums[i // 2] + nums[i // 2 + 1]
    return max(nums)
