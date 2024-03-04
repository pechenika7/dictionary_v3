def code_pswd(str_):
    return str_[::-1]


def decode_pswd(str_):
    return str_[::-1]


def check_role(user_dict,current_user, role):
    role_list = {'admin': 2, 'user': 1, 'guest': 0}
    return user_dict[2][current_user] == role_list[role]