import string

def anagram_signature (text):
    """Converts a string into a tuple of letter counts."""
    lc = ''.join(filter(str.isalpha, text)).lower()
    return tuple([lc.count(i) for i in string.ascii_lowercase])

filename = "anagrams.txt"
anagram_sets = dict()
for line in open(filename):
    line = line.rstrip('\n')
    sig = anagram_signature(line)
    if sig not in anagram_sets:
        anagram_sets[sig] = set()
    anagram_sets[sig].add(line)

for key,anagram_sets in anagram_sets.items():
    if len(anagram_sets) > 1:
        print('----------')
        for line in anagram_sets:
            print(line)