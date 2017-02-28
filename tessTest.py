# # you can write to stdout for debugging purposes, e.g.
# # print "this is a debug message"
#
# def solution(A, B, M, X, Y):
#     # write your code in Python 2.7
#     i = 0
#     pCnt = 0
#     eCnt = 0
#     weightSum = 0
#     pList = []
#     pDict = {}
#     while i < len(A):
#         if i < len(A)-1:
#             if pCnt < X and weightSum + A[i+1] < Y:
#                 pCnt += 1
#                 weightSum += A[i]
#                 pList.append(B[i])
#             if pCnt >= X or weightSum + A[i+1] >= Y:
#                 if len(pList) != 0:
#                     pList = sorted(pList)
#                     for j in range(0, len(pList)):
#                         if pDict.get(pList[j], 0) == 0:
#                             pDict[pList[j]] = 1
#                             eCnt += 1
#                     eCnt += 1
#                     pCnt = 0
#                     weightSum = 0
#                     pList = []
#                     pDict = {}
#         if i == len(A)-1:
#             if pCnt < X and weightSum < Y:
#                 pCnt += 1
#                 weightSum += A[i]
#                 pList.append(B[i])
#                 if len(pList) != 0:
#                     pList = sorted(pList)
#                     for j in range(0, len(pList)):
#                         if pDict.get(pList[j], 0) == 0:
#                             pDict[pList[j]] = 1
#                             eCnt += 1
#                     eCnt += 1
#                     pCnt = 0
#                     weightSum = 0
#                     pList = []
#                     pDict = {}
#         i += 1
#     return eCnt
#
# print(solution([40,40,100,80,20],[3,3,2,2,3],3,5,200))
# #print(solution([60, 80, 40], [2, 3, 5], 5, 2, 200))
#
#
#
#
#
#
#
#
#
#

def solution(A, K):
    n = len(A)
    best = 0
    count = 1
    for i in range(1, n - K):
        if (A[i] == A[i - 1]):
            count = count + 1
        else:
           count = 1
        best = max(best, count)
    result = best + K if K < n else n

    return result

print(solution([1,1,3,3,3,4,5,5,5,5],0))
print(solution([1,1,3,3,3,4,5,5,5,5],2))
print(solution([1,1,1,1],0))
print(solution([1,1,1,1],4))
print(solution([1,1,1,2,3,3],0))
print(solution([1,3,3,3,3,3],0))
