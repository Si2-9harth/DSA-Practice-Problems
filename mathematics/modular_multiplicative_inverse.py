#{ 
#Driver Code Starts
#Initial Template for Python 3


import math



 # } Driver Code Ends
#User function Template for python3
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
        
class Solution:    
    ##Complete this function
    def modInverse(self,a,m):
        if gcd(a,m)==1:
            for i in range(0,m):
                if (i*a)%m==1:
                    return i
            return -1
        else:
            return -1

#{ 
#Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        am=[int(x) for x in input().strip().split()]
        a=am[0]
        m=am[1]
        ob=Solution()
        print(ob.modInverse(a,m))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends