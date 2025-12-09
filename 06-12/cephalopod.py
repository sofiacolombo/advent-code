import sys
import time
from functools import reduce

def main():
    start_time = time.time()
    if len(sys.argv) < 2:
        sys.exit("Use: python3 name.py <inputfile.txt>")

    filename = sys.argv[1]
    
    with open(filename) as file:
        content = file.read().split('\n')
        
    op = content[-1].split()
    total_sum = 0

    result = [tuple(map(int, s.split())) for s in content[:-1]]
    t = list(zip(*result)) # transpose
    
    for i,col in enumerate(t):
        if (op[i] == '*'):
            total_sum += reduce(lambda x,y: x*y, col)
        else:
            total_sum += sum(col)
        
    print('Total sum is', total_sum)
    print("%s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()
