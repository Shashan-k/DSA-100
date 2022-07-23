##Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

##You may assume that each input would have exactly one solution, and you may not use the same element twice.

##You can return the answer in any order.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        s = len(numbers) - 1
        ans = []
        while(f<s):
            summ = numbers[f] + numbers[s]
            if summ < target :
                f+=1
            elif summ > target :
                s-=1
            else:
                ans.append(f+1)
                ans.append(s+1)
                break
        return ans                
               
