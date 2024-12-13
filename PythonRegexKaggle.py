import re


def is_str_alphanumeric(str_input: str):
    #  1. check if string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
    '''
     pattern: 
        \W -Matches any non-alphanumeric character, equivalent to [^a-zA-Z0-9_].
    '''
    pattern = r"[\W]"
    if re.search(pattern, str_input) is None:
        return True
    return False

def check_is_str_alphanumeric():
    str_input = "dfgsd45345g5434234" # example
    if is_str_alphanumeric(str_input):
        print(str_input," - Is alphanumeric.")
    else:
        print(str_input," - Is non-alphanumeric.")


def match_str_ax(str_input: str):
    # 2. match a string that has an 'a' followed by none or more 'b's
    '''
     pattern: 
        a -static char.
        b* -match none to more 'b's.
        ? -the ? after, makes the match non-greedy, meaning it will match as few 'b's as possible.
    '''
    pattern = r"ab*?"

    # 3. matche a string that has an 'a' followed by one or more b's
    '''
     pattern: 
        b+ -match one to more 'b's.
    '''
    pattern = r"ab+?"

    # 4. matche a string that has an 'a' followed by zero or one 'b's
    '''
     pattern: 
        b? -match zero or one 'b's (at least).
    '''
    pattern = r"ab?"

    # 5. matche a string that has an 'a' followed by three 'b's
    '''
     pattern: 
        b{3} -bbb exactly.
    '''
    pattern = r"ab{3}?"

    # 6. matche a string that has an 'a' followed by two or three 'b's
    '''
     pattern: 
        b{2,3} -bb or bbb exactly.
    '''
    pattern = r"ab{2,3}?"

    if re.search(pattern, str_input):
        return True
    return False


def check_match_str_ax():
    str_input = "abb" # example
    if match_str_ax(str_input):
        print("Found a match.")
    else:
        print("No match.")





def main():
    #check_is_str_alphanumeric()
    check_match_str_ax()

if __name__ == '__main__':
    main()
    