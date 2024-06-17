hours =  [72,48,24,3]
count = 0
dicts = {}

for i, val in enumerate(hours):
    temp = val % 24
    complement = (24 - temp) % 24
    if complement in dicts:
        count += dicts[complement]
    dicts[temp] = dicts.get(temp, 0) + 1
print(dicts)
print(count)