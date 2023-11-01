s = "{{)}()"

def validPar(s):
    opcl = {
        '{' : '}',
        '[' : ']',
        '(' : ')'
    }
    stack = []

    for char in s:
        if char in opcl.keys():
            stack.append(char)
        else:
            if len(stack) == 0 or char!= opcl[stack.pop()]:
                return False

    if len(stack) == 0:     
        return True     
    else:       
        return False        

valid = validPar(s)
print(valid)
    