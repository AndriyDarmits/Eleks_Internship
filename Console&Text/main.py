# Написати консольну програму яка зчитує файл і
# виводить частоту використання різних слів починаючи від найбільш вживаних слів закінчуючи найменш вживаними словами.
from collections import Counter
import os
import re

f = open("Text.txt", "r")
text = f.read()
wordlist=re.findall(r"[\w']+",text)# ділимо текст на слова
wordlist = list(filter(None, wordlist))

print("Text:\n" + text + "\n") # текст з файлу
print("List of words:\n" + str(wordlist) + "\n") # список окремих слів з тексту

wordlist=[x.lower() for x in wordlist]

print("Word and Frequencies:")
counts = Counter(wordlist)
print(str(counts))
os.system("pause")