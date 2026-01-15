import sys

input = sys.stdin.readline
def print(*args, end="\n", sep=" "):
    sys.stdout.write(sep.join(map(str, args)) + end)
sys.setrecursionlimit(10**6)



def solve():
    nums = list(map(int, input().split()))
    target = int(input())

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i]+nums[j]) == target:
             print(i,j)
             return
                                   

if __name__ == "__main__":
    solve()