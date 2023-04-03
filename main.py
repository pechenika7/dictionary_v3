import random

def is_quit(promt = ''):
    return input(promt) in ['Q', 'q', 'Й', 'й']

def left_case_string(s):
    pass

def edit_settings():
    pass

def navigate_page():
    pass

def add_word():
    pass

def edit_word():
    pass

def edit():
    pass

def test():
    if eng_rus == [[], []]:
        print('Sorry. Dictionary is empty.')
    else:
        a = 0
        b = 1
        test_mode = input('Please choose test mod. If you want to translate words from English to Russian then press "e", otherwise press "r": ').upper()
        if test_mode in ['E', 'У']:
            # translate from english to russian
            a = 0
            b = 1
        elif test_mode in ['R', 'К']:
            # translate from russian to engish
            a = 1
            b = 0
        else:
            print('Wrong command! Сontinue with the standard setting: translation from English to Russian')
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
            if is_quit('Would you like to finish press "q", otherwise press any key: ') :
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

    #try
    #reset(f);
    #except
    #rewrite(f);
    #end;
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
        ch = input('q- quite work, e- edit, t- test, s- settings.\n').upper()
        if ch in ['Q', 'Й']: break
        elif ch == 'E': edit()
        elif ch == 'T': test()
        elif ch == 'S': edit_settings()
        else: print('Wrong command! Repeat please.')
    print('Goodbye!')



main_dict()