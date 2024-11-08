# Основной исполняемый модуль

import tkinter as tk
from tkinter import messagebox
import winsound

from factory_examples.show_example_v2 import Show_test


# функция очищает все поля
def clear():
    entry_2.delete(0, tk.END)  # удаляем текст из поля для примеров
    entry_3.delete(0, tk.END)  # удаляем текст из поля для ответов
    entry_4.delete(0, tk.END)  # удаляем текст из поля для результата
    # возвращаем поле для смайлика в исходное состояние
    entry_5 = tk.Entry(font=("Arial Bold", 37), width=2, justify="center")
    entry_5.grid(row=10, column=8)


# функция для проверки входных данных и вставки задания для решения в поле
def get_test():
    clear()  # очищаем поля предыдущего примера
    try:
        num = int(entry_1.get())  # считываем с окна число-ограничение
        obj = Show_test(num)  # создаем экземпляр класса Show_test
    except ValueError:  # если число-ограничение не введено
        messagebox.showinfo(
            "ВНИМАНИЕ!",
            "Не введено число, не более которого\n"
            "будут числа в примерах.\n\n"
            "ВВЕДИТЕ ЧИСЛО-ОГРАНИЧЕНИЕ.",
        )
    try:  # считываем значения в кнопках-флажках
        flg_1 = int(entry_bnt_1_state.get())
        flg_2 = int(entry_bnt_2_state.get())
        flg_3 = int(entry_bnt_3_state.get())
        flg_4 = int(entry_bnt_4_state.get())
        flg_5 = int(entry_bnt_5_state.get())
        flg_6 = int(entry_bnt_6_state.get())
        mask = flg_1, flg_2, flg_3, flg_4, flg_5, flg_6
        entry_2.insert(0, obj.get_example(*mask))  # вставляем сгенерированное задание
        entry_3.focus()  # переводим курсор в поле для ответа
    except:  # если ни одного флажка не поставлено
        messagebox.showinfo(
            "ВНИМАНИЕ!",
            "Не выбраны варианты заданий!\n\n"
            "ПОСТАВЬТЕ ГАЛОЧКУ В ОДНОМ\nИЛИ НЕСКОЛЬКИХ ПОЛЯХ.",
        )


# функция для проверки введеного ответа, вывода результата и подсчета решеных примеров
def check_answer():
    global cnt_bad, cnt_good

    entry_4.delete(0, tk.END)  # удаляем текст из поля для результата

    # считываем из поля для примеров сам пример, удаляем знак "=" и пробел
    test = entry_2.get().split(" =")[0]  # например: 12 - 10 + 6
    # заменяем знаки Юникода '·' и '∶'
    test = test.replace("∶", "/") if "∶" in test else test
    test = test.replace("·", "*") if "·" in test else test

    try:
        result_to_test = int(eval(test))  # решаем считанный пример
        answer = int(entry_3.get())  # считываем ответ из поля для ответов

        # сравниваем ответ с решением, выводим соответствующий результат и смайлик, окрашиваем поля
        if answer == result_to_test:  # если ответ пользователя правильный
            entry_4.insert(0, "Правильно!")
            entry_5 = tk.Entry(
                font=("Arial Bold", 37), width=2, background="aquamarine"
            )  # цвет - зеленый
            entry_5.grid(row=10, column=8)
            entry_5.insert(0, "\U0001F31E")  # радостное солнышко 🌞
            # воспроизведение звука из файла
            if entry_sound_state.get():
                winsound.PlaySound("sound_good.wav", winsound.SND_ASYNC)
            cnt_good += 1  # увеличиваем счетчик на 1
            entry_6.delete(0, tk.END)  # удаляем старое значение счетчика из поля
            entry_6.insert(0, f"{cnt_good}")  # вставляем новое значение счетчика
        else:  # если ответ пользователя не правильный
            entry_4.insert(0, "Не правильно")
            entry_5 = tk.Entry(
                font=("Arial Bold", 37), width=2, background="IndianRed1"
            )  # цвет - красный
            entry_5.grid(row=10, column=8)
            entry_5.insert(0, "\U0001F61F")  # грустный смайлик 😟
            # воспроизведение звука из файла
            if entry_sound_state.get():
                winsound.PlaySound("sound_bad.wav", winsound.SND_ASYNC)
            cnt_bad += 1  # увеличиваем счетчик на 1
            entry_7.delete(0, tk.END)  # удаляем старое значение счетчика из поля
            entry_7.insert(0, f"{cnt_bad}")  # вставляем новое значение счетчика
    except:
        messagebox.showinfo(
            "ОШИБКА!",
            "Нельзя проверить то, чего нет )))\n\n"
            "РЕШИ ПРИМЕР или НАЖМИ КНОПКУ,\nчтобы появился другой пример",
        )


# функция для однократного считывания введенного результата для кнопки "Проверить"
# (не позволяет накручивать счетчик правильно решенных примеров)
def stop_repets():
    res = entry_4.get()
    check_answer() if not res or res == "Не правильно" else None


