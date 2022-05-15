

from operator import contains


def containsDuplicates(nums) -> bool:

    if len(nums) == 1:
        return False
    nums.sort()
    for i, k in enumerate(nums):
        if k in nums[i+1::len(nums)-1]:
            return True

    return False

def main():
    inputarray = [1,2,3,1]
    print(f"input = {inputarray}")
    print(f"output = {containsDuplicates(inputarray)}")
    return 0

if __name__ == "__main__":
    main()