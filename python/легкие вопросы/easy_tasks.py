#

def compare(a, b):
    if a > b:
        return 1
    elif a == b: 
        return 0
    else:
        return -1
    
# print(compare(7, 6))


##max-of-three
def max_of_three(a, b, c):
    return max(a, b, c)

# print(max_of_three(1, 0, 42))

##sqr-sum-1-n
def get_sum_of_sqr(n):
    result = 0
    if 1 <= n <= 10860:
        for i in range(1, n+1):
            result += i**2
        return result
    else:
        return('Please enter a number betwwen 1 and 10860')
 

# print(get_sum_of_sqr(7))


##print-even-a-b

def get_even(a, b):
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i, end=' ')

# get_even(5, 15)

##pow-a-b

def get_power(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return 'Please enter an integer'
    power = 1
    for i in range(b):
        power *= a
    return power

# print(get_power(2, 7))

##calc-deposit
def calc_deposit(balance, percent, duration):
    for i in range(duration):
        balance += balance * percent/100
    return round(balance, 2)

# print(calc_deposit(1000, 5, 10))
    

#Массивы
##Min
def get_min(array):
    if not array:
        return 0
    if 0 <= len(array) <= 10_000: 
        return sorted(array)[0]
    else: 
        return "Array length is out of range"
    
# print(get_min([6, 9, 4, 0]))

##range
def get_range(n):
    if 0 < n <= 10000:
        arr = []
        for i in range(1, n + 1):
            arr.append(i)
        return arr
    else:
        return "Please enter number in range {1: 10000}"

# print(get_range(10))


##sum
def get_sum(array):
    result = 0
    for num in array:
        result += num
    return result

# print(get_sum([4, 5, 8, 7]))

##sort
def sort_arr(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


# print(sort_arr([1, 2, 0, 5, 4, 8]))


