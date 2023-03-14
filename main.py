def left_case_string(s):
    pass

def edit_settings():
    pass

def load_settings():
    pass

def navigate_page():
    pass

def add_word():
    pass

def edit_word():
    pass

def edit():
    pass

def test():
    pass

def main_dict():
    load_settings()
    #assign (f,pass);
    #try
    #reset(f);
    #except
    #rewrite(f);
    #end;
    #while not(eof(f)) do
    #begin
    #read (f,item);
    #count+=1;
    #end;
    print('Hello! I am program dictionary!')
    while True:
        print('Please select command')
        ch = input('q- quite work, e- edit, t- test, s- settings.\n')
        if ch == 'q': break
        elif ch == 'e': edit()
        elif ch == 't': test()
        elif ch == 's': edit_settings()
        else: print('Wrong command! Repeat please.')
    print('Goodbye!')
    #close(f);



main_dict()