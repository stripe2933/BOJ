from math import inf

n = int(input())
a_seq = list(map(int, input().split()))

def solution(begin):
    if begin == n - 1:
        return (1, a_seq[-1], 0, inf)
    
    nxt_c_cnt, nxt_c_min, nxt_nc_cnt, nxt_nc_min = solution(begin + 1)
    return (*max((nxt_c_cnt + 1, a_seq[begin]) if a_seq[begin] < nxt_c_min else (-inf, nxt_c_min), (nxt_nc_cnt + 1, a_seq[begin]) if a_seq[begin] < nxt_nc_min else (-inf, nxt_nc_min)), *max((nxt_c_cnt, nxt_c_min), (nxt_nc_cnt, nxt_nc_min)))

print(max(solution(0)[::2]))

# from itertools import islice

# n = int(input())
# a_seq = list(map(int, input().split()))

# def lis(a_seq):
#     if len(a_seq) == 0:
#         return 0
    
#     result = 1
#     for i in range(len(a_seq)):
#         nxt = list(filter(lambda x: x > a_seq[i], islice(a_seq, i + 1, None)))
#         result = max(result, 1 + lis(nxt))
    
#     return result

# print(lis(a_seq))