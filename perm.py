from itertools import permutations
s=input()
s=s.split(' ')
list1 = s[0].split()
list2 = s[1].split()
my_string = list1[0]
number = int(list2[0])
for i in sorted(permutations(my_string, r = number)):
    print(''.join(i))