import math

def is_prime(N):
    if N < 2:
        return False

    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False

    return True


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        if is_prime(N):
            print("Yes")
        else:
            print("No")