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
    #pass
    print(words_on_page)
    print(eng_rus)

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
    print('Hello! I am program dictionary!')
    while True:
        print('Please select command')
        ch = input('q- quite work, e- edit, t- test, s- settings.\n')
        if ch == 'q': break
        elif ch == 'e': edit()
        elif ch == 't': test()
        elif ch == 's': edit_settings()
        else: print('Wrong command! Repeat please.')
    print('Goodbye!')
    #close(f);



main_dict()