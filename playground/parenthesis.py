def isValid(self, s: 'str') -> 'bool':
    # return false when str has odd length
    if len(s)%2: return False
    mapping = {")":"(","]":"[","}":"{"}
    stack = []
    for ss in s:
        if ss in mapping:
            if mapping[ss] == stack[-1]:
                stack.pop()
                continue
        stack.append(ss)
    return (not stack)
