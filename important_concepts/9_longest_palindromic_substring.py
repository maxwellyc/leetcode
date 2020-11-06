#class Solution:
#    def checkEven(self,i):
#            j = 0; count = 0
#            while i-j>0 and i+j<self.n:
#                if self.s[i-j-1] == self.s[i+j]:
#                    count+=2;j+=1
#                else: break
#            if count>self.size:
#                c = count//2
#                self.ans,self.size = self.s[i-c:i+c],count
#            return
#    def checkOdd(self,i):
#        j = 1; count = 1
#        while i-j>-1 and i+j<self.n:
#            if self.s[i-j] == self.s[i+j]:
#                count+=2;j+=1
#            else: break
#        if count>self.size:
#            c = count//2
#            self.ans,self.size = self.s[i-c:i+c+1],count
#        return
#
#    def main(self,s):
#        self.n,self.s = len(s),s
#        self.m,self.ans,self.size = (self.n+1)//2,"",0
#        for i in range(self.m-1,-1,-1):
#            self.checkOdd(i)
#            self.checkEven(i)
#            self.checkEven(self.n-i-1)
#            if not (self.n%2 and i==self.m-1):
#                self.checkOdd(self.n-i-1)
#        return self.ans
class Solution:
    def longestPalindrome(self, s):
        maxlen,begin=1,0
        if len(s)<2 or s==s[::-1]:
            return s
        for i in range(1,len(s)):
            odd=s[i-maxlen-1:i+1]
            even=s[i-maxlen:i+1]
            print (i,odd,even)
            if i-maxlen-1>=0 and odd==odd[::-1]:
                begin=i-maxlen-1
                maxlen+=2
                continue
            if i-maxlen>=0 and even==even[::-1]:
                begin=i-maxlen
                maxlen+=1
            print (i,odd,even,maxlen,begin)
            print ("*******************")
        return s[begin:begin+maxlen]

s = "abcedaadecbaa"
A = Solution()
print ("final:",A.longestPalindrome(s))
