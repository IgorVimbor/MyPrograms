# Основной исполняемый модуль

from tkinter import *
from tkinter import messagebox


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

# пустая строка
lbl = Label(window, text="", font=("Arial Bold", 2))
lbl.grid(row=0, column=0)

# формируем и размещаем строку с текстом "Число-ограничение:"
lbl_1 = Label(window, text="Число-ограничение:", font=("Arial Bold", 11))
lbl_1.grid(row=1, column=0, columnspan=3, sticky='e')

# формируем и размещаем поле для ввода числа-ограничения
entry_1 = Entry(font=("Arial Bold", 18), width=3)
entry_1.grid(row=1, column=3, sticky='w')
entry_1.focus()   # переводим курсор в поле для ввода числа-ограничения

# пустая строка
lbl = Label(window, text="", font=("Arial Bold", 2))
lbl.grid(row=2, column=0)

frm_1 = LabelFrame(window, text="1-2 класс", font=("Arial Bold", 15), labelanchor='n')
frm_1.grid(row=3, column=0, columnspan=4, sticky='n', padx=10)

frm_2 = LabelFrame(window, text="3-4 класс", font=("Arial Bold", 15), labelanchor='n')
frm_2.grid(row=3, column=5, columnspan=9, padx=5)

# формируем и размещаем строку с текстом "Сложение/вычитание 2-х чисел:"
lbl_2 = Label(frm_1, text="Сложение/вычитание 2-х чисел:", font=("Arial Bold", 11))
lbl_2.grid(row=0, column=0, sticky='e')

# формируем и размещаем кнопку-флажок для 2-х чисел
entry_bnt_1_state = BooleanVar()  # создаем объект для хранения логического значения виджета
entry_bnt_1_state.set(False)      # устанавливаем значение по умолчанию (флажок выключен)
entry_bnt_1 = Checkbutton(frm_1, width=3, variable=entry_bnt_1_state)  # создаем объект кнопки-флажка
entry_bnt_1.grid(row=0, column=1, sticky='w')                   # размещаем кнопку-флажок

# формируем и размещаем строку с текстом "3-х чисел:"
lbl_3 = Label(frm_1, text="3-х чисел:", font=("Arial Bold", 11))
lbl_3.grid(row=1, column=0, sticky='e')

# формируем и размещаем кнопку-флажок для 2-х чисел
entry_bnt_2_state = BooleanVar()  # создаем объект для хранения логического значения виджета
entry_bnt_2_state.set(False)      # устанавливаем значение по умолчанию (флажок выключен)
entry_bnt_2 = Checkbutton(frm_1, width=3, variable=entry_bnt_2_state)  # создаем объект кнопки-флажка
entry_bnt_2.grid(row=1, column=1, sticky='w')                   # размещаем кнопку-флажок

# формируем и размещаем строку с текстом "Сложение/вычитание со скобками:"
lbl_4 = Label(frm_2, text="Сложение/вычитание со скобками:", font=("Arial Bold", 11))
lbl_4.grid(row=0, column=0, sticky='e')

# формируем и размещаем кнопку-флажок для 2-х чисел
entry_bnt_3_state = BooleanVar()  # создаем объект для хранения логического значения виджета
entry_bnt_3_state.set(False)      # устанавливаем значение по умолчанию (флажок выключен)
entry_bnt_3 = Checkbutton(frm_2, width=3, variable=entry_bnt_3_state)  # создаем объект кнопки-флажка
entry_bnt_3.grid(row=0, column=1, sticky='w')                   # размещаем кнопку-флажок

# формируем и размещаем строку с текстом "Умножение/деление 2-х чисел:"
lbl_5 = Label(frm_2, text="Умножение/деление 2-х чисел:", font=("Arial Bold", 11))
lbl_5.grid(row=1, column=0, sticky='e')

# формируем и размещаем кнопку-флажок для 2-х чисел
entry_bnt_4_state = BooleanVar()  # создаем объект для хранения логического значения виджета
entry_bnt_4_state.set(False)      # устанавливаем значение по умолчанию (флажок выключен)
entry_bnt_4 = Checkbutton(frm_2, width=3, variable=entry_bnt_4_state)  # создаем объект кнопки-флажка
entry_bnt_4.grid(row=1, column=1, sticky='w')                   # размещаем кнопку-флажок

