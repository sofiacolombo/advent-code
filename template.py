import sys
import time

def main():
    start_time = time.time()
    if len(sys.argv) < 2:
        sys.exit("Use: python3 name.py <inputfile.txt>")

    filename = sys.argv[1]
    
    with open(filename) as file:
        content = file.read().split('\n')[:-1]
        
    for line in content:
        print(line)
            
    print(' ',  )
    print("%s seconds" % (time.time() - start_time))
    

if __name__ == '__main__':
    main()
