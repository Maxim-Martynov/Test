from collections import OrderedDict
od = OrderedDict()
n = int(input())
for i in range(n)
    pred, prob, cen = input().rpartition(' ')
    od[pred]=od.get(pred, 0)+int(cen)
for pred, cen in od.items()
    print(pred, cen)
