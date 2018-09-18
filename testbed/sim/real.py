import glob
import re

def main():
    biggestInt = 0
    for filename in glob.iglob('./logfiles/*.txt'):
        with open(filename, "r") as logFile:
            stringData = logFile.readlines()
            for i in range(0, len(stringData)):
                if "Commit new mining work" in stringData[i]:
                    m = stringData[i].split("number=",1)[1]
                    m = re.search("\d+", m).group()
                    if int(m) > int(biggestInt):
                        biggestInt = m
    arr = [0]*(int)(biggestInt)
    for filename in glob.iglob('./logfiles/*.txt'):
        with open(filename, "r") as logFile:
            stringData = logFile.readlines()
            for i in range(0, len(stringData)):
                if "block  became a side fork" in stringData[i]:
                    m = stringData[i].split("number=",1)[1]
                    m = re.search(r"\d+", m).group()
                    arr[(int)(m)] = 1
    age = [0]*10
    count = 0
    for j in range(0, len(arr)):
        if(arr[j] == 1):
            count = count + 1
        if(arr[j] == 0 or j == len(arr)-1):
            age[count] = age[count] + 1
            count = 0
    print age

if __name__ == "__main__":
    main()
