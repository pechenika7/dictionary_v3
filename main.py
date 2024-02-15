from random import shuffle
from password_utils import code_pswd, decode_pswd
from back_up_utils import save_dict, back_up, restore
from line_by_line_translation import scan, list_translate, get_translate, get_key


def is_quit(promt=''):
    temp = (input(promt).lower())
    flag = temp in {'q', 'й'}
    res = list()
    res.append(flag)
    res.append(temp)
    return res


def edit_settings(current_user, user_dict):
    if user_dict[2][current_user] in {1, 2}:
      pass


def list_words(dict, count_words, words_on_page):
    lk = list(dict.keys())  # lk- list keys
    lv = list(dict.values())  # lv - list values
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
        if current <= pages and current > 0:
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
        if (res[0]):
            break
        current = int(res[1])
    return(current)


def add_word(dict):
    res = is_quit('Please type new couple of words or type "q" to quit: ')
    if res[0] == False:
        temp = res[1].split()
        if dict.get(temp[0]) == None:
            dict[temp[0]] = temp[1].strip()
            save_dict(dict)
        else:
            print('This word already in dictionary')


def edit_word(dict, count_words, words_on_page):
    r = list_words(dict, count_words, words_on_page)
    res = is_quit('Please type wrong word or type "q" to quit: ')
    if res[0] == False:
        temp = dict.get(res[1])
        if temp == None:
            k = get_key(dict,res[1])
            if k!= []:
                if len(k) == 1:
                    dict[k[0]] = input('Please type correct variant: ')
                else:
                    print(k, '\n', 'According to your request find', len(k), 'words')
                    req = int(input('Please type word number'))
                    dict[k[req-1]] = input('Please type correct variant: ')
            else:
                    print('Word not found')
        else:
            dict[input('Please type correct variant: ')] = dict.pop(res[1])
        print(dict)
        save_dict(dict)


def edit(dict, current_user, user_dict, count_words, words_on_page):
    if user_dict[2][current_user] == 2:
      print('Edit mod activ')
      back_up(current_user, user_dict, dict)
      while True:
          ch = input('Choose edit mod: a- add word, e- edit word, q- quit: ')
          print(ch)
          if ch in {'a', 'A', 'ф', 'Ф'}: add_word(dict)
          elif ch in {'e', 'E', 'у', 'У'}: edit_word(dict, count_words, words_on_page)
          elif ch in {'q', 'Q', 'й', 'Й'}: break
          else:
              print('Wrong command! Repeat please.')
    else:
      print("Access denied- you don't have permission.")


def translate(dict):
    query = input('Please type your word ').lower()
    print(get_translate(dict, query))


def test(eng_rus):
    if eng_rus == [[], []]:
        print('Sorry. Dictionary is empty.')
    else:
        res = is_quit("Hello, I am program testing. Please select test mod. If you want to translate words from English to Russian then press 'e', otherwise press 'r' or press 'q' to quit: ")
        if res[0] == False:
            if res[1] in ['e', 'у', '1']:
                list_ = list(eng_rus.keys())
                shuffle(list_)
            else:
                list_ = list(eng_rus.values())
                shuffle(list_)
            summary = 0
            succes = 0
            for n in list_:
                summary += 1
                quest = input('Please translate '+n+' ') #ввод слова
                answer = get_translate(eng_rus, n)#перевод слова
                try:
                    gk = get_key(eng_rus,n)
                    gk = gk[0]
                except:
                    gk = ''
                if eng_rus.get(n) == quest or gk == quest:
                    print('You are right!')
                    succes += 1
                else:
                    if type(answer) == list:
                        res_ans = ''
                        for i in answer:
                            res_ans += '{'+i+'}'
                        answer =res_ans
                    print('No, you are wrong. Correct variant is ' + answer)
                res = is_quit('Would you like to finish press "q", otherwise press any key: ')
                if res[0]:
                    break
            print('You result ' + str(succes) + '/' + str(summary))


def main_dict(user_dict):

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


    words_on_page = load_settings('settings.txt')


    dict_file = open('dict.txt',  'r', encoding='utf8')

    eng_rus = {}
    while True:
        item = dict_file.readline()
        if item == '' or item == '\n':
            break
        temp_list = item.split(';')
        eng_rus[temp_list[0]] = temp_list[1].strip()
    count_words = len(eng_rus)
    dict_file.close()
    print(eng_rus)


    while True:
        print('Please select command')
        ch = input('q- quite work, l- list words, e- edit, t- test, d- translate, s- settings, b- backup, r- restore, x- file translation.\n').upper()
        if ch in {'Q', 'Й'}: break
        elif ch in {'L', 'Д'}: list_words(eng_rus, count_words, words_on_page)
        elif ch in {'E', 'У'}: edit(eng_rus, current_user, user_dict, count_words, words_on_page)
        elif ch in {'T', 'Е'}: test(eng_rus)
        elif ch in {'D', 'В'}: translate(eng_rus)
        elif ch in {'S', 'Ы'}: edit_settings(current_user, user_dict)
        elif ch in {'X', 'Ч'}: print(list_translate(eng_rus, scan()))
        elif ch in {'B', 'И'}:
            res = back_up(current_user, user_dict, eng_rus)
            if res != -1:
                count_words = res
        elif ch in {'R', 'К'}: restore(current_user, user_dict)
        else: print('Wrong command! Repeat please.')
    print('Goodbye!')


def auth():

    def load_users():
#        global user_dict
        current_user = 0
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
            nick.append(decode_pswd(temp_list[0]))
            password.append(decode_pswd(temp_list[1]))
            role.append(int(temp_list[2].strip()))
        user_dict = [nick, password, role]
        count_user = len(nick)
        user_file.close
        print(user_dict)
        return user_dict

    def sign_in(user_dict):
        log = input('Please entre your nickname: ')
        paswd = input('Please entre your password: ')
        for u in user_dict[0]:
            if u == log:
                if paswd == user_dict[1][user_dict[0].index(u)]:
                    print('Hello', u, 'you successfully logged in')
                    return user_dict[0].index(u)
        return -1

    def reg(user_dict):
        nick = code_pswd(input('Please entre your nickname: '))
        pswd = code_pswd(input('Please entre your password: '))
        user_dict[0].append(nick)
        user_dict[1].append(pswd)
        user_dict[2].append(1)
        user_file = open('users.data', 'a', encoding='utf8')
        item = ('\n' + nick + ';' + pswd + ';' + '1')
        user_file.write(item)
        user_file.close
        return len(user_dict[0]) - 1

    def guest():
        print('Welcome guest!\nFor full access you have to registration.')
        return 0

    user_dict = load_users()
    print('Hello! I am program dictionary!')
    while True:
        print('Please select command')
        ch = input('s- sign in, r- registration, g- guest.\n').upper()
        if ch in {'Q', 'Й'}: break
        elif ch in {'S', 'Ы'}:
            current_user = sign_in(user_dict)
            if current_user != -1:
                break
            print('Incorrect login or password. Please try again ')
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