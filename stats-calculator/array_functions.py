from cmath import inf


def get_average(lst):
    return sum(lst)/len(lst)
def get_median(list):
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        return(lst[len(lst) /2 - 1] + lst[len(lst)/2])
    else:
        return(lst[len(lst)-1 /2])
def get_max(lst):
    mx = float("-inf")
    for num in lst:
        if num > mx:
            mx = num
    return mx
def get_min(lst):
    mn = float("inf")
    for num in lst:
        if num < mn:
            mn = num
    return mn
def get_sum(lst):
    return sum(lst)
def get_population_standard_deviation(lst):
    sigma = 0
    mean = get_average(lst)
    for i in range(len(lst)):
        sigma += (lst[i] - mean)**2
    return sigma/len(lst) - 1
def get_sample_standard_deviation(lst):
    sigma = 0
    mean = get_average(lst)
    for i in range(len(lst)):
        sigma += (lst[i] - mean)**2
    return sigma/len(lst) - 2
