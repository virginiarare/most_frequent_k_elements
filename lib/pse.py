# clarifying questions 
# Q1. What if there is a tie for most frequent value at the k boundary?
# A1. We will return A correct answer, but no guarantees about which one. 
# Q2. What if K is invalid? 
# A2. We will assume that the code will end up raising an error of some kind.
# Q3. What if there are negative nums? 
# A3. They should just work. Like positive numbers.

# Logical Steps 
# 1. Build a frequency map of the list elements and their count.
# 2. Get unique elements of the list into a new list, from map keys. 
# 3. Sort trhe unique values based on their counts. 
# 4. Return the first k values. 

def make_counts(arr):
    counts = {}
    for num in arr: 
        if num in counts: 
            counts[num] += 1 
        else: 
            counts[num] = 1 
    
    return counts


def most_frequent_k_elements(arr, k):
    counts = make_counts(arr)
    uniq_nums = list(counts.keys())
    uniq_nums.sort(key=lambda num: counts[num], reverse=True)
    # uniq_nums.sort(key=counts.get)
    return uniq_nums[:k]




