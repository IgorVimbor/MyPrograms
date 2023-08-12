from tkinter import *
from tkinter import messagebox
from example_generator import Example


# функция очищает все поля
def clear():
    entry_2.delete(0, END)     # удаляем текст из поля для примеров
    entry_3.delete(0, END)     # удаляем текст из поля для ответов
    entry_4.delete(0, END)     # удаляем текст из поля для результата
    # возвращаем поле для смайлика в исходное состояние
    entry_5 = Entry(font=("Arial Bold", 37), width=2)
    entry_5.grid(row=9, column=2)


# функция вставки в поле примера для решения
def get_test():
    clear()     # очищаем все поля
    # проверка - введено или нет число-ограничение
    try:
        num = int(entry_1.get())   # считываем с окна число-ограничение
        obj = Example(num)         # создаем экземпляр класса Example
    except:
        messagebox.showinfo('ВНИМАНИЕ!', 'Не введено число, в пределах которого\n'
                            'должны быть числа в примерах и результат.\n'
                            'Введите число-ограничение.')
    flag_1 = entry_bnt_1_state.get()    # считываем значение в первой кнопке-флажке
    flag_2 = entry_bnt_2_state.get()    # считываем значение во второй кнопке-флажке
    # если поставлен только первый флажок
    if flag_1 and not flag_2:
        entry_2.insert(0, obj.get_example(1, 0))   # в поле для примеров вставляем пример из 2 чисел
    # если поставлен только второй флажок
    if flag_2 and not flag_1:
        entry_2.insert(0, obj.get_example(0, 1))   # в поле для примеров вставляем пример из 3 чисел
    # если поставлены оба флажка
    if flag_1 and flag_2:
        entry_2.insert(0, obj.get_example(1, 1))   # в поле для примеров вставляем пример из 2 и 3 чисел
    # если флажки не поставлены
    if not entry_bnt_1_state.get() and not entry_bnt_2_state.get():
        messagebox.showinfo('ВНИМАНИЕ!', 'Не отмечено количество чисел в примере!\n'
                            'Выберите количество чисел - поставьте отметку\n'
                            'в первом или втором или в обоих полях.')
    entry_3.focus()   # переводим курсор в поле для ответа


# функция проверки введеного ответа, вывода результата и подсчета решеных примеров
def check_answer():
    global cnt_bad, cnt_good

    entry_4.delete(0, END)     # удаляем текст из поля для результата

    # считываем из поля для примеров сам пример, удаляем знак "=" и пробел
    test = entry_2.get().split(' =')[0]       # например: 12 - 10 + 6

    try:
        result_to_test = eval(test)           # решаем считанный пример
        answer = int(entry_3.get())           # считываем ответ из поля для ответов

        # сравниваем ответ с решением, выводим соответствующий результат и смайлик, окрашиваем поля
        if answer == result_to_test:
            entry_4.insert(0, 'Правильно!')
            entry_5 = Entry(font=("Arial Bold", 37), width=2, background='aquamarine')  # цвет - зеленый
            entry_5.grid(row=9, column=2)
            entry_5.insert(0, '\U0001F31E')   # радостное солнышко 🌞
            cnt_good += 1                     # увеличиваем счетчик на 1
            entry_6.delete(0, END)            # удаляем старое значение счетчика из поля
            entry_6.insert(0, f'{cnt_good}')  # вставляем новое значение счетчика
        else:
            entry_4.insert(0, 'Не правильно')
            entry_5 = Entry(font=("Arial Bold", 37), width=2, background='IndianRed1')  # цвет - красный
            entry_5.grid(row=9, column=2)
            entry_5.insert(0, '\U0001F61F')   # грустный смайлик 😟
            cnt_bad += 1                      # увеличиваем счетчик на 1
            entry_7.delete(0, END)            # удаляем старое значение счетчика из поля
            entry_7.insert(0, f'{cnt_bad}')   # вставляем новое значение счетчика
            messagebox.showwarning('НЕПРАВИЛЬНЫЙ ОТВЕТ!', 'ПОДУМАЙТЕ, ИСПРАВЬТЕ ОТВЕТ\n\n'
                                   'И НАЖМИТЕ КНОПКУ "Проверить"...\n\n'
                                   'ИЛИ РЕШИТЕ ДРУГОЙ ПРИМЕР.')
    except:
        messagebox.showinfo('ОШИБКА!', 'Нельзя проверить то, чего нет )))\n'
                            'Нажмите кнопку "Нажми и появится пример".')


# функция для запрета накручивания счетчика правильно решенных примеров
def stop_repets():
    res = entry_4.get()
    check_answer() if not res or res == 'Не правильно' else None


cnt_good = cnt_bad = 0   # счетчики решеных примеров

# создание окна
window = Tk()

# устанавливаем ширину и высоту окна
width = 610
heigh = 460
# определяем координаты центра экрана и размещаем окно
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
window.title(f"ПОРЕШАЙКА by IgorVimbor\n{' ' * 20} Примеры по математике")    # текст заголовка

