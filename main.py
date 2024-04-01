from random import shuffle
from password_utils import code_pswd, decode_pswd, check_role
from back_up_utils import save_dict, back_up, restore
from line_by_line_translation import get_translate, get_key


def is_quit(promt: str = '') -> list:
    temp = (input(promt).lower())
    flag = temp in {'q', 'й'}
    res = list()
    res.append(flag)
    res.append(temp)
    return res


def is_alphaEng(word_):
    eng_char = 'abcdefghijklmnopqrstuvwxyz_'
    for ch in word_.lower():
        if ch not in eng_char:
            return False
    return True


def is_alphaRus(word_):
    rus_char = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя_'
    for ch in word_.lower():
        if ch not in rus_char:
            return False
    return True


def is_nickname(word_):
    nick_char = 'abcdefghijklmnopqrstuvwxyz_!?-.0123456789'
    if word_[0].isdigit():
        return False
    for ch in word_.lower():
        if ch not in nick_char:
            return False
    if (len(word_) >= 3) and (len(word_) <= 20):
        return True
    else:
        return False



def is_password(word_):
    password_char = 'abcdefghijklmnopqrstuvwxyz_!?-.,#&*+0123456789'
    for ch in word_.lower():
        if ch not in password_char:
            return False
    if (len(word_) >= 4) and (len(word_) <= 20):
        return True
    else:
        return False


def edit_settings(user_, list_user):
    if check_role(list_user, user_, 'admin') or check_role(list_user, user_, 'user'):
        pass


def list_words(dict_: dict, count_words: int, words_on_page: int) -> str:
    lk = list(dict_.keys())  # lk- list keys
    lv = list(dict_.values())  # lv - list values
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
        if (current <= pages) and (current > 0):
            if (current == pages) and (reminder > 0):
                t = reminder
            else:
                t = words_on_page
            for i in range(t):
                print(lk[words_on_page*(current-1)+i], '-', lv[words_on_page*(current-1)+i])
            if pages == 1:
                break
        else:
            print('Page is too big')
        res = is_quit('Select page or type "q" for quit ')
        if res[0]:
            break
        current = int(res[1])
    return current


def add_word(dict_):
    res = is_quit('Please type new couple of words or type "q" to quit: ')
    if not res[0]:
        temp = res[1].split()
        if dict_.get(temp[0]) is None:
            dict_[temp[0]] = temp[1].strip()
            save_dict(dict_)
        else:
            print('This word already in dictionary')


def edit_word(dict_, count_words, words_on_page):
    r = list_words(dict_, count_words, words_on_page)
    res = is_quit('Please type wrong word or type "q" to quit: ')
    if not res[0]:
        temp = dict_.get(res[1])
        if temp is None:
            k = get_key(dict_, res[1])
            if not k == []:
                if len(k) == 1:
                    dict_[k[0]] = input('Please type correct variant: ')
                else:
                    print(k, '\n', 'According to your request find', len(k), 'words')
                    req = int(input('Please type word number'))
                    dict_[k[req-1]] = input('Please type correct variant: ')
            else:
                print('Word not found')
        else:
            dict_[input('Please type correct variant: ')] = dict_.pop(res[1])
        print(dict_)
        save_dict(dict_)


def edit(dict_, user_, list_user, count_words, words_on_page):
    if check_role(list_user, user_, 'admin'):
        print('Edit mod activ')
        back_up(user_, list_user, dict_)
        while True:
            ch = input('Choose edit mod: a- add word, e- edit word, q- quit: ')
            print(ch)
            if ch in {'a', 'A', 'ф', 'Ф'}:
                add_word(dict_)
            elif ch in {'e', 'E', 'у', 'У'}:
                edit_word(dict_, count_words, words_on_page)
            elif ch in {'q', 'Q', 'й', 'Й'}:
                break
            else:
                print('Wrong command! Repeat please.')
    else:
        print("Access denied- you don't have permission.")


def translate(dict_):
    query = input('Please type your word ').lower()
    print(get_translate(dict_, query))


def test(dict_):
    if len(dict_) == 0:
        print('Sorry. Dictionary is empty.')
    else:
        res = is_quit("Hello, I am program testing. Please select test mod. If you want to translate words from English to Russian then press 'e', otherwise press 'r' or press 'q' to quit: ")
        if not res[0]:
            if res[1] in ['e', 'у', '1']:
                list_ = list(dict_.keys())
                shuffle(list_)
            else:
                list_ = list(dict_.values())
                shuffle(list_)
            summary = 0
            success = 0
            for n in list_:
                summary += 1
                quest = input('Please translate '+n+' ')  # ввод слова
                answer = get_translate(dict_, n)  # перевод слова
                try:
                    gk = get_key(dict_, n)
                    gk = gk[0]
                except ValueError:
                    gk = ''
                if dict_.get(n) == quest or gk == quest:
                    print('You are right!')
                    success += 1
                else:
                    if type(answer) == list:
                        res_ans = ''
                        for i in answer:
                            res_ans += '{'+i+'}'
                        answer = res_ans
                    print('No, you are wrong. Correct variant is ' + answer)
                res = is_quit('Would you like to finish press "q", otherwise press any key: ')
                if res[0]:
                    break
            print('You result ' + str(success) + '/' + str(summary))


