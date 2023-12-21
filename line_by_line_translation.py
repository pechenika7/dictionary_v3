def scan():
    list_ = list()
    f = open('D:\python lesson\dictionary_v3\storage\proverb.txt', 'r', encoding='utf8')
    while True:
        line_ = f.readline()
        if line_ == '' or line_ == '\n':
            break
        list_.extend(line_.split())
    return list_