def method(r,p,q):
  count=(q//r)-((p-1)//r)
  return count

if __name__ == "__main__":
  t=int(input())
  for _ in range(t):
    r,p,q = map(int,input().split())
    result=method(r,p,q)
    print(result)