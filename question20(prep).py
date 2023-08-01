def is_prime(n):
  if n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

def method(roll,k):
  first=int(roll[0])
  last=int(roll[-1])
  if is_prime(first) and is_prime(last) and (first+last)>k:
    return "Yes"
  else:
    return "No"

def main():
  n,k = map(int,input().split())
  for _ in range(n):
    roll=input().strip()
    res=method(roll,k)
    print(res)
if __name__ == "__main__":
  main()