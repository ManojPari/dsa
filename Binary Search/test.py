def calculateBananas(piles, bananas, h):
    hours = 0
    for i in piles:
        hours += (i + bananas - 1) // bananas  # Corrected calculation
        if hours > h:
            return False
    return True

piles = [312884470]
h = 312884469
low = 1
high = max(piles)
ans = max(piles)
while low <= high:
    mid = (low + high) // 2
    if calculateBananas(piles, mid, h):
        high = mid - 1
        ans = min(ans, mid)
    else:
        low = mid + 1
print(ans)