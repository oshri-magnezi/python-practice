from main import second_largest

"""normal array"""
assert second_largest([3, 1, 4, 1, 5, 9, 2]) == 5

"""duplicated values array"""
assert second_largest([7, 7, 3]) == 3

"""negative values array"""
assert second_largest([-5, -2, -8, -1]) == -2

print("All tests passed!")
