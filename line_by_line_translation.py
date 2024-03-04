def get_key(dict, value):
    k_list = list()
    for k, v in dict.items():
        if v == value:
            k_list.append(k)
    return k_list


def get_translate(dict, query):
    try:
        return(dict[query])
    except:
        k_list = get_key(dict, query)
        if k_list == []:
            return 'Word not found'
        else:
            return (k_list)


def scan():
    pass


def list_translate():
    pass