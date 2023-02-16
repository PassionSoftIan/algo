from itertools import permutations
from pprint import pprint
from itertools import combinations
a = range(1, 3)
b = list(permutations(a))
for i in b:
    print(i)
print()
c = list(combinations(a, 3))
for i in c:
    print(i)