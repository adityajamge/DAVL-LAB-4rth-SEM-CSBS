def mean(ar):
    return sum(ar) / len(ar)

def median(ar):
    sorted_ar = sorted(ar)
    n = len(sorted_ar)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_ar[mid - 1] + sorted_ar[mid]) / 2
    else:
        return sorted_ar[mid]

def mode(ar):
    frequency = {}
    for i in ar:
        frequency[i] = frequency.get(i, 0) + 1
    
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]


    if len(modes) == len(frequency):
        return None
    return modes

def variance(ar):
    m = mean(ar)
    return sum((x - m) ** 2 for x in ar) / len(ar)

def std_dev(ar):
    return math.sqrt(variance(ar))

def covariance(ar1, ar2):
    mean1 = mean(ar1)
    mean2 = mean(ar2)
      
    covar = sum((ar1[i] - mean1) * (ar2[i] - mean2) for i in range(len(ar1))) / len(ar1)
    return covar

def corelation(ar1, ar2):
    covar = covariance(ar1, ar2)
    stddev1 = std_dev(ar1)
    stddev2 = std_dev(ar2)
    
    return covar / (stddev1 * stddev2)

data = [1,2,3,4,5,6,7,8,8,9,9,10,10]
print(f"Mean: {mean(data)}")
print(f"Median: {median(data)}")    
print(f"Mode: {mode(data)}")

import math
print(f"Variance: {variance(data)}")
print(f"Standard Deviation: {std_dev(data)}")
print(f"Covariance: {covariance(data, data)}")
print(f"Correlation: {corelation(data, data)}")
