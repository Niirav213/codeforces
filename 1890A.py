import sys

def solve():

    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))

    my_dict = {}

    for i in a:
        my_dict[i] = my_dict.get(i,0) + 1
     
    if len(my_dict) >= 3:
        print("NO")
        
    elif len(my_dict) < 2:
            print("yes")
    else:
        freqs = list(my_dict.values())
        freq1 = freqs[0]
        freq2 = freqs[1]

        if abs(freq1 - freq2) <= 1:
            print("yes")
        else:
            print("NO")


def main():
    l = int(sys.stdin.readline())

    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()

