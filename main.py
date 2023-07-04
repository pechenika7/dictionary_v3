global current_user
current_user = 0

import random
from shutil import copy2


def code_pswd(str_):
    return str_[::-1]


def decode_pswd(str_):
    return str_[::-1]


def is_quit(promt=''):
    return input(promt) in {'Q', 'q', 'Й', 'й'}


def edit_settings(current_user):
    if user_dict[2][current_user] in {1, 2}:
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


def restore(current_user):
    if user_dict[2][current_user] == 2:
      print('restore')
      copy2('dict.bak', 'dict.txt')


def save_dict(path = 'dict.txt'):
    count_words = len(eng_rus[0])
    f = open(path, 'w', encoding='utf8')
    for i in range(count_words):
        temp = eng_rus[0][i] + ';' + eng_rus[1][i] + '\n'
        f.write(temp)
    f.close


def back_up(current_user):
    if user_dict[2][current_user] == 2:
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


def edit(current_user):
    if user_dict[2][current_user] == 2:
      print('Edit mod activ')
      back_up()
      while True:
          ch = input('Choose edit mod: a- add word, e- edit word, q- quit: ')
          print(ch)
          if ch in {'a', 'A', 'ф', 'Ф'}: add_word()
          elif ch in {'e', 'E', 'у', 'У'}: edit_word()
          elif ch in {'q', 'Q', 'й', 'Й'}: break
          else:
              print('Wrong command! Repeat please.')
    else:
      print("Access denied- you don't have permission.")


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


def translate():
    a, b = test_mode('Please select translation direction: eng-рус(press 1), рус-eng(press 2) ')
    query = input('Please type your word').lower()
    is_fine = False
    for i in range(count_words):
        if query == eng_rus[a][i]:
            print ('There is translate your word: "', eng_rus[b][i], '"')
            is_fine = True
            break
    if not (is_fine):
        print('Word not found')


def test():
    if eng_rus == [[], []]:
        print('Sorry. Dictionary is empty.')
    else:
        if not(is_quit("Hello, I'm program testing. Press any key to start ot 'q' to quit.")):
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
        if ch in {'Q', 'Й'}: break
        elif ch in {'L', 'Д'}: list_words()
        elif ch in {'E', 'У'}: edit(current_user)
        elif ch in {'T', 'Е'}: test()
        elif ch in {'D', 'В'}: translate()
        elif ch in {'S', 'Ы'}: edit_settings()
        elif ch in {'B', 'И'}: backup()
        elif ch in {'R', 'К'}: restore()
        else: print('Wrong command! Repeat please.')
    print('Goodbye!')


def auth():

    def load_users():
        global user_dict
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
        print (user_dict)

    def sign_in():
        log = input('Please entre your nickname: ')
        paswd = input('Please entre your password: ')
        for u in user_dict[0]:
            if u == log:
                if paswd == user_dict[1][user_dict[0].index(u)]:
                    print('Hello', u, 'you successfully logged in')
                    return user_dict[0].index(u)
        return -1

    def reg():
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

    load_users()
    print('Hello! I am program dictionary!')
    while True:
        print('Please select command')
        ch = input('s- sign in, r- registration, g- guest.\n').upper()
        if ch in {'Q', 'Й'}: break
        elif ch in {'S', 'Ы'}:
            current_user = sign_in()
            if current_user != -1:
                break
            print('Incorrect login or password. Please try again ')
        elif ch in {'R', 'К'}:
            current_user = reg()
            print(current_user)
            break
        elif ch in {'G', 'П'}:
            current_user = guest()
            break
        else:
            print('Wrong command! Repeat please.')

    return current_user

current_user = auth()
main_dict()