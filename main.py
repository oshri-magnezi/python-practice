class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def surface(self) -> float:
        """returns the area of the rectangle """
        return self.width * self.height

rect = Rectangle(4, 5)
print(rect.surface()) #20


def second_largest(nums: list[int]) -> int:
    """return the second largest number in the list"""
    largest = float("-inf")
    second = float("-inf")
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif second < num < largest:
            second = num
    return second