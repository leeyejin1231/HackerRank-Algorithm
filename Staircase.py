def staircase(n):
    for i in range(1, n+1):
        print(" "*(n-i), end='')
        print("#"*i)

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
