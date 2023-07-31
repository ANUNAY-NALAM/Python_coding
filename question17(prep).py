
def gcd(a,b):
  while b:
    a,b=b,a%b
  return a

def method(heroes):
  v_p=heroes[0]
  for p in heroes[1:]:
    v_p=gcd(v_p,p)
  c_v=0
  for i in range(1,v_p+1):
    if v_p%i==0:
      c_v+=1
  return c_v


def main():
  t = int(input())
  for _ in range(t):
    n=int(input())
    heroes=list(map(int,input().split()))
    result=method(heroes)
    print(result)

if __name__ == "__main__":
  main()