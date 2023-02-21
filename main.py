# Let Fib(n) be the string formed by concatenating the first n sequential 
# Fibonacci numbers (i.e. Fib(0) = 1, Fib(1) = 11, Fib(2) = 112, …).  
# Find the first ten-digit prime number that occurs as ten sequential digits in Fib(n).  
# Go to http://{prime number}.com to proceed with the interview.

# fib_nums[i] = ith fibonacci number
fib_nums = {0 : 0, 1 : 1}
# Fib_vals[n] = Fib(n) where n = fibonacci(i)
Fib_vals = {0 : '1', 1 : '11'}

# gives ith fibonacci number
def fibonacci(i):
    if i < 0:
        return -1
    elif i in fib_nums.keys():
        return fib_nums[i]
    else:
        fib_nums[i] = fibonacci(i-1) + fibonacci(i-2)
        return fib_nums[i]

# Fib(fibonacci(i)) == Fib(n) where n = fibonacci(i)
def Fib(i):
    if fibonacci(i) in Fib_vals:
        return Fib_vals[fibonacci(i)]
    else:
        Fib_vals[fibonacci(i)] = str(Fib(i-1)) + str(fibonacci(i))
        return Fib_vals[fibonacci(i)]

# recursive function
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def findKthPrime(k):
    found = False
    index = 3
    prime_count = 0
    cur_Fib = '11'
    start = 0

    while not found:
        cur_Fib = Fib(index)
        # cur_Fib += str(fibonacci(index))

        if len(cur_Fib) >= 10:
            # find each 10 digit sequence & check for primeness
            while start + 10 <= len(cur_Fib):
                sub = int(cur_Fib[start:start+10])
                if isPrime(sub):
                  prime_count += 1
                if prime_count >= k:
                  return sub
                start += 1

        index += 1
    
    return -1

def translate(val):
    char_list = []
    val = str(val)
    for i in range(0,9,2):
        char_list.append(val[i:i+2])

    output = ''
    for x in char_list:
        output += chr(int(x) % 26 + 65)
        
    return output

val_1 = findKthPrime(1)         # 2584418167
val_2 = findKthPrime(44722)     # 9046450429
val_3 = findKthPrime(53215)     # 9952635697
print('1st 10 digit prime: ' + val_1)             
print('44722nd 10 digit prime translation: ' + translate(val_2))        # MUTED
print('53215th 10 digit prime: ' + translate(val_3))                    # VALET