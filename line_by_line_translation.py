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
    list_1 = list()
    f = open('D:\python lesson\dictionary_v3\storage\proverb.txt', 'r', encoding='utf8')
    while True:
        line_ = f.readline()
        if line_ == '' or line_ == '\n':
            break
        list_1.extend(line_.split())
    return list_1


def list_translate(dict, list_1):
    list_2 = list()
    for i in list_1:
        list_2.append(get_translate(dict, i))
    return list_2