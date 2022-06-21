from collections import defaultdict
def groupanagrams(strs):
    dict = defaultdict(list)

    for s in strs:
        count = [0]*26
        for c in s: #TEA
            count[ord(c) - ord("a")] +=1
        dict[tuple(count)].append(s)
    

    return dict.values()

def main():
    input = ["eat","tea","tan","ate","nat","bat"]
    output = groupanagrams(input)

    print(f"input = {input}")
    print(f"output = {output}")
    return


if __name__ == "__main__":
    main()