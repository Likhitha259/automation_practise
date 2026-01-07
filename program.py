def longest_word_without_char_repetition(string,long=''):
    for i in string:
        unique=''
        for j in i:
            if j not in unique:
                unique+=j
        if len(long)<len(unique):
            long=unique
    return long
print(longest_word_without_char_repetition(input('enter:').split()))

''' length of the longest alphabetical continuous substring.'''
# alt ans:
def longestContinuousSubstring(self, s: str) -> int:
        max_len = 1
        curr_len = 1

        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i-1]) + 1:
                curr_len += 1
            else:
                curr_len = 1
            max_len = max(max_len, curr_len)

        return max_len
# my ans :
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        long=''
        for i in s:
            if i not in long:
                if long=='':
                    long+=i
                else:
                    if ord(i)==ord(long[-1])+1:
                        long+=i
                    else:
                        break
            else:
                break
        return len(long)

a='"nkvexzqgctjxwqnzneuvtuvyvrmhfbawyabanxadvlzllpwnanjxyjhhzzjokcszjeooitnvadkuzsnklxriwo"'
z=""
z1 = ""
for i in a:
    z += i
    if z in ("".join([chr(i) for i in range(ord("a"),ord("z")+1)])):
        z1=z
    else:
        z=i
print(len(z1))