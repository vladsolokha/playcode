'''
string, s, of lowercase English letters repeated 
infinitely many times. Given int, n, find and 
print the number of letter a's in the first n
letters of the infinite string.

example
s = 'abcac'
n = 10

the substing we consider is 'abcacabcac', the
first 10 characters of the infinite string. 
There are 4 occurances of a in the substring.

s: a string to repeat
n: the number of characters to consider
'''

def repeatedString(s, n):
    if s == 'a':
        return n
    
    string_length = len(s)
    s_length = n // string_length
    rem = n % string_length

    a_count_in_s = s.count('a')

    s_rem = s[:rem]
    a_count_in_rem = s_rem.count('a')

    return s_length * a_count_in_s + a_count_in_rem

s = 'afcfffaged'
n = 962645758455

print(repeatedString(s, n))
