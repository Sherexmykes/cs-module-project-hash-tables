def no_dups(s):
    # Your code here
    # Best idea is to set filter for duplicates
    words = set()

#Then we can split the repeated
    wordList = s.split()
    #  outputs
    output = ""

    for word in wordList:
        # if the word is not  in our set
        if word not in words:
            # We add the word to our set
            words.add(word)
            output += word + " "
    #  remove spaces at the beginning and end of a string
    return output.strip()

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))