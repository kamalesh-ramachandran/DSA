class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]):
        found=[]
        dict1={}
        flag=float("inf")
        for index,value in enumerate(list1):
            dict1[value]=index
        for i,v in enumerate(list2):
            if v in dict1:
                add=dict1[v]+i
                if add<flag:
                    found=[v]
                    flag=add
                elif flag==add:
                    found.append(v)
        return found