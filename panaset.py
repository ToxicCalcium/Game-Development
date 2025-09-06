usr_word = input("Please type something: ").lower()

def pangramChecker(s):
    # full alphabet set
    alphabet_set = {
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    }

    # set of letters found in input
    input_set = set()
    for ch in s:
        if ch in alphabet_set:
            input_set.add(ch)

    # check coverage
    if alphabet_set.issubset(input_set):
        print("Yes, it's a pangram")
    else:
        print("No, it's not a pangram")


pangramChecker(usr_word)
