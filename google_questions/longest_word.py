'''
Given string S and set of words D, 
find the longest word in D that is sub sequence of S

W is a subsequence of S if some number of chars (including 0)
can be deleted from S to form W, without reordering remaining chars

D can appear in any format (list, hash table, prefix tree, etc.)

Inputs:
S = 'abpplee'
D = {'able', 'ale', 'apple', 'bale', 'kangaroo'}

Output:
'apple'

explanation:
'able' and 'ale' are both subsequences (W) of S, but are shorter than 'apple'
'bale' is not W of S because even though S has right letters, they're 
not in the right order
'kangaroo' is longest word in D, but is not a W of S. 

potential solution:
look at each char in D for each word
check if match in S
if yes, keep word in D
if no, pop word in D
return word with max length
'''
def longest(S, D):
    # Build a map of char occurence indicies in S
    # Will be used later to binary search through
    smap = {}
    for char in S:
        smap[char] = # list of indicies where letter occurs
    matching_words = list(D)
    print(matching_words)
    longest_word = matching_words[0]
    for word in matching_words:
        for character in word:
            if character not in S:
                matching_words.remove(word)
                print('removed: ', word)
                break
        if len(word) > len(longest_word):
            longest_word = word
            print('longest word: ', longest_word)
    return longest_word

S = 'abpplee'
D = {'able', 'ale', 'apple', 'bale', 'kangaroo'}
print(longest(S,D))