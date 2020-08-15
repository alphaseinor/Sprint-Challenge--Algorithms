'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # less than two does not match, also our exit strategy, works with odd and even :)
    if len(word) < 2:
        return 0
    else:
        # first two characters match
        if word[0:2] == 'th':
            # return 1 + remove first two letters
            return 1 + count_th(word[2:])
        else:
            # return remove first letter
            return count_th(word[1:])
    
