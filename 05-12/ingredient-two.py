import sys
import time

def main():
    start_time = time.time()
    if len(sys.argv) < 2:
        sys.exit("Use: python3 name.py <inputfile.txt>")

    filename = sys.argv[1]
    count = 0

    with open(filename) as file:
        content = file.read().split('\n')

    half = content.index('')
    content = content[:half]

    #for range in content:
    #    count += (end-start+1)
    sorted = [list(map(int, range.split('-'))) for range in content]
    sorted.sort()
    
    result = []
    r = sorted[0]
    result.append(r)

    for range in sorted:
        if range[0] <= r[1]:
            r[1] = max(r[1], range[1])
        else:
            r = range
            result.append(r)
    
    for range in result:
        start = range[0]
        end = range[1]
        count+= end-start+1

    print('Total fresh ingredients',  count)
    print("%s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()
