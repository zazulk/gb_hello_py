# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово
# длинное, выводить только первые 10 букв в слове.

phrase = input("Скажите какую-нибудь фразу: ")

phrase = phrase.replace("  ", "")
punctuations = [",", ".", "!", ":", "–", "?", ";"]
for mark in punctuations:
    phrase = phrase.replace(mark, "")

words = phrase.split()
for ind, word in enumerate(words):
    print(ind, word[:11])

