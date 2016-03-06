# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

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

print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
