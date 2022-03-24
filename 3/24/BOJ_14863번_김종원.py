import sys
from collections import deque

N, K = map(int,sys.stdin.readline().strip().split())
walks , ride = [], []

for _ in range(N):
    a1,a2,b1,b2, = map(int,sys.stdin.readline().strip().split())
    walks.append((a1,a2))
    ride.append((b1,b2))

dp = [0] * (K+1)

q = deque()
q.append((K,N))
while q:
    cur_K, depth_index = q.popleft()
    
    walk_min, walk_money = walks[depth_index-1]
    ride_min, ride_money = ride[depth_index-1]
    if (cur_K - walk_min) >=0 and (depth_index - 1) >=0:
         
        dp[cur_K - walk_min] = max(dp[cur_K - walk_min], dp[cur_K] + walk_money)
        print(cur_K , "next_walk : ", cur_K - walk_min , " COST : ",dp[cur_K - walk_min] ," depth : ", depth_index)
        q.append((cur_K - walk_min , depth_index - 1))

    if (cur_K - ride_min) >=0 and (depth_index - 1) >=0 :
        dp[cur_K - ride_min] = max(dp[cur_K - ride_min], dp[cur_K] + ride_money)
        print(cur_K , "next_ride : ", cur_K - ride_min , " COST : ",dp[cur_K - ride_min] ," depth : ", depth_index)
        q.append((cur_K - ride_min , depth_index - 1))
    

print(max(dp))
    
