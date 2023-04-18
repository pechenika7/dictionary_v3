import random

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

def is_quit(promt=''):
    return input(promt) in ['Q', 'q', 'Й', 'й']

def left_case_string(s):
    pass

def edit_settings():
    pass

def list_words():
    remainder = 0
    if count_words % words_on_page != 0:
        remainder = 1
    pages = count_words / words_on_page + remainder
    print('Dictionary contains ',coun_wtrds, ' words, ', words_on_page, ' item on the page, current page is 1 of', pages)
    current = 1
    while True:
        for i in range(words_on_page):
            print(eng_rus[(pages-1)*(current-1)+i])


def add_word():
    pass

def edit_word():
    pass

def edit():
    pass
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
        if item == '':
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
        ch = input('q- quite work, l- list words, e- edit, t- test, d- translete, s- settings.\n').upper()
        if ch in ['Q', 'Й']: break
        elif ch in ['L', 'Д']: list_words()
        elif ch == 'E': edit()
        elif ch == 'T': test()
        elif ch == 'D': translete()
        elif ch == 'S': edit_settings()
        else: print('Wrong command! Repeat please.')
    print('Goodbye!')



main_dict()