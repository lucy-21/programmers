""" 
직사각형 별찍기
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12969
- 입출력 예
입력 : 5 3
출력 :
*****
*****
*****
"""

def solution():
    a, b = map(int, input().strip().split(' '))
    
    # solution 1
    # for b_idx in range(0, b):
    #     for a_idx in range(0, a):
    #         print('*', end='')
    #     print('')
    
    # solution 2
    print((('*' * a) + '\n') * b)

if __name__ == "__main__":
    solution()