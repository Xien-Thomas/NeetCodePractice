def productArray(nums):
    #pre 1[1 2 6 24]
    pre = []
    post = []
    res = []
    product = 1
    for n in range(0,len(nums)):
        product *= nums[n] 
        pre.append(product)
    
    product = 1
    for n in range(len(nums)-1,-1,-1):
        product *= nums[n] 
        post.append(product)
        print(product)
    post.reverse()
   
    for n in range(0,len(nums)):
        if n == 0:
            res.append(1 * post[n+1])
        elif n == len(nums)-1:
            res.append(pre[n-1] * 1)
        else:
            res.append(pre[n-1] * post[n+1])
    return res

def main():
    input = [-1,1,0,-3,3]
    print(f"Output = {productArray(input)}")
    return 0

if __name__ == "__main__":
    main()