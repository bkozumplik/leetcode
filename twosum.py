#!/usr/bin/env python3

nums = [32,2,7,11,15] 
complement={}
found=False

target=int(input('whats the target: '))


for i in range(0,len(nums)):
	key_we_want=target-nums[i]
	if complement.get(key_we_want) is not None:
		match=complement[key_we_want]
		found=True
		print(match,i)
	else:
		complement[nums[i]]=i
if found is False:
	print('Not found')

			
