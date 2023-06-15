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


    while True:
        print('Please select command')
        ch = input('q- quite work, l- list words, e- edit, t- test, d- translate, s- settings, b- backup, r- restore.\n').upper()
        if ch in ['Q', 'Й']: break
        elif ch in ['L', 'Д']: list_words()
        elif ch in ['E', 'У']: edit()
        elif ch in ['T', 'Е']: test()
        elif ch in ['D', 'В']: translate()
        elif ch in ['S', 'Ы']: edit_settings()
        elif ch in ['B', 'И']: backup()
        elif ch in ['R', 'К']: restore()
        else: print('Wrong command! Repeat please.')
    print('Goodbye!')

def auth():

    def load_users():
        global user_dict
        user_dict = []
        user_file = open('users.data', 'r', encoding='utf8')
        nick = []
        password = []
        role = []
        while True:
            item = user_file.readline()
            if item == '' or item == '\n':
                break
            temp_list = item.split(';')
            nick.append(temp_list[0])
            password.append(temp_list[1])
            role.append(temp_list[2].strip())
        user_dict = [nick, password, role]
        count_user = len(nick)
        user_file.close
        print (user_dict)


    def sign_in():
        log = input('Please entre your nickname: ')
        paswd = input('Please entre your password: ')
        print(user_dict)
        flag = False
        for u in user_dict[0]:
            if u == log:
                if paswd == user_dict[1][user_dict[0].index(u)]:
                    print('Hello ', u, 'you successfully logged in')
        return True

    def reg():
        user_dict = 'Pushok'
        return True

    def guest():
        user_dict= 'guest'
        return True


    load_users()
    print('Hello! I am program dictionary!')
    while True:
        print('Please select command')
        ch = input('s- sign in, r- registration, g- guest.\n').upper()
        if ch in ['Q', 'Й']: break
        elif ch in ['S', 'Ы']:
            flag = sign_in()
            if flag: break
        elif ch in ['R', 'К']: reg()
        elif ch in ['G', 'П']: guest()
        else:
            print('Wrong command! Repeat please.')


auth()
main_dict()