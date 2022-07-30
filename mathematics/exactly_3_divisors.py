#{ 
#Driver Code Starts
#Initial Template for Python 3


import math


 # } Driver Code Ends
#User function Template for python3
import math
class Solution:
    def exactly3Divisors(self,N):
        t=math.floor(pow(N,0.5))+1
        primes=[True]*t
        for i in range(2,t):
            if primes[i]:
                j=2*i
                while j<t:
                    primes[j]=False
                    j=j+i
        ans=0
        for i in range(2,t):
            if primes[i]:
                ans+=1
        return ans
                    

#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        ob=Solution()
        print(ob.exactly3Divisors(N))
        
        T-=1
    

if __name__=="__main__":
    main()
#} Driver Code Ends