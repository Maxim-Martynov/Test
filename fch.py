def f(a,b,m):
    if a+b>=68: return m%2==0
    if m==0: return 0
    h=[f(a+2,b,m-1),f(a*2,b,m-1),f(a,b+2,m-1),f(a,b*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print('19)',[s for s in range(1,61) if f(7,s,2)])
print('20)',[s for s in range(1,61) if not f(7,s,1) and f(7,s,3)])
print('20)',[s for s in range(1,61) if not f(7,s,2) and f(7,s,4)])
