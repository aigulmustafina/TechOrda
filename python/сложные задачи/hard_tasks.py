##sum-1-n 

n = int(input('Enter the number: '))
if 1 <= n <= 65535: 
    array = range(1, n+1)
    print(sum(array))
else:
    print('The number is out of range')

##count-leap-year 
def count_leap_year(year):
    count = 0
    i = 0
    while i != year:
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            count += 1
        i += 1
    return f"До года {year} присутстует {count} високосных лет."

# print(count_leap_year(100))

##swap-bits 
def swap_bits(a):
    if 0 <= a <= 255:
        high_bits = a >> 4
        low_bits = a & 0b1111
        swap = low_bits << 4 | high_bits
        return bin(swap)
    else:
        return "The value is out of the range"
    
# print(swap_bits(0b00001111)) 
# print(swap_bits(0b01100111)) 

##swap-bits - option 2
def swap_bits(a):
    bits_str = f"{a:08b}"
    swapped = bits_str[4:] + bits_str[4:]
    return int(swapped, 2)


print(swap_bits(0b00001111))



##sort-nums-three 
def sort_three_nums(a, b, c): 
    if a < b and a < c: 
        min_num = a
        if b < c: 
            second_min = b
            max_num = c
        else:
            second_min = c
            max_num = b
    elif b < c and b < a:
        min_num = b
        if c < a: 
            second_min = c
            max_num = a
        else:
            second_min = a
            max_num = c
    elif c < a and c < b:
        min_num = c
        if b < a: 
            second_min = b
            max_num = a
        else:
            second_min = a
            max_num = b
    return f'Sorted numbers: {[min_num, second_min, max_num]}'

# print(sort_three_nums(8, 4, 25))

##median  
def get_median(arr):
    if 0 <= len(arr) <= 10_000:
        arr.sort()
        median = len(arr) // 2
        if len(arr) % 2 == 0: 
            return arr[median - 1]
        else:
            return arr[median]
            

# print(get_median([1, 4, 3, 2, 5, 6]))
# print(get_median([1, 6, 3, 4, 5, 2, 7]))

##miss-you 
def get_difference(arr1, arr2):
    return sorted(list(set(arr2).difference(set(arr1))))

print(get_difference([1, 1, 3, 2, 5], [1, 3, 9, 1, 5, 7]))

##perfectly-balanced 
def is_perfectly_balanced(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if right_sum == left_sum:
            return True
        left_sum += arr[i]
    return False

# print(is_perfectly_balanced([1, 2, 9, 8, 5, 7]))


##stock-buy 
def buy_stock(m, s):
    if m > 1 and 0 <= len(s) <= 10_000:
        for i in range(len(s)):
            for j in range(i + 1, len(s)): 
                sum = s[i] + s[j]
                if sum == m:
                    return [i, j]
    else:
        return 'Data is not valid'

# print(buy_stock(8, [1, 2, 3, 8, 5]))

##hanoi-tower 
def hanoi_towers(n, source_tower, target_tower, extra_tower):
    if n == 1:
        print(f"Диск 1 с башни {source_tower} переложить в башню {target_tower}")
        return
    hanoi_towers(n-1, source_tower, extra_tower, target_tower)

    print(f"Диск {n} с башни {source_tower} переложить в башню {target_tower}")

    hanoi_towers(n-1, extra_tower, target_tower, source_tower)


n = int(input('Введите количество дисков: '))
hanoi_towers(n, 1, 2, 3)

