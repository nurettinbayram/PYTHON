# You are given an integer array nums consisting of 2 * n integers.
# You need to divide nums into n pairs such that:
# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.

nums = [3,2,3,2,2,2]
#nums = [1,2,3,4]
n = int(len(nums)/2)
nums.sort()


#print(all (nums[i] == nums[i+1] for i in range(0, len(nums), 2) ))
# all ---> tum kosullar true ise true aksi taktirde false dondurur

#pairs = [nums[i:i+2] for i in range(0, len(nums), 2)]
# yukaridaki code for dongusu ile her aldigi i uzerinde islem yapar bir daha i yi 2 arttirip gene ele alir