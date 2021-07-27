N=int(input())
Сумма=0
Предыдущее=0
for number in range(N):
    k=int(input())
    if (number%2)==0:
        Предыдущее=k
    else:
        Сумма=Сумма+(k-Предыдущее)
if (N%2)==1:
    print('still running')
else:
    print(Сумма)
