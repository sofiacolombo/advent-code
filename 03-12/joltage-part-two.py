import sys
import time

def main():
    start_time = time.time()
    if len(sys.argv) < 2:
        sys.exit("Use: python3 joltage.py <inputfile.txt>")

    filename = sys.argv[1]
    total_sum = 0
    
    with open(filename) as file:
        content = file.read().split('\n')[:-1]
    
    for line in content:
        digits = list(map(int, line))

        first = max(digits[:-11])
        index = digits.index(first)
        
        total = twelveBatteries(digits, index, 1, first*(10**12))
        total_sum += total//10
            
    print('Total sum', total_sum)
    print("%s seconds" % (time.time() - start_time))

def twelveBatteries(digits, index, count, tot):
    end = len(digits) - (12-count) + 1

    if count == 12 or index >= len(digits):
        return tot
    
    elif index+1 >= end:
        sum = 0
        for i in range(12-count):
            sum += digits[index+1+i]*(10**(12-count-1-i))
        return tot + sum

    new_max = max(digits[index+1:end])
    i = index + 1 + digits[index+1:end].index(new_max)
    
    num = new_max*(10**(12-count))
    
    return twelveBatteries(digits, i, count+1, tot+num)

if __name__ == '__main__':
    main()
