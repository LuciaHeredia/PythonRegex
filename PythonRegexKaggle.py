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
        
    '''
    pattern = r"ab*?"
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