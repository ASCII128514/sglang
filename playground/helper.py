import os


def readfile(file="text.txt", start_pos=0, length=1024):
    counter = 0
    res = []
    with open(file) as f:
        for line in f.readlines():
            res = res + line.split()
    
    return " ".join(res[start_pos:start_pos+length])



if __name__ == "__main__":
    print(readfile(length=10))