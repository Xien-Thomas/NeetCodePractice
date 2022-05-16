def isAnagram(s,t) -> bool:
    if len(s) != len(t):
        return False

    hashmap = {}
    
    for k in s:
        if k not in hashmap:
            hashmap.update({k: 0})
        hashmap.update({k: hashmap[k]+1})

    for k in t:
        if k in hashmap:
            hashmap.update({k: hashmap[k]-1})
    
    for k in hashmap:
        if hashmap[k] != 0:
            return False

    return True

def main():
    inputS = "aacc"
    inputT = "ccac"
    print(f"input (S,T) = ({inputS},{inputT})")
    print(f"output = {isAnagram(inputS,inputT)}")
    return 0

if __name__ == "__main__":
    main()