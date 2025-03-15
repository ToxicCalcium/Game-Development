usr_word = input("Please type something. ").lower()
def vowelChecker(s):
    vowels = {
        'a' : 0,
        'e' : 0,
        'i' : 0,
        'o' : 0,
        'u' : 0,
    }
    for i in s: # This for oop is used to check every character of the string 's'
        if i in vowels:
            vowels[i] += 1
    
    print('Vowels Count:\n')
    for b in vowels:
        print(b, ":", vowels[b])

def alphaChecker(s):
    alphabs = {
        'a' : 0,
        'b' : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k' : 0,
        'l' : 0,
        'm' : 0,
        'n' : 0,
        'o' : 0,
        'p' : 0,
        'q' : 0,
        'r' : 0,
        's' : 0,
        't' : 0,
        'u' : 0,
        'v' : 0,
        'w' : 0,
        'x' : 0,
        'y' : 0,
        'z' : 0,
    }
    for i in s:
        if i in alphabs:
            alphabs[i] += 1

    print('Alphabet Count:\n')
    for n in alphabs:
        print(n, ":", alphabs[n])



vowelChecker(usr_word)
alphaChecker(usr_word)