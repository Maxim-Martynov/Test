s=input()
words = s.split()
X=int(words[0])
Y=int(words[1])
N=int(words[2])
for i in range(1,N+1):
    if ((i%X==0)&(i%Y==0)):
        print('FizzBuzz')
    elif (i%Y)==0:
        print('Buzz')
    elif (i%X==0):
        print('Fizz')
    else:
        print(i)
        