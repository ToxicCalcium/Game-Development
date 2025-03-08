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

vowelChecker(usr_word)