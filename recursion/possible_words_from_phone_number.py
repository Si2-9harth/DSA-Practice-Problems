#User function Template for python3


numbs = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

       
class Solution:
    
    #recursive function to return all possible words that can
    #be obtained by pressing given numbers.  
    def combo(self,phnum):
        
        #base case, if current output word is prepared.
        if len(phnum) == 1:
            #pushing the word in output list.
            return list(numbs[phnum[0]])
        else: 
            result = self.combo(phnum[:-1])
        return [(ch1+ch2) for ch1 in result for ch2 in numbs[phnum[-1]]]
    
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        number=""
        for i in a:
            number+=str(i)
        answer=self.combo(number)
        #returning the list.
        return answer      

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends