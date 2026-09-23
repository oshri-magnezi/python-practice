class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def surface(self) -> float:
        return self.width * self.height


def second_largest(nums: list[int]) -> int:
    """return the second largest number in the list"""
    max = float("-inf")
    second_max = float("-inf")
    for num in nums:
        if num > second_max:
            max = second_max
            second_max = num
        elif max < num < second_max:
            max = second_max
    return second_max
