from numpy import append


def kfrequent(nums,k):
    freq = [[] for i in range(len(nums)+1)]
    count = {}
    res = []
    for n in nums:
        count[n] = 1 + count.get(n,0)
    # count c--> 0 1 2 3
    # number n-> [0][3][2][1]
    for n, c in count.items():
        freq[c].append(n)
    
    for k in range(len(freq)-1, 0, -1):
        for n in freq[k]:
            res.append(n)
            if len(res) == k:
                return res
        
    

def main():
    nums = [1,1,1,2,2,3]
    k= 2

    print(f"Output = {kfrequent(nums,k)}")
    return

if __name__ == "__main__":
    main()