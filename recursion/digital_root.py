#User function Template for python3

def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10+sum_of_digits(n//10)

class Solution:
    def digitalRoot(self, n):
        '''
        :param n: given number 
        :return: digital root as defined
        '''
        if n//10==0:
            return n
        else:
            n=sum_of_digits(n)
            return self.digitalRoot(n)
            
            

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
        n = int(input())
        print(Solution().digitalRoot(n))
# } Driver Code Ends