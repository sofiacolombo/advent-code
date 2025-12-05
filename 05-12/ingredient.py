import sys
import time

def main():
    start_time = time.time()
    if len(sys.argv) < 2:
        sys.exit("Use: python3 name.py <inputfile.txt>")

    filename = sys.argv[1]
    count = 0

    with open(filename) as file:
        content = file.read().split('\n')[:-1]
    
    half = content.index('')
    ranges = content[:half]
    foodIDs = content[half+1:]

    for id in foodIDs:
        for range in ranges:
            start,end = map(int, range.split('-'))
            if int(id) >= start and int(id) <= end:
                count+=1
                break
   
    print('Total fresh ingredients',  count)
    print("%s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()
