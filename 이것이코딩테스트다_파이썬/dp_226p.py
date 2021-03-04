# 모범 답안과 다른 풀이
from collections import deque
import sys
import copy

n, m = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(int(input()))
    
queue = deque()
tmpQueue = deque()
queue.append(0)


coinDepth = 0
# cnt = 0

while True:
    coinDepth += 1
    while queue:
        pop = queue.popleft()
        if pop >= m:    #맞나..?
            print("-1")
            sys.exit()
        # print()
        # print("pop : ", pop, end=" ")
        # if cnt >= 100:
        #     break
        for n_index in arr:
            if pop + n_index == m:
                print(coinDepth)
                sys.exit()
            elif pop + n_index not in queue:
                tmpQueue.append(pop + n_index)
                # print("append : ", pop + n_index, end=" ")
                # cnt += 1   
    queue = copy.deepcopy(tmpQueue)
    # print(queue), checking shallow copy 
    tmpQueue.clear()
    # print(queue)
