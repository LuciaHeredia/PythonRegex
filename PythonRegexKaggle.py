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

    # 3. match a string that has an 'a' followed by one or more b's
    '''
     pattern: 
        b+ -match one to more 'b's.
    '''
    pattern = r"ab+?"

    # 4. match a string that has an 'a' followed by zero or one 'b's
    '''
     pattern: 
        b? -match zero or one 'b's (at least).
    '''
    pattern = r"ab?"

    # 5. match a string that has an 'a' followed by three 'b's
    '''
     pattern: 
        b{3} -bbb exactly.
    '''
    pattern = r"ab{3}?"

    # 6. match a string that has an 'a' followed by two or three 'b's
    '''
     pattern: 
        b{2,3} -bb or bbb exactly.
    '''
    pattern = r"ab{2,3}?"

    # 9. match a string that has an 'a' followed by anything, ending in 'b'
    '''
     pattern: 
        a -the char 'a'
        .* -match any single char except newline, 0 or more repetitions.
        b$ -ends in 'b'
    '''
    pattern = r"a.*b$"

    if re.search(pattern, str_input):
        return True
    return False

def check_match_str_ax():
    str_input = "aab" # example
    if match_str_ax(str_input):
        print("Found a match.")
    else:
        print("No match.")


def find_sequences_Xcase(str_input: str):
    # 7. find sequences of lowercase letters joined(connected) with a underscore.
    '''
     pattern: 
        [a-z]+ -lowercase characters, one or more.
        _ -the char '_'
    '''
    pattern = r"[a-z]+_[a-z]+"

    # 8. find sequences of one upper case letter followed by lower case letters.
    '''
     pattern: 
        [A-Z] -one upper case letter.
        [a-z]+ -lowercase characters, one or more.
    '''
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, str_input)

def check_find_sequences_Xcase():
    str_input = "FD Fd_ss32 d_Fh45 dsf" # example
    print("The sequences found:", find_sequences_Xcase(str_input))


def word_at_beginning(str_input: str):
    # 10. Match a word at the beginning of a string.
    '''
     pattern: 
        ^ -match start of string
        [a-zA-Z] -alphabetic chars
        + -one or more alphabetic chars
    '''
    pattern = r"^[a-zA-Z]+"
    if re.match(pattern, str_input):
        return True
    return False

def check_word_at_beginning():
    str_input = "d 332world" # example
    if word_at_beginning(str_input):
        print("Match found.")
    else:
        print("No match found.")


def word_at_end(str_input: str):
    # 11. Match a word at the end of string, with optional punctuation.
    '''
     pattern: 
        [a-zA-Z]+ -one or more alphabetic char.
        [^\w\s]* - matches any non-word, non-space character, zero or more times.
        $ -matches the end of the string(of preceding regex).
    '''
    pattern = r"[a-zA-Z]+[^\w\s]*$"
    if re.search(pattern, str_input):
        return True
    return False

def check_word_at_end(): 
    str_input = "hi you!" # example
    if word_at_end(str_input):
        print("Match found.")
    else:
        print("No match found.")


def containing_char(str_input: str):
    # 12. Match a word containing 'z'.
    '''
     pattern: 
        \b -word boundry.
        \w* - zero or more word chars.
        z -char 'z'.
    '''
    pattern = r"\b\w*z\w*\b"

    # 13. Match a word containing 'z', not at the start or end of the word.
    '''
     pattern: 
        \B - match where chars are present, but NOT at start/end of a word.
        z -char 'z'.
    '''
    pattern = r"\Bz\B"

    if re.search(pattern, str_input):
        return True
    return False

def check_containing_char():
    str_input = "the hero zd khjd" # example
    if containing_char(str_input):
        print("Match found.")
    else:
        print("No match found.")


def match_string(str_input: str):
    # 14. Match a string that has only: upper/lowercase letters, numbers, underscores.
    '''
     pattern: 
        ^ -match start of string.
        [a-zA-Z0-9_]* - zero or more: upper/lowercase letters, numbers, underscores.
        $ -match end of string.
    '''
    pattern = r"^[a-zA-Z0-9_]*$"
    results = re.search(pattern, str_input)

    # 15. Match a string where it starts with a specific number.(ex.:1)
    '''
     pattern: 
        ^1 -match start of string with char'1'.
    '''
    pattern = r"^1"
    results = re.match(pattern, str_input)

    if results:
        return True
    return False

def check_match_string():
    str_input = "1_the_hero_is_him" # example
    if match_string(str_input):
        print("Match found.")
    else:
        print("No match found.")


def remove_leading_zeros(ip: str):
    # 16. Remove leading zeros from IP address.
    '''
     pattern: 
        \.[0]* -char "."with zero or more 0's after
    '''
    pattern = r"\.[0]*"
    # with sub, replace pattern with "."
    return re.sub(pattern, '.', ip) 

def check_remove_leading_zeros():
    ip = "13.0342.032.2" # example
    print(remove_leading_zeros(ip))


def is_num_at_end(str_input: str):
    # 17. Check for a number at the end of a string.
    '''
     pattern: 
        \d+ -one or more nu,eric char
        $ -at end of string
    '''
    pattern = r"\d+$"
    return re.search(pattern, str_input) 

def check_is_num_at_end():
    str_input = "year 2022" # example
    if is_num_at_end(str_input):
        print("Match found.")
    else:
        print("No match found.")


def main():
    #check_is_str_alphanumeric()
    #check_match_str_ax()
    #check_find_sequences_Xcase()
    #check_word_at_beginning()
    #check_word_at_end()
    #check_containing_char()
    #check_match_string()
    #check_remove_leading_zeros()
    check_is_num_at_end()

if __name__ == '__main__':
    main()
    