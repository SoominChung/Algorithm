from itertools import permutations

def solution(numbers):
    houbo = []
    for i in range(1,len(numbers)+1):
        for num_list in set(permutations(numbers, i)):
                num = ''.join(map(str,num_list))
                houbo.append(num)
    houbo = set(map(int,houbo))
    
    answer = 0
    for num in houbo:     
        if is_prime(num):
            answer += 1
    return answer

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True