# формируем пустые строки (label) для красоты окна
for i in (4, 6, 8, 10, 11):
    lbl = Label(window, text="")
    lbl.grid(row=i, column=0)

# формируем и размещаем строку с текстом "Число-ограничение:"
lbl_1 = Label(window, text="Число-ограничение:", font=("Arial Bold", 11))
lbl_1.grid(row=0, column=1, sticky='e')

# формируем и размещаем поле для ввода числа-ограничения
entry_1 = Entry(font=("Arial Bold", 20), width=3)
entry_1.grid(row=0, column=2, sticky='w')
entry_1.focus()   # переводим курсор в поле для ввода числа-ограничения

# формируем и размещаем строку с текстом "Показывать примеры с 2-мя числами:"
lbl_2 = Label(window, text="Показывать примеры с 2-мя числами:", font=("Arial Bold", 12))
lbl_2.grid(row=1, column=1, sticky='e')

# формируем и размещаем кнопку-флажок для 2-х чисел
entry_bnt_1_state = BooleanVar()  # создаем объект для хранения логического значения виджета
entry_bnt_1_state.set(False)      # устанавливаем значение по умолчанию (флажок выключен)
entry_bnt_1 = Checkbutton(width=3, variable=entry_bnt_1_state)  # создаем объект кнопки-флажка
entry_bnt_1.grid(row=1, column=2, sticky='w')                   # размещаем кнопку-флажок

# формируем и размещаем строку с текстом "с 3-мя числами:"
lbl_3 = Label(window, text="с 3-мя числами:", font=("Arial Bold", 12))
lbl_3.grid(row=2, column=1, sticky='e')

# формируем и размещаем кнопку-флажок для 3-х чисел
entry_bnt_2_state = BooleanVar()
entry_bnt_2_state.set(False)
entry_bnt_2 = Checkbutton(width=3, variable=entry_bnt_2_state)
entry_bnt_2.grid(row=2, column=2, sticky='w')

# формируем и размещаем строку с текстом "Реши пример:"
lbl_4 = Label(window, text="Реши пример:", font=("Arial Bold", 15))
lbl_4.grid(row=3, column=0, sticky='e')

# формируем и размещаем поле, в которое будет автоматически вставлен пример
entry_2 = Entry(font=("Arial Bold", 37), width=12, justify='right')
entry_2.grid(row=5, column=1, sticky='e')

# формируем и размещаем поле для ввода ответа
entry_3 = Entry(font=("Arial Bold", 37), width=2)
entry_3.grid(row=5, column=2)

# формируем, привязываем к функции get_test и размещаем кнопку "Нажми и появится пример"
btn_1 = Button(window,
               text="Нажми \nи появится пример",  # текст на кнопке
               bg='linen',                        # цвет фона кнопки
               activebackground='peach puff',     # цвет кнопки при нажатии на нее
               font=("Arial Bold", 12),           # тип и размер шрифта
               command=get_test)                  # на какую команду реагирует
btn_1.grid(row=7, column=1)

# формируем, привязываем к функции check_answer и размещаем кнопку "Проверить"
btn_2 = Button(window,
               text="Проверить",
               bg='linen',
               activebackground='peach puff',
               font=("Arial Bold", 15),
               command=stop_repets)
btn_2.grid(row=7, column=2)

# формируем и размещаем строку с текстом "Результат:"
lbl_8 = Label(window, text="Результат:", font=("Arial Bold", 15))
lbl_8.grid(row=9, column=0)

# формируем и размещаем поле, в котором будет показан результат "Правильно/Не правильно"
entry_4 = Entry(font=("Arial Bold", 30), width=12)
entry_4.grid(row=9, column=1)

# формируем и размещаем поле для смайликов
entry_5 = Entry(font=("Arial Bold", 37), width=2)
entry_5.grid(row=9, column=2)

# формируем и размещаем строки подписей полей "Правильно" и "Не правильно"
lbl_10 = Label(window, text="Правильно", font=("Arial Bold", 12))
lbl_10.grid(row=11, column=1, sticky='e')
lbl_11 = Label(window, text="Не правильно", font=("Arial Bold", 12))
lbl_11.grid(row=11, column=2)

# формируем и размещаем строку с текстом "Решено примеров:"
lbl_12 = Label(window, text="Решено примеров:", font=("Arial Bold", 12))
lbl_12.grid(row=12, column=1)

# формируем и размещаем поле для счетчика правильных ответов
entry_6 = Entry(font=("Arial Bold", 20), width=2, justify='center')
entry_6.grid(row=12, column=1, sticky='e')
entry_6.insert(0, '0')     # вставляем в поле счетчика цифру 0

# формируем и размещаем поле для счетчика неправильных ответов
entry_7 = Entry(font=("Arial Bold", 20), width=2, justify='center')
entry_7.grid(row=12, column=2)
entry_7.insert(0, '0')     # вставляем в поле счетчика цифру 0

# запуск приложения
window.mainloop()
