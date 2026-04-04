import sys
def main():
    weight = int(sys.stdin.readline().strip())
    if not (weight & 1) and weight>2 :
        print("YES")
        return
    print("NO")
    return

if __name__=="__main__":
    main()