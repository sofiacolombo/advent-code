import sys
import time

# not very efficient but works
def main():
    start_time = time.time()
    if len(sys.argv) < 2:
        sys.exit("Use: python3 paper-rolls.py <inputfile.txt>")

    filename = sys.argv[1]
    
    with open(filename) as file:
        content = file.read().split('\n')
    
    count = 0
    coordinates = []
    
    row = 0
    for line in content:
        coordinates.extend(getCoordsFromLine(row, line))
        row+=1

    for i in range(len(coordinates)-1, -1, -1):
        if getCountFromCoords(coordinates[i], coordinates) < 4:
            count+=1

    
    print("Il numero di paper roll accessibili",count)
    print("%s seconds" % (time.time() - start_time))

def getCoordsFromLine(row, line):
    r = []
    col = 0
    for col, char in enumerate(line):
        if char == '@':
            r.append((row, col))
    
    return r

def getCountFromCoords(coords, fullList):
    y = coords[0]
    x = coords[1]

    adj = [(y-1,x-1), (y-1, x), (y-1, x+1), 
           (y, x-1),             (y, x+1), 
           (y+1, x-1), (y+1, x), (y+1, x+1)]
    
    local_count = 0
    for couple in adj:
        if couple[0] < 0 or couple[1] < 0:
            continue

        if couple in fullList:
            local_count+=1
    return local_count
    

if __name__ == '__main__':
    main()
