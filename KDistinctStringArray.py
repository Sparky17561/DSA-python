# brute force

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        
        res=[]
        hash1={}

        for i in range(len(arr)):
            if arr[i] not in res and arr[i] not in hash1:
                res.append(arr[i])
        
            else:
                if arr[i] in res:
                    res.remove(arr[i])
                hash1[arr[i]] = 0

        if len(res) >= k:
            return res[k-1]
        else:
            return ""


        

# better solution
        
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        d={}
        count=1
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]]+=1
            else:
                d[arr[i]]=1
        for i in range(len(arr)):
            if arr[i] in d and d.get(arr[i])==1:
                if count==k:
                    return arr[i]
                else:
                    count+=1
        return ""
        
        

        