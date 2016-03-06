# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def next_letter(letter):
    if letter != 'z':
        return chr(ord(letter)+1)
    else:
        return 'a'
def previous_letter(letter):
    if letter != 'a':
        return chr(ord(letter)-1)
    else:
        return 'z'

def shift_n_letters(letter, n):
    if n >= 0:
        i = 0
        result = letter
        while i < n:
            result = next_letter(result)
            i += 1
        return result
    else:
        i = 0
        result = letter
        while i > n:
            result = previous_letter(result)
            i = i - 1
        return result

def rotate(word, n):
    i = 0
    result = ''
    while i < len(word):
        if word[i] != ' ':
            result = result + shift_n_letters(word[i], n)
            i += 1
        else:
            result = result + ' '
            i += 1
    return result



print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
