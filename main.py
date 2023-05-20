import random
from shutil import copy2


def is_quit(promt=''):
    return input(promt) in ['Q', 'q', 'Й', 'й']

def edit_settings():
    pass


def list_words():
    reminder = count_words % words_on_page
    pages = count_words // words_on_page
    if reminder > 0:
        pages += 1
    if count_words < words_on_page:
        pages = 1
        reminder = count_words
    print('Dictionary contains ', count_words, ' words, ', words_on_page, ' item on the page, current page is 1 of', pages)
    current = 1
    while True:
        if (current == pages) and (reminder > 0):
            t = reminder
        else:
            t = words_on_page
        for i in range(t):
            print(eng_rus[0][words_on_page*(current-1)+i], '-', eng_rus[1][words_on_page*(current-1)+i])
        if pages == 1:
            break
        if is_quit('Do u want to continue, if not pleas type "q" '):
            break
        current = int(input('which page do you want to go to? Please enter the number: '))
    return(current)

def restore():
    print('restore')
    copy2('dict.bak', 'dict.txt')

def save_dict(path = 'dict.txt'):
    count_words = len(eng_rus[0])
    f = open(path, 'w', encoding='utf8')
    for i in range(count_words):
        temp = eng_rus[0][i] + ';' + eng_rus[1][i] + '\n'
        f.write(temp)
    f.close


def back_up():
    print('back up')
    save_dict('dict.bak')


def add_word():
    temp = input('Please type new couple of words: ')
    temp = temp.split()
    eng_rus[0].append(temp[0])
    eng_rus[1].append(temp[1])
    save_dict()


def edit_word():
    num = list_words()
    wn = int(input('Please entre position wrong word: '))
    pos = words_on_page * (num - 1) + (wn - 1)
    print(eng_rus[0][pos], '-', eng_rus[1][pos])
    item = int(input('What word is wrong? 0- english word, 1- russian word: '))
    #print(words_on_page * (num - 1) + (wn - 1))
    eng_rus[item][pos] = input('Please type correct variant: ')
    #print(eng_rus[words_on_pages * (num - 1) + wn])
    #print(eng_rus[0][pos], '-', eng_rus[1][pos])
    save_dict()



def edit():
    print('Edit mod activ')
    back_up()
    while True:
        ch = input('Choose edit mod: a- add word, e- edit word, q- quit: ')
        print(ch)
        if ch in ['a', 'A', 'ф', 'Ф']: add_word()
        elif ch in ['e', 'E', 'у', 'У']: edit_word()
        elif ch in ['q', 'Q', 'й', 'Й']:break
        else:
            print('Wrong command! Repeat please.')



def test_mode(promt):
    a = 0
    b = 0
    while True:
        tm = input(promt).upper()
        if tm in ['E', 'У', '1']:
            # translate from english to russian
            a = 0
            b = 1
            break
        elif tm in ['R', 'К', '2']:
            # translate from russian to engish
            a = 1
            b = 0
            break
        else:
            print('Wrong command! Repeat please.')
    return a, b



def translete():
    a, b = test_mode('Please select translation direction: eng-рус(press 1), рус-eng(press 2) ')
    query = input('Please type your word').lower()
    is_fine = False
    for i in range(count_words):
        if query == eng_rus[a][i]:
            print ('There is translate your word: "', eng_rus[b][i], '"')
            is_fine = True
            break
    if not(is_fine):
        print('Word not found')



def test():
    if eng_rus == [[], []]:
        print('Sorry. Dictionary is empty.')
    else:
        a, b = test_mode('Please select test mod. If you want to translate words from English to Russian then press "e", otherwise press "r": ')
        number_list = []
        for i in range(count_words):
            number_list.append(i)
        while True:
            n = random.randint(a, count_words-1)
            if n in number_list:
                if input('Please translate '+eng_rus[a][n]+' ') == eng_rus[b][n]:
                    print('You are right!')
                else:
                    print('No, you are wrong. Correct variant: "'+eng_rus[b][n]+'"')
            else:
                if number_list == []:
                    print('Testing finished')
                    break
                continue
            number_list.remove(n)
            if is_quit('Would you like to finish press "q", otherwise press any key: '):
                break




def main_dict():

    def load_settings(path):
        wp = '5'
        try:
            f = open(path, 'r', encoding='utf8')
            try:
                wp = int(f.readline())
            except:
                f.close
                f = open(path, 'w', encoding='utf8')
                f.write(wp)
        except:
            f = open(path, 'w', encoding='utf8')
            f.write(wp)
        f.close
        return wp





    global eng_rus
    global count_words
    global words_on_page
    words_on_page = load_settings('settings.txt')


    dict_file = open('dict.txt',  'r', encoding='utf8')

    eng = []
    rus = []
    while True:
        item = dict_file.readline()
        if item == '' or item == '\n':
            break
        temp_list = item.split(';')
        eng.append(temp_list[0])
        rus.append(temp_list[1].strip())
    eng_rus = [eng, rus]
    count_words = len(eng)
    dict_file.close

    print('Hello! I am program dictionary!')
    while True:
        print('Please select command')
        ch = input('q- quite work, l- list words, e- edit, t- test, d- translate, s- settings, b- backup, r- restore.\n').upper()
        if ch in ['Q', 'Й']: break
        elif ch in ['L', 'Д']: list_words()
        elif ch == 'E': edit()
        elif ch == 'T': test()
        elif ch == 'D': translete()
        elif ch == 'S': edit_settings()
        elif ch == 'B': backup()
        elif ch == 'R': restore()
        else: print('Wrong command! Repeat please.')
    print('Goodbye!')



main_dict()