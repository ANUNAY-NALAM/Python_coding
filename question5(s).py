st=input()

n=int(input())

if len(st) % 2==0:
    mid=(len(st)//2)-1
else:
    mid=len(st)//2
    

if mid+n > len(st):
    print(st[mid:])
else:
    print(st[mid:mid+n])