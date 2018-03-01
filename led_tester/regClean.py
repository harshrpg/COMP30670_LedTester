import re
def regexClean(instructions,L):
    regex = re.compile(
        ".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    result = regex.search(instructions)
    if result != None:
        method = str(result.group(1)).strip()
        l1 = int(result.group(2))
        l2 = int(result.group(3))
        l3 = int(result.group(4))
        l4 = int(result.group(5))
        if l1 < 0:
            l1 = 0
        if l2 < 0:
            l2 = 0
        if l3 > L:
            l3 = L-1
        if l4 >= L:
            l4 = L-1
        return method, l1, l2, l3, l4
    else:
        return None, None, None, None, None
   
