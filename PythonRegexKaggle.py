import re


def is_str_alphanumeric(str_input: str):
    #  check if string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
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


def main():
    check_is_str_alphanumeric()
    #print('')


if __name__ == '__main__':
    main()