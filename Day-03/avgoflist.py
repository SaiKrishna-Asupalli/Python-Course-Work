#Calculate the average of numbers in a list using a for loop ?
nums=[1,2,3,4]

sum=0
for num in nums:
    sum += num

avg=sum/len(nums)
print("Average is: ",avg)
