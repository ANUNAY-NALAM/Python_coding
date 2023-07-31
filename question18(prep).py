
#lcm and gcd
def gcd(a,b):
  while b:
    a,b =b,a%b
  return a
def lcm(a,b):
  return (a*b)//gcd(a,b)

def method(n,m,k):
  min_s=lcm(n,m)
  count=k//min_s
  return count

def main():
  t=int(input())
  for _ in range(t):
    n,m,k=map(int,input().split())
    res=method(n,m,k)
    print(res)
    

if __name__ == "__main__":
  main()