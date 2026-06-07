from typing import Any

all_guests: dict[str, dict[str, int]] = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}

def total_brought(guests: dict[str, dict[str, int]], item: str) -> int:
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought

print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
print(' - Pretzels       ' + str(total_brought(all_guests, 'pretzels')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))