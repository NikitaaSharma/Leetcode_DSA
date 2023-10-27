# n number of people are sitting in a circle, we've to find the winner who remains till the end as people kill each other 
# in the given pattern:
# 1. kill the kth person from the ith position, including ith person.
# 2. After kth person dies, the counting starts again from the (k+1)th position and so on.

n = 41
k = 2

def josephusSolution(n,k):
    if n==1: return 1

    return ((josephusSolution(n-1,k) + k -1)%n + 1)

winner_position = josephusSolution(n, k)
print(f"Winner should sit at: {winner_position}th position")