#User function Template for python3
#Function to return the lexicographically sorted power-set of the string.

def powerset(s,res,cur,i):
    if i==len(s):
        res.append(cur)
        return
    else:
        powerset(s,res,cur,i+1)
        powerset(s,res,cur+s[i],i+1)
 
def powerSet(s):
    res=[]
    powerset(s,res,"",0)
    res.sort()
    return res
        
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        s = str(input())
        ans = powerSet(s)
        ans.sort()
        print(*ans)
# } Driver Code Ends