# функция для однократного считывания введенного результата при нажатии клавиши "Enter"
# (не позволяет накручивать счетчик правильно решенных примеров)
def on_enter_press(event):
    res = entry_4.get()
    check_answer() if not res or res == "Не правильно" else None


cnt_good = cnt_bad = 0  # счетчики решеных примеров


# создание окна
window = tk.Tk()

# устанавливаем ширину и высоту окна
width = 620
heigh = 450
# определяем координаты центра экрана и размещаем окно
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry(
    "%dx%d+%d+%d"
    % (width, heigh, (screenwidth - width) / 2, (screenheight - heigh) / 2)
)
# текст заголовка
window.title(f"ПОРЕШАЙКА by IgorVimbor\n{' ' * 20} Примеры по математике")

# формируем пустые строки для лучшей визуализации приложения
for i in (0, 2, 3, 7, 9, 11):
    lbl = tk.Label(window, text="", font=("Arial Bold", 2))
    lbl.grid(row=i, column=0)

# формируем и размещаем строку с текстом "Число-ограничение:"
lblw_1 = tk.Label(window, text="Число-ограничение:", font=("Arial Bold", 11))
lblw_1.grid(row=1, column=0, sticky="e")

# формируем и размещаем поле для ввода числа-ограничения
entry_1 = tk.Entry(font=("Arial Bold", 18), width=3)
entry_1.grid(row=1, column=1, sticky="w")
entry_1.focus()  # переводим курсор в поле для ввода числа-ограничения

lblw_1_1 = tk.Label(window, text="Звуки:", font=("Arial Bold", 11))
lblw_1_1.grid(row=1, column=7, sticky="e")

# формируем и размещаем во фрейме кнопку-флажок для звука
entry_sound_state = tk.BooleanVar()  # объект для хранения логического значения виджета
entry_sound_state.set(False)  # устанавливаем значение по умолчанию (флажок выключен)
# создаем объект кнопки-флажка
entry_sound = tk.Checkbutton(window, width=3, variable=entry_sound_state)
entry_sound.grid(row=1, column=8, sticky="w")  # размещаем кнопку-флажок

# формируем и размещаем фрейм для строк и кнопок-флажков
frm_1 = tk.LabelFrame(
    window, text="Варианты заданий", font=("Arial Bold", 14), labelanchor="n"
)
frm_1.grid(row=3, column=0, columnspan=9, sticky="w", padx=10)

# формируем и размещаем во фрейме строку с текстом "Сложение/вычитание 2-х чисел:"
lbl_1 = tk.Label(frm_1, text="Сложение/вычитание 2-х чисел:", font=("Arial Bold", 11))
lbl_1.grid(row=0, column=0, sticky="e")

# формируем и размещаем во фрейме строку с текстом "3-х чисел:"
lbl_2 = tk.Label(frm_1, text="3-х чисел:", font=("Arial Bold", 11))
lbl_2.grid(row=1, column=0, sticky="e")

# формируем и размещаем во фрейме строку с текстом "Сложение/вычитание со скобками:"
lbl_3 = tk.Label(frm_1, text="Сложение/вычитание со скобками:", font=("Arial Bold", 11))
lbl_3.grid(row=2, column=0, sticky="e")

# формируем и размещаем во фрейме кнопку-флажок для 2-х чисел
entry_bnt_1_state = tk.BooleanVar()  # объект для хранения логического значения виджета
entry_bnt_1_state.set(False)  # устанавливаем значение по умолчанию (флажок выключен)
# создаем объект кнопки-флажка
entry_bnt_1 = tk.Checkbutton(frm_1, width=3, variable=entry_bnt_1_state)
entry_bnt_1.grid(row=0, column=1, sticky="w")  # размещаем кнопку-флажок

# формируем и размещаем во фрейме кнопку-флажок для 3-х чисел
entry_bnt_2_state = tk.BooleanVar()
entry_bnt_2_state.set(False)
entry_bnt_2 = tk.Checkbutton(frm_1, width=3, variable=entry_bnt_2_state)
entry_bnt_2.grid(row=1, column=1, sticky="w")  # размещаем кнопку-флажок

# формируем и размещаем во фрейме кнопку-флажок для сложения/вычитания со скобками
entry_bnt_3_state = tk.BooleanVar()
entry_bnt_3_state.set(False)
entry_bnt_3 = tk.Checkbutton(frm_1, width=3, variable=entry_bnt_3_state)
entry_bnt_3.grid(row=2, column=1, sticky="w")  # размещаем кнопку-флажок

# формируем и размещаем во фрейме строку с текстом "Умножение/деление 2-х чисел:"
lbl_4 = tk.Label(frm_1, text="Умножение/деление 2-х чисел:", font=("Arial Bold", 11))
lbl_4.grid(row=0, column=2, sticky="e")

# формируем и размещаем во фрейме строку с текстом "Слож./выч. и умн./дел. без скобок:"
lbl_5 = tk.Label(
    frm_1, text="Слож./выч. и умн./дел. без скобок:", font=("Arial Bold", 11)
)
lbl_5.grid(row=1, column=2, sticky="e")

