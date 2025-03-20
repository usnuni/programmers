def solution(n, k):
    answer = 0
    answer += n * 12000
    
    num_service = n // 10
    answer += (k-num_service) * 2000
    
    return answer