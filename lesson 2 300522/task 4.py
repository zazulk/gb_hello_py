# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово
# длинное, выводить только первые 10 букв в слове.

# phrase = input("Скажите какую-нибудь фразу: ").strip().replace("  ", "")
# words = phrase.split()

print("Буду выводить нумерованный список слов.")
words = []
phrase = ""
punctuations = [",", ".", "!", ":", "–", "?", ";"]
stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
stop = False

while len(words) <= 1 and not stop:
    if phrase in stop_words:
        print("Ну и ладно :(")
        stop = True
        break
    if len(words) == 0:
        phrase = input("Скажите какую-нибудь фразу или введите 'Q' для выхода: ")
    if len(words) == 1:
        print("⚠️ Этого мало.")
        phrase += " " + input("Еще что-нибудь скажите: ")
    for mark in punctuations:
        phrase = phrase.replace(mark, " ")
    words = phrase.split()

if not stop:
    print("\nРезультат:")
    words = phrase.split()
    for ind, word in enumerate(words, 1):
        print(f"{ind}. {word[:10]}")

