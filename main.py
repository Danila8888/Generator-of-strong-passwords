from tkinter import Tk, Button, IntVar, Checkbutton, Label, W, Scale, HORIZONTAL, StringVar, filedialog

def generate(ifdigit, ifletters, iflettersstr, ifsymbols, counter):
    from random import choice
    password_end = ""
    password = list('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM%*)?@#$~')
    if (ifdigit.get() == 0 and ifletters.get() == 0 and iflettersstr.get() == 0 and ifsymbols.get() == 0):
        return "Выберите хотя-бы один пункт из предложенных"
    if (counter.get() == 0):
        return "Пароль не может быть пустым"
    if (ifsymbols.get() == 0):
        password.remove('%')
        password.remove('*')
        password.remove(')')
        password.remove('?')
        password.remove('@')
        password.remove('#')
        password.remove('$')
        password.remove('~')
    if (iflettersstr.get() == 0):
        password.remove('M')
        password.remove('N')
        password.remove('B')
        password.remove('V')
        password.remove('C')
        password.remove('X')
        password.remove('Z')
        password.remove('L')
        password.remove('K')
        password.remove('J')
        password.remove('H')
        password.remove('G')
        password.remove('F')
        password.remove('D')
        password.remove('S')
        password.remove('A')
        password.remove('P')
        password.remove('O')
        password.remove('I')
        password.remove('U')
        password.remove('Y')
        password.remove('T')
        password.remove('R')
        password.remove('E')
        password.remove('W')
        password.remove('Q')
    if (ifdigit.get() == 0):
        password.remove('0')
        password.remove('1')
        password.remove('2')
        password.remove('3')
        password.remove('4')
        password.remove('5')
        password.remove('6')
        password.remove('7')
        password.remove('8')
        password.remove('9')
    if (ifletters.get() == 0):
        password.remove('m')
        password.remove('n')
        password.remove('b')
        password.remove('v')
        password.remove('c')
        password.remove('x')
        password.remove('z')
        password.remove('l')
        password.remove('k')
        password.remove('j')
        password.remove('h')
        password.remove('g')
        password.remove('f')
        password.remove('d')
        password.remove('s')
        password.remove('a')
        password.remove('p')
        password.remove('o')
        password.remove('i')
        password.remove('u')
        password.remove('y')
        password.remove('t')
        password.remove('r')
        password.remove('e')
        password.remove('q')
        password.remove('w')
    for i in range(0, counter.get()):
        password_end = password_end + choice(password)
    gen_button = Button(text="Скопировать предложенный пароль", command=bar, background = '#E0FFFF')
    gen_button.grid(row=8, column=0, sticky=W)
    return password_end

def foo():
    password_output.set(generate(digit_lang,letters_lang,lettersstr_lang,symbols_lang,count))

def bar():
    def exit():
        warning.destroy()
    if (password_output.get() == "Выберите хотя-бы один пункт из предложенных" or password_output.get() == "Пароль не может быть пустым"):
        warning = Tk()
        warning.title("Ошибка")
        warning.geometry("180x150")
        warning.configure(background='#E0FFFF')
        warning.resizable(False, False)
        warning_label = Label(warning, text="Пароль не сгенерирован", background='#E0FFFF')
        warning_label.grid(row=0, column=0, sticky=W)
        exit_button = Button(warning, text="Закрыть", command=exit, background='#E0FFFF')
        exit_button.grid(row=1, column=0, sticky=W)
        warning.mainloop()
    else:
        root.clipboard_clear()
        root.clipboard_append(password_output.get())

root = Tk()
root.title("Генератор паролей")
root.geometry("350x350")
root.configure(background = '#E0FFFF')

digit_lang = IntVar()
digit_checkbutton = Checkbutton(root,text="Наличие цифр", variable=digit_lang,
                                 onvalue=1, offvalue=0, padx=15, pady=10, background = '#E0FFFF')
digit_checkbutton.grid(row=0, column=0, sticky=W)

letters_lang = IntVar()
letters_checkbutton = Checkbutton(root,text="Наличие прописных букв", variable=letters_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10, background = '#E0FFFF')
letters_checkbutton.grid(row=1, column=0, sticky=W)

lettersstr_lang = IntVar()
lettersstr_checkbutton = Checkbutton(root,text="Наличие строчных букв", variable=lettersstr_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10, background = '#E0FFFF')
lettersstr_checkbutton.grid(row=2, column=0, sticky=W)

symbols_lang = IntVar()
symbols_checkbutton = Checkbutton(root,text="Наличие специальных символов", variable=symbols_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10, background = '#E0FFFF')
symbols_checkbutton.grid(row=3, column=0, sticky=W)

label_count = Label(root, text="Выберите длину пароля", background = '#E0FFFF')
label_count.grid(row=4, column=0, sticky=W)

counter = IntVar()
counter.set(0)
count = Scale(root, from_ = 0, to = 32, orient=HORIZONTAL, length=32 * 5, background = '#E0FFFF')
count.grid(row = 5, column = 0, sticky = W)

gen_button = Button(text="Сгенерировать", command=foo, background = '#E0FFFF')
gen_button.grid(row=6, column=0, sticky=W)

password_output = StringVar()
label_output = Label(root, textvariable = password_output, background = '#E0FFFF')
label_output.grid(row=7, column=0, sticky=W)

root.mainloop()
