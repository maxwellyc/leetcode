seen = set()

def check(num):
    print (num)
    if num == 1: return True
    if num in seen: return False
    seen.add(num)
    num = str(num)
    accu = 0
    for c in num:
        accu += (int(c))**2
    check(accu)


# visited = {}
# class Solution(object):
#     def isHappy(self, n):
#         l = []
#         for i in str(n):
#             l.append(int(i))
#         l = tuple(sorted(l))
#         while l:
#             if l in visited:
#                 if visited[l] == 1:
#                     return True
#                 elif visited[l]:
#                     l = visited[l]
#                 else:
#                     return False
#             else:
#                 t,sums = [],0
#                 for i in l:
#                     sums += i**2
#                 for j in str(sums):
#                     t.append(int(j))
#                 t = sorted(t)
#                 while t[0] == 0:
#                     t.pop(0)
#                 t = tuple(t)
#                 visited[l] = t
#                 if sums == 1:
#                     visited[l] = 1
#                     return True
#                 if l == t:
#                     visited[l] = 0
#                     return False
#                 if t in visited:
#                     return False
#                 l = t
#
# x = Solution()
# print (x.isHappy(4))
# print (visited)
