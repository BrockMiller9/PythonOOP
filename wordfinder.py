"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    ...

    def __init__(self, path):
        self.path = path
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f'{len(self.words)} words read')

    def parse(self, dict_file):
        return [w.strip() for w in dict_file]

    def random(self):

        return random.choice(self.words)


# word = WordFinder('/words.txt')
# print(word.open_file())
wf = WordFinder(
    r"C:\Users\9broc\OneDrive\Desktop\Springboard\Python\pythonOOP\words.txt")
print(wf.random())


class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)

    def parse(self, dict_file):
        return [w.strip() for w in dict_file if w.strip() and not w.startswith('#')]
