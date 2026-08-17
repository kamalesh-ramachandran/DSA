class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        dict2={}
        found=[]
        for i in nums1:
            dict1[i]=dict1.get(i,0)+1
        for j in nums2:
            dict2[j]=dict2.get(j,0)+1
        for key in dict1:
            if key in dict2:
                value=min(dict1[key],dict2[key])
                for _ in range(value):
                    found.append(key)
        return found


        
        

        
