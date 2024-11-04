a='abcdefghijklmnopqrstuvwxyz'
size=int(input('Size:'))
lines=[]
for row in range(size):
    print_ = "-".join(a[row:size])
    lines.append(print_[::-1] + print_[1:])
width = len(lines[0])

for row in range(size - 1, 0, -1):
    print(lines[row].center(width, '-'))

for row in range(size):
    print(lines[row].center(width, '-'))
