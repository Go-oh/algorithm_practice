# https://github.com/Go-oh/python-for-coding-test/blob/master/8/6.py
# 왼쪽부터 하나씩 쌓아올라감. 단, 붙어있나 아니냐가 변수일뿐.
# 직접 그려보면 쉬움
n, k = int(input()), list(map(int, input().split()))

d = [0] * 100
# d = list() 안됨

d[0] = k[0]
d[1] = max(k[0], k[1])

# for i in n-1:
for i in range(2, n) :
    d[i] = max(d[i-1], d[i-2]+k[i])
    # print("d[", i, "] : ", d[i], "= max(d[", i-1, "], d[", i-2, "] + array[", i, "])")

print(d[n-1])
    

  
  
  
# instance
# 11
# 4 5 1 3 4 10 1 5 8 4 3 

# d[0] :  4
#         5
#         5 v 4+1 -> 5
#         5 v 5+3 -> 8
#  d[4] : 8 v 5+4 -> 9      #4
#  d[5] : 9 v 10+8 -> 18    #10
#  d[6] : 18 v 1+9 -> 18    #1
#  d[7] : 18 v 18+5 -> 23   #5
#         23 v 18+8 -> 26   #8
#         26 v 23+4 -> 27   #4
#  d[10] :27 v 26+3 -> 29   #3 END
