
def method2(arr,y):
  n=len(arr)
  s=0
  for i in range(n):
    diff=arr[i]-y*(i+1)
    s+=max(diff,0)
  return s

def method1(arr,k):
  left,right=0,max(arr)
  res_y,res_s=-1,-1
  while left<=right:
    mid= (left+right)//2
    s=method2(arr,mid)
    if s>=k:
      res_y=mid
      res_s=s
      left=mid+1
    else:
      right=mid-1
  return res_y,res_s

if __name__ == '__main__':
  t=int(input())
  for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    y,s=method1(arr,k)
    print(y,s)

    