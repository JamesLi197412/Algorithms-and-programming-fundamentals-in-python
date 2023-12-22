# Task 1 Palindrome:Part A
def palindrom(wrods):
    length = len(words)
    for i in range(length):
        if words[i] != words[length-i-1]:
            return False
        else:
            pass

words=input('Please enter a word: ')
Dis = palindrom(words)
if Dis == False:
    print('Unfortunately',words,'is not a palindrome')
else:
    print('Great,',words,'is a palindrome.')

# Task 1 palindromic senstences-- Part B

sentence =input('Please enter a sentence: ')

def palindromic(sentence):
    sentence=sentence.split()
    sentence = ''.join(sentence)
    sentence = sentence.split(',')
    sentence = ''.join(sentence)
    sentence = sentence.split('?')
    sentence = ''.join(sentence)
    sentence = sentence.split('.')
    sentence = ''.join(sentence)
    sentence = sentence.lower()
    print(sentence) ##Perfect

palindromic(sentence)
