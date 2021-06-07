"""
행렬의 덧셈
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12950
- 입출력 예
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]
"""

def solution(arr1, arr2):
    # solution 1
    # return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[i]))] for i in range(len(arr1))]
    # solution 2
    return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]

if __name__ == "__main__":
    arr1 = [[1,2],[2,3]]
    arr2 = [[3,4],[5,6]]
    result = solution(arr1, arr2)
    print(result)