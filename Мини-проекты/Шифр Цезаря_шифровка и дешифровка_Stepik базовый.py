# Программа шифрования и дешифрования текста алгоритмом Цезаря.
# Она должна запрашивать у пользователя следующие данные:
# •	направление: шифрование или дешифрование;
# •	язык алфавита: русский или английский;
# •	шаг сдвига (со сдвигом вправо).

# приветствие
print("-" * 100)
print("Привет! Добро пожаловать в программу Шифр Цезаря.")
print(
    "Программа шифрует и дешифрует введенный на русском или английском языках текст по алгоритму Цезаря."
)
print("-" * 100)


# функция проверки правильности ввода 0 и 1
def check(answer):
    while answer != "0" and answer != "1":
        print("ОШИБКА: Вы ввели недопустимую цифру.")
        answer = input('Введите цифру "0" или цифру "1". \n')
    return answer


# функция проверки языка
def check_text(txt, lng):
    for i in txt:
        if lng == "0" and i.isalpha() and i not in ru:
            return False
        elif lng == "1" and i.isalpha() and i not in en:
            return False
    else:
        return True


ru = "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
en = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# запрос информации от пользователя
direct = input(
    'Что программа должна сделать? Шифровать - введите цифру "0", дешифровать - цифру "1". \n'
)
check(direct)
language = input(
    'Какой язык вы выбираете? Русский – введите цифру "0", английский - цифру "1". \n'
)
check(language)
step = int(input("Укажите шаг сдвига для шифрования / дешифрования. Введите цифру. \n"))
print("-" * 100)

# ввод текста с проверкой, что текст не набор только цифр и пробелов и проверкой соответствия языка
while True:
    text = input("Введите исходный текст. \n")
    if text.isdigit() or text.isspace():
        print("ОШИБКА: Вы ввели что-то непонятное для программы.")
        text = input("Введите текст. \n")
    if check_text(text, language):
        print("Программа приступает к работе.", "-" * 100, sep="\n")
        break
    else:
        print("Язык сообщения не соответствует выбранному языку. Попробуйте еще раз.")
        print("-" * 100)


# функция шифрования и дешифрования
def cezar(txt, lng):
    if lng == "0":
        alphabet = ru
        power = 32
    else:
        alphabet = en
        power = 26
    for i in range(len(text)):
        if txt[i].isalpha():
            if txt[i] == txt[i].lower():
                if direct == "0":
                    print(alphabet[(alphabet.index(text[i]) + step) % power], end="")
                if direct == "1":
                    print(alphabet[(alphabet.index(text[i]) - step) % power], end="")
            if txt[i] == txt[i].upper():
                if direct == "0":
                    print(
                        alphabet[(alphabet.index(text[i]) + step) % power + power],
                        end="",
                    )
                if direct == "1":
                    print(
                        alphabet[(alphabet.index(text[i]) - step) % power + power],
                        end="",
                    )
        else:
            print(text[i], end="")


if direct == "0":
    print("Зашифрованный текст:")
if direct == "1":
    print("Дешифрованный текст:")
cezar(text, language)
print()
print("-" * 100)