def main_dict(list_user):

    def load_settings(path):
        wp = '5'
        try:
            f = open(path, 'r', encoding='utf8')
            try:
                wp = int(f.readline())
            except FileNotFoundError:  # файл пустой
                f.close()
                f = open(path, 'w', encoding='utf8')
                f.write(wp)
        except FileNotFoundError:  # файл пустой
            f = open(path, 'w', encoding='utf8')
            f.write(wp)
        f.close()
        return wp


    words_on_page = load_settings('settings.txt')
    dict_file = open('dict.txt',  'r', encoding='utf8')
    eng_rus = dict()
    while True:
        item = dict_file.readline()
        if item == '' or item == '\n':
            break
        temp_list = item.split(';')
        temp_list[1] = temp_list[1].strip('\n')
        if is_alphaEng(temp_list[0]) and is_alphaRus(temp_list[1]):
            eng_rus[temp_list[0]] = temp_list[1].strip()
        else:
            print('input file error',temp_list[0],temp_list[1])
            exit()
    count_words = len(eng_rus)
    dict_file.close()
    print(eng_rus)

    while True:
        print('Please select command')
        ch = input('q- quite work, l- list words, e- edit, t- test, d- translate, s- settings, b- backup, r- restore, x- file translation.\n').upper()
        if ch in {'Q', 'Й'}:
            break
        elif ch in {'L', 'Д'}:
            list_words(eng_rus, count_words, words_on_page)
        elif ch in {'E', 'У'}:
            edit(eng_rus, current_user, list_user, count_words, words_on_page)
        elif ch in {'T', 'Е'}:
            test(eng_rus)
        elif ch in {'D', 'В'}:
            translate(eng_rus)
        elif ch in {'S', 'Ы'}:
            edit_settings(current_user, list_user)
        elif ch in {'X', 'Ч'}:
            print('function in developing')
        elif ch in {'B', 'И'}:
            res = back_up(current_user, list_user, eng_rus)
            if res != -1:
                count_words = res
        elif ch in {'R', 'К'}:
            restore(current_user, list_user)
        else:
            print('Wrong command! Repeat please.')
    print('Goodbye!')


def auth():

    def load_users():
        ud = []
        nick = []
        password = []
        role = []
        try:
            user_file = open('users.data', 'r', encoding='utf8')
            while True:
                item = user_file.readline()
                if item == '' or item == '\n':
                    break
                temp_list = item.split(';')
                nick.append(decode_pswd(temp_list[0]))
                password.append(decode_pswd(temp_list[1]))
                role.append(int(temp_list[2].strip()))
        except FileNotFoundError:
            user_file = open('users.data', 'w', encoding='utf8')
            user_file.write('guest;0000;0')
            nick.append('guest')
            password.append('0000')
            role.append(0)
            print('xxx')
        finally:
            user_file.close()
            ud = [nick, password, role]
        print(ud)
        return ud

    def sign_in(user_dict):
        if len(user_dict[0]) == 1:
            return -2
        else:
            log = input('Please entre your nickname: ')
            paswd = input('Please entre your password: ')
            for u in user_dict[0]:
                if u == log:
                    if paswd == user_dict[1][user_dict[0].index(u)]:
                        print('Hello', u, 'you successfully logged in')
                        return user_dict[0].index(u)
        return -1

    def reg(user_dict):
        while True:
            # nick = code_pswd(input('Please entre your nickname: '))
            nick = input('Please entre your nickname: ')
            if is_nickname(nick):
                break
            else:
                temp = input('Forbidden symbol or too small/big length or nickname must not start with digit. Pls try again. If you want to quit then print "q"').lower()
                if temp in {'q', 'й'}:
                    exit()
        while True:
            # pswd = code_pswd(input('Please entre your password: '))
            pswd = input('Please entre your password: ')
            if is_password(pswd):
                break
            else:
                temp = input('Forbidden symbol or too small/big length. Pls try again. If you want to quit then print "q"').lower()
                if temp in {'q', 'й'}:
                    exit()
        user_dict[0].append(nick)
        user_dict[1].append(pswd)
        user_dict[2].append(1)
        user_file = open('users.data', 'a', encoding='utf8')
        item = ('\n' + nick + ';' + pswd + ';' + '1')
        user_file.write(item)
        user_file.close()
        return len(user_dict[0]) - 1

    def guest():
        print('Welcome guest!\nFor full access you have to registration.')
        return 0

    user_dict = load_users()
    current_user = 0
    print('Hello! I am program dictionary!')
    while True:
        print('Please select command')
        ch = input('s- sign in, r- registration, g- guest.\n').upper()
        if ch in {'Q', 'Й'}:
            exit()
        elif ch in {'S', 'Ы'}:
            current_user = sign_in(user_dict)
            if current_user > 0:
                break
            elif current_user == -1:
                print('Incorrect login or password. Please try again ')
            elif current_user == -2:
                print('Your account is lost. Please registrate or use guest mode')
        elif ch in {'R', 'К'}:
            current_user = reg(user_dict)
            print(current_user)
            break
        elif ch in {'G', 'П'}:
            current_user = guest()
            break
        else:
            print('Wrong command! Repeat please.')

    return current_user, user_dict

current_user, user_dict = auth()
main_dict(user_dict)