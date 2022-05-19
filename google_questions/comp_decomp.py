'''
Decompress a compressed string
Input: a compressed string in format
number[string]
Output: a decompressed string written number times
Examples:
Input: 3[abc]4[ab]c
Output: abcabcabcababababc
Rules: 
10[a] is allowed
2[3[a]b] is allowed => aaabaaab
char can be digits, small Eng letters and brackets
digits only repr no. of repetitions
letters are just letters
brackts are only part of syntax of writing repeated substring
input is always valid, no need to check validity

Learning objectives:
practice strings, recursion, algorithm, compilers, automata, and loops. Work on coding with better efficiency.
'''
'''
traverse string with i through length of string-1
  result += i # If i is letter or number just add it to result
  if i is [, result += *(
    if i+1 is letter, result += ' 
  elif i is ], replace with ')+
    if i+1 is letter, result += ' 
  if last item 
    if i is ], replace with ')
    if i is letter, result += i+'
'''
# print('3[abc]4[ab]c should be: ', 3*('abc')+4*('ab')+'c')
# print('10[a] should be: ', 10*('a'))
# print('2[3[a]b] should be: ', 2*(3*('a')+'b'))

def decomp(s):
  result = ''
  for i in range(len(s)-1):
    if s[i] == '[':
      result += '*'
      if s[i+1].isalpha():
        result += '\''
    elif s[i] == ']':
      result += '\'+'
      if s[i+1].isalpha():
        result += '\''
    else:
      result += s[i]
  if s[-1] == ']':
    result += '\''
  else:
    result += s[-1]+'\''
  res = eval(result)
  return print(res)

decomp('5[two]8[six]')
decomp('2[3[a]b]')