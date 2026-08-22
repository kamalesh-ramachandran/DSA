class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        res=""
        for i in s:
            freq[i]=freq.get(i,0)+1
        sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for i in range(len(sorted_freq)):
            res+=sorted_freq[i][0]*sorted_freq[i][1]
        return res

        """
        for ch,count in sorted_freq:
            res+=ch*count
        """
        