# формируем и размещаем во фрейме строку с текстом "Слож./выч. и умн./дел. со скобками:"
lbl_6 = tk.Label(
    frm_1, text="Слож./выч. и умн./дел. со скобками:", font=("Arial Bold", 11)
)
lbl_6.grid(row=2, column=2, sticky="e")

# формируем и размещаем во фрейме кнопку-флажок для умножения/деления 2-х чисел
entry_bnt_4_state = tk.BooleanVar()
entry_bnt_4_state.set(False)
entry_bnt_4 = tk.Checkbutton(frm_1, width=3, variable=entry_bnt_4_state)
entry_bnt_4.grid(row=0, column=3, sticky="w")  # размещаем кнопку-флажок

# формируем и размещаем во фрейме кнопку-флажок для cложения/вычитания и умножения/деления без скобок
entry_bnt_5_state = tk.BooleanVar()
entry_bnt_5_state.set(False)
entry_bnt_5 = tk.Checkbutton(frm_1, width=3, variable=entry_bnt_5_state)
entry_bnt_5.grid(row=1, column=3, sticky="w")  # размещаем кнопку-флажок

# формируем и размещаем во фрейме кнопку-флажок для сложения/вычитания и умножения/деления со скобками
entry_bnt_6_state = tk.BooleanVar()
entry_bnt_6_state.set(False)
entry_bnt_6 = tk.Checkbutton(frm_1, width=3, variable=entry_bnt_6_state)
entry_bnt_6.grid(row=2, column=3, sticky="w")  # размещаем кнопку-флажок

# формируем и размещаем строку с текстом "Реши пример:"
lblw_2 = tk.Label(window, text="Реши пример:", font=("Arial Bold", 15))
lblw_2.grid(row=5, column=0, sticky="e")

# формируем и размещаем поле, в которое будет автоматически вставлен пример
entry_2 = tk.Entry(font=("Arial Bold", 35), width=12, justify="right")
entry_2.grid(row=6, column=0, columnspan=8, sticky="e")

# формируем и размещаем поле для ввода ответа
entry_3 = tk.Entry(font=("Arial Bold", 35), width=3)
entry_3.grid(row=6, column=8)

# формируем, привязываем к функции get_test и размещаем кнопку "Нажми и появится пример"
btn_1 = tk.Button(
    window,
    text="Нажми \nи появится пример",  # текст на кнопке
    bg="linen",  # цвет фона кнопки
    activebackground="peach puff",  # цвет кнопки при нажатии на нее
    font=("Arial Bold", 12),  # тип и размер шрифта
    command=get_test,  # на какую команду реагирует
)
btn_1.grid(row=8, column=1, columnspan=5, sticky="e")

# формируем, привязываем к функции stop_repets и размещаем кнопку "Проверить"
btn_2 = tk.Button(
    window,
    text="Проверить",
    bg="linen",
    activebackground="peach puff",
    font=("Arial Bold", 12),
    command=stop_repets,
)
btn_2.grid(row=8, column=8, columnspan=10, sticky="w")
# Привязываем событие нажатия на клавишу Enter к функции on_enter_press
entry_3.bind("<Return>", on_enter_press)

# формируем и размещаем строку с текстом "Результат:"
lblw_3 = tk.Label(window, text="Результат:", font=("Arial Bold", 15))
lblw_3.grid(row=10, column=0, sticky="e")

# формируем и размещаем поле, в котором будет показан результат "Правильно/Не правильно"
entry_4 = tk.Entry(font=("Arial Bold", 30), width=12)
entry_4.grid(row=10, column=1, columnspan=7)

# формируем и размещаем поле для смайликов
entry_5 = tk.Entry(font=("Arial Bold", 37), width=2, justify="center")
entry_5.grid(row=10, column=8)

# формируем и размещаем строки подписей полей "Правильно" и "Не правильно"
lblw_4 = tk.Label(window, text="Правильно", font=("Arial Bold", 12))
lblw_4.grid(row=12, column=1)
lblw_5 = tk.Label(window, text="Не правильно", font=("Arial Bold", 12))
lblw_5.grid(row=12, column=2, columnspan=4)

# формируем и размещаем строку с текстом "Решено примеров:"
lblw_6 = tk.Label(window, text="Решено примеров:", font=("Arial Bold", 12))
lblw_6.grid(row=13, column=0, sticky="e")

# формируем и размещаем поле для счетчика правильных ответов
entry_6 = tk.Entry(font=("Arial Bold", 20), width=2, justify="center")
entry_6.grid(row=13, column=1)
entry_6.insert(0, "0")  # вставляем в поле счетчика цифру 0

# формируем и размещаем поле для счетчика неправильных ответов
entry_7 = tk.Entry(font=("Arial Bold", 20), width=2, justify="center")
entry_7.grid(row=13, column=2, columnspan=4)
entry_7.insert(0, "0")  # вставляем в поле счетчика цифру 0

# запуск приложения
window.mainloop()

# pyinstaller --onefile --windowed --add-data "sound_good.wav;." --add-data "sound_bad.wav;." ПОРЕШАЙКА_v2.py
