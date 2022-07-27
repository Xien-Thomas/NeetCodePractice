from typing import List


def twoSum(nums, target)-> List[int]:
    if len(nums) < 2:
        return []

    L = 0
    R = len(nums) -1

    while L != R:
        sum = nums[L] + nums[R]
        if target == sum:
            return [L, R]
        if target > sum:
            L +=1
        elif target < sum:
            R -=1

    return []

def main():
    inputNums = [2,7,11,15]
    inputTarget = 9
    print(f"input (S,T) = ({inputNums},{inputTarget})")
    print(f"output = {twoSum(inputNums,inputTarget)}")
    return 0

if __name__ == "__main__":
    main()