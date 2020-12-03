
def loadWords():
    """
    Returns a list of valid words. 
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    file = open('words.txt', 'r')
    wordslist = file.readlines()
    print(f"{len(wordslist)} words loaded!")
    return wordslist

def find_anagrams(words, string):
    anagrams = []
    for word in words:
        if sorted(string) == sorted(word[:-1]):
            anagrams.append(word[:-1])
    return anagrams

word_list = loadWords()
word = input("Enter a string of text: ")
anagrams = find_anagrams(word_list,word)
print(f"{len(anagrams)} anagrams found!")
print(anagrams)

