from shutil import copy2
def save_dict(dict_, path='dict.txt'):
    cw = len(dict_) #cw - count words
    f = open(path, 'w', encoding='utf8')
    lk = list(dict_.keys()) #lk- list keys
    lv = list(dict_.values()) #lv - list values
    for i in range(cw):
        temp = lk[i] + ';' + lv[i] + '\n'
        f.write(temp)
    f.close
    return cw


def back_up(user_, users_list, dict_):
    if users_list[2][user_] == 2:
        cw = save_dict(dict_, 'dict.bak')
        print('Success')
        return cw
    else:
        print("Access denied- you don't have permission.")
        return -1


def restore(user_, users_list):
    if users_list[2][user_] == 2:
      print('Restore completed')
      copy2('dict.bak', 'dict.txt')
    else:
        print("Access denied- you don't have permission.")