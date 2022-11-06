"""
MONTE CARLO DEMONSTRATION
* GQC: Joe & Sang
* 2022/11/06
"""

from sequential import SampleNormalWongs, SampleOldestWongs
# from parallel import SampleNormalWongs, SampleOldestWongs

def main():
    while True:
        print("Number of samples:")
        N = int(input())

        print("Kind of Wong - 1 for normal; 2 for oldest:")
        k = int(input())

        if k == 1:
            print(SampleNormalWongs(N))
        else:
            print(SampleOldestWongs(N))

if __name__ == "__main__":
    main()