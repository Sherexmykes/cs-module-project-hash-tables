def word_count(s):
    # Your code here
    a= dict()

    char_list = '"":;.,-+=/\|[]{}()*^&'

    new_s = s.lower().replace("\r", " ").replace(
        "\t", " ").replace("\n", " ").split(" ")

    print(new_s)

    for word in new_s:
        new_word = word.strip(char_list)
        print(new_word)

        if new_word not in a and new_word != "":
            a[new_word] = 1
        elif new_word != "":
            a[new_word] += 1

    return a



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))