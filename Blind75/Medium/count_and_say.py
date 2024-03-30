"""
link: https://leetcode.com/problems/count-and-say/description/

countAndSay(1) = 1
countAndSay(2) = 11 (one "1")
countAndSay(3) = 21 (two "1"'s)
countAndSay(4) = 1211 (one "2" and one "1")
countAndSay(5) = 111221 (one "1" + one "2" + two "1"s)


res = str(count) + str(curr_str)

"""
def countAndSay(n):
    if n == 1:
        return "1"

    say = countAndSay(n-1)
    # an empty result string
    result = ""
    count = 1
    current_char = say[0]
    for i in range(1, len(say)):
        # increment count of the char till we find a different character
        if say[i] == current_char:
            count +=1
        else:
            result += str(count) + str(current_char)
            # increment the current char to the next one
            current_char = say[i]
            # reset the count to 1
            count = 1

    result += str(count) + str(current_char)
    return result


n = 4
res = countAndSay(n)
print(res)
