#create func pass in string and character
#print out the positions of the character in the string

# Vlad, a ==> print out position of a, 2
# Solokha, o ==> print out 1 and 3

#func print out letter and number of times the letter is in the string

def position_of_char (input_string, char_in_string):
    arr = []
    for position in range(len(input_string)):
        # print(position)
        if input_string[position] == char_in_string:
            arr.append(position)
    
    return arr

myName = "vlad"
myLastName = "solokha"
character_in_myName = 'a'
character_in_my_Last_Name = 'o'


print(position_of_char(myName, character_in_myName))
print(position_of_char(myLastName, character_in_my_Last_Name))

