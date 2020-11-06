intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort(key=lambda x:x[0])
ans, n = [], len(intervals)
start, end = -1,-1
for i in range(n):
    s, e = intervals[i]
    print (s,e,(start,end))
    if start == -1:
        start = s
        end = e
        continue
    if i == n-1:
        if s > end:
            ans.append([start,end])
            ans.append([s,e])
        else:
            ans.append([start,max(end,e)])
        break#print( ans)
    if s <= end:
        end = max(end,e)
    else:
        ans.append([start,end])
        start = s
        end = e

print (ans)
