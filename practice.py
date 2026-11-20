# def are_anagrams(n1: int, n2: int) -> bool:
#     if n1 == 0 and n2 == 0:
#         return True
        
#     freq = [0] * 10
    
#     while n1 > 0:
#         freq[n1 % 10] += 1
#         n1 //= 10
            
#     for count in freq:
#         if count != 0:
#             return False        
#     return True


def analyze_numbers(numbers)
    :print("maximum =", max(numbers))
    print("minimum =", min(numbers))
    print("sum =", sum(numbers))
    print("average =", sum(numbers)/len(numbers))
analyze_numbers([10, 20, 30, 40]) 