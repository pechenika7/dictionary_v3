def save_dict(eng_rus, path='dict.txt'):
    cw = len(eng_rus[0]) #cw - count words
    f = open(path, 'w', encoding='utf8')
    for i in range(cw):
        temp = eng_rus[0][i] + ';' + eng_rus[1][i] + '\n'
        f.write(temp)
    f.close
    return cw


def back_up(current_user, user_dict, eng_rus):
    if user_dict[2][current_user] == 2:
        cw = save_dict(eng_rus, 'dict.bak')
        return cw
    else:
        print("Access denied- you don't have permission.")
        return -1


def restore(current_user, user_dict):
    if user_dict[2][current_user] == 2:
      print('Restore completed')
      copy2('dict.bak', 'dict.txt')
    else:
        print("Access denied- you don't have permission.")