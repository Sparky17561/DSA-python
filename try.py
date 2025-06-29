nums = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
# answer = 9
i=0
for j in range(1,len(nums)):
    if nums[j] != nums[i]:
        i+=1
    nums[i]=nums[j]

print(i+1)