# формируем и размещаем строку с текстом "Смешанные примеры:"
lbl_5 = Label(frm_2, text="Смешанные примеры:", font=("Arial Bold", 11))
lbl_5.grid(row=2, column=0, sticky='e')

# формируем и размещаем кнопку-флажок для 2-х чисел
entry_bnt_5_state = BooleanVar()  # создаем объект для хранения логического значения виджета
entry_bnt_5_state.set(False)      # устанавливаем значение по умолчанию (флажок выключен)
entry_bnt_5 = Checkbutton(frm_2, width=3, variable=entry_bnt_5_state)  # создаем объект кнопки-флажка
entry_bnt_5.grid(row=2, column=1, sticky='w')                   # размещаем кнопку-флажок

# пустая строка
lbl = Label(window, text="", font=("Arial Bold", 2))
lbl.grid(row=4, column=0)

# формируем и размещаем строку с текстом "Реши пример:"
lbl_6 = Label(window, text="Реши пример:", font=("Arial Bold", 15))
lbl_6.grid(row=5, column=0, columnspan=2, sticky='e')

# формируем и размещаем поле, в которое будет автоматически вставлен пример
entry_2 = Entry(font=("Arial Bold", 35), width=12, justify='right')
entry_2.grid(row=6, column=2, columnspan=8)

# формируем и размещаем поле для ввода ответа
entry_3 = Entry(font=("Arial Bold", 35), width=2)
entry_3.grid(row=6, column=10)

# пустая строка
lbl = Label(window, text="", font=("Arial Bold", 4))
lbl.grid(row=7, column=0)

# формируем, привязываем к функции get_test и размещаем кнопку "Нажми и появится пример"
btn_1 = Button(window,
               text="Нажми \nи появится пример",  # текст на кнопке
               bg='linen',                        # цвет фона кнопки
               activebackground='peach puff',     # цвет кнопки при нажатии на нее
               font=("Arial Bold", 12),           # тип и размер шрифта
               command=None)                      # на какую команду реагирует
btn_1.grid(row=8, column=3, columnspan=5)

# формируем, привязываем к функции check_answer и размещаем кнопку "Проверить"
btn_2 = Button(window,
               text="Проверить",
               bg='linen',
               activebackground='peach puff',
               font=("Arial Bold", 15),
               command=None)
btn_2.grid(row=8, column=8, columnspan=9)

# пустая строка
lbl = Label(window, text="", font=("Arial Bold", 4))
lbl.grid(row=9, column=0)

# формируем и размещаем строку с текстом "Результат:"
lbl_7 = Label(window, text="Результат:", font=("Arial Bold", 15))
lbl_7.grid(row=10, column=0, columnspan=2, sticky='e')

# формируем и размещаем поле, в котором будет показан результат "Правильно/Не правильно"
entry_4 = Entry(font=("Arial Bold", 30), width=12)
entry_4.grid(row=10, column=2, columnspan=8)

# формируем и размещаем поле для смайликов
entry_5 = Entry(font=("Arial Bold", 37), width=2, justify='center')
entry_5.grid(row=10, column=10)

# пустая строка
lbl = Label(window, text="", font=("Arial Bold", 2))
lbl.grid(row=11, column=0)

# формируем и размещаем строки подписей полей "Правильно" и "Не правильно"
lbl_10 = Label(window, text="Правильно", font=("Arial Bold", 12))
lbl_10.grid(row=12, column=2)
lbl_11 = Label(window, text="Не правильно", font=("Arial Bold", 12))
lbl_11.grid(row=12, column=3, columnspan=4)

# формируем и размещаем строку с текстом "Решено примеров:"
lbl_12 = Label(window, text="Решено примеров:", font=("Arial Bold", 12))
lbl_12.grid(row=13, column=0, columnspan=2)

# формируем и размещаем поле для счетчика правильных ответов
entry_6 = Entry(font=("Arial Bold", 20), width=2, justify='center')
entry_6.grid(row=13, column=2)
entry_6.insert(0, '0')     # вставляем в поле счетчика цифру 0

# формируем и размещаем поле для счетчика неправильных ответов
entry_7 = Entry(font=("Arial Bold", 20), width=2, justify='center')
entry_7.grid(row=13, column=3, columnspan=4)
entry_7.insert(0, '0')     # вставляем в поле счетчика цифру 0

# запуск приложения
window.mainloop()
