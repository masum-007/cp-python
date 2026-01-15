import sys

# ------------------- FAST I/O SETUP -------------------

# 1. Fast Input: Overrides the slow input()
input = sys.stdin.readline

# 2. Fast Output: Overrides the slow print()
# This handles integers, lists, and strings automatically
def print(*args, end="\n", sep=" "):
    sys.stdout.write(sep.join(map(str, args)) + end)

# 3. Increase Recursion Limit (Essential for Graph/Tree problems)
sys.setrecursionlimit(10**6)

# ------------------- SOLUTION -------------------

def solve():
    # TYPE YOUR CODE HERE
    # Example: Reading n
    # n = int(input())
    
    # Example: Reading list
    # arr = list(map(int, input().split()))
    
    pass 

# ------------------- DRIVER CODE -------------------
if __name__ == "__main__":
    solve()