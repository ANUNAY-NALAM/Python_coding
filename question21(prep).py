def method(n,st):
  count=0
  ones=0
  for i in range(n):
    if st[i] =='1':
      ones+=1
      count+=ones
  return count


if __name__ == '__main__':
  t=int(input())
  for _ in range (t):
    n=int(input())
    st=input()
    res=method(n,st)
    print(res)