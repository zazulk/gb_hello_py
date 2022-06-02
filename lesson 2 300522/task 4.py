# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово
# длинное, выводить только первые 10 букв в слове.

# phrase = input("Скажите какую-нибудь фразу: ").strip().replace("  ", "")
# words = phrase.split()

print("Буду выводить нумерованный список слов.")
words = []
phrase = ""
punctuations = [",", ".", "!", ":", "–", "?", ";"]

while len(words) <= 1:
    if len(words) == 0:
        phrase = input("Скажите какую-нибудь фразу: ")
    if len(words) == 1:
        print("⚠️ Этого мало.")
        phrase += " " + input("Еще что-нибудь скажите: ")
    for mark in punctuations:
        phrase = phrase.replace(mark, " ")
    words = phrase.split()

print("\nРезультат:")
words = phrase.split()
for ind, word in enumerate(words, 1):
    print(ind, word[:11])

