nums = [2,12,3,15,6]
target = 9
q = {} #dictionary for hashing

for i in range(len(nums)):
    complement = target - nums[i]
    if q.get(complement)!=None: # already complement ase kina dict e key hishebe
        print(q[complement],i)
        break
    q.update({nums[i]:i})# value as key and index as value


