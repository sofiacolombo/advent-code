import sys
import time

def main():
    start_time = time.time()
    if len(sys.argv) < 2:
        sys.exit("Use: python3 joltage.py <inputfile.txt>")

    filename = sys.argv[1]
    total = 0
    
    with open(filename) as file:
        content = file.read().split('\n')[:-1]
        
    for line in content:
        maxd = nextd = 0
        digits = list(map(int, line))
        maxd = max(digits)
        
        i = digits.index(maxd)
        if i == len(digits)-1:
            maxd = max(digits[:i])
            i = digits.index(maxd)

        nextd = max(digits[i+1:])
        total = total + (maxd*10)+nextd
            
    print('Total sum', total)
    print("%s seconds" % (time.time() - start_time))
    

if __name__ == '__main__':
    main()
