def wordBreak(s,wordDict):
    cList = {}
    def helper(s,wordDict,start,cList):
        #print (f"calling helper at {start}")
        n = len(s); cList[(start)] = False
        for end in range(start+1,n+1):
            prefix = s[start:end]
            if prefix in wordDict:
                if end in cList:
                    cList[(start)] = cList[(end)]
                    if cList[(start)] == True: break
                else:
                    #print (f"{end} not in cList, recursive calling {end}")
                    cList[(start)] = helper(s,wordDict,end,cList)
                    if cList[(start)] == True: break
                if end == n:
                    cList[(start)] = True
                    return True
        return cList[(start)]
    helper(s,wordDict,0,cList)
    return cList[(0)]

s = "applepenapple"
wordDict = ["apple", "pen"]
wordBreak(s,wordDict)
