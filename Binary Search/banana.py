def min_eating_speed(piles, h):
    def can_finish(speed):
        hours_needed = sum((pile + speed - 1) // speed for pile in piles)
        return hours_needed <= h

    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left

# Example usage:
piles = [3, 6, 7, 11]
h = 8
result = min_eating_speed(piles, h)
print(result)
