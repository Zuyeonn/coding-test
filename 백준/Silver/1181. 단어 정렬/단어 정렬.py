import sys

words = set()

for _ in range(int(sys.stdin.readline().strip())):
    words.add(sys.stdin.readline().strip())

words = list(words)
words.sort() 
words.sort(key = len) 

for word in words:
    print(word)