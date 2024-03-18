def get_key(dict_, value):
    k_list = list()
    for k, v in dict_.items():
        if v == value:
            k_list.append(k)
    return k_list


def get_translate(dict_, query):
    try:
        return(dict_[query])
    except:
        k_list = get_key(dict_, query)
        if k_list == []:
            return 'Word not found'
        else:
            return (k_list)


def scan():
    pass


def list_translate():
    pass