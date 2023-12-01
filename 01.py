with open('./inp/01.txt') as f:
    lines = f.read().split('\n')

# part A
_sum = 0
for line in lines: 
    digits = list(filter(lambda n: n.isdigit(), line))
    _sum += int(digits[0] + digits[-1])

print(_sum)

# part B

import string 

numbers = ["one","two","three","four","five","six","seven","eight","nine"] + [i for i in string.digits if i != '0']

to_digit_str = lambda i: i if i.isdigit() else str(numbers.index(i) + 1)

_sum = 0
for line in lines: 

    first = None; last = None; 

    for i in range(len(line)):
        for n in numbers:
            if line[i:i + len(n)] == n:
                if first == None: 
                    first = n
                    break
                else:
                    last = n
                    break

    if last == None: last = first
    _sum += int(to_digit_str(first) + to_digit_str(last))
    
print(_sum)