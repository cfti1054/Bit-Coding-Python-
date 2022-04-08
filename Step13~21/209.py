def wordlist(string):
    return string.upper().split(' ')

string = input('Enter the sentence : ')
print(wordlist(string))