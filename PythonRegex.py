import re

def validateEmail(email: str) -> bool:
    '''
    pattern:
        ^ matches start of string.
        [a-zA-Z0-9._%+-]+ matches one or more: alphanumeric characters, dots, underscores, percent signs, plus signs, or hyphens.
        @ matches @ symbol.
        [a-zA-Z0-9.-]+ matches one or more: alphanumeric characters, dots, or hyphens.
        \. matches dot before the top-level domain.
        [a-zA-Z]{2,} matches the top-level domain (must be at least 2 characters long).
        $ matches end of string.
    '''
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    return False


def checkValidateEmail():
    email = "example@example.com" # example
    if validateEmail(email):
        print(email," - Valid email address")
    else:
        print(email," - Invalid email address")


def extractPhoneNumbers(str_input: str) -> list[str]:
    '''
     pattern: (matches Isrsel Mobile numbers: 05XXXXXXXX)
        05 phone start.
        [0-9] one digit.
        \-? optional - symbol.
        [0-9]{7} other 7 digits.
    '''
    pattern = r"05[0-9]\-?[0-9]{7}"
    phone_numbers = re.findall(pattern, str_input)
    return phone_numbers


def checkExtractPhoneNumbers():
    str_input = "sd780567 6777777fs8d34f054054-6375653ghf" # example
    print(extractPhoneNumbers(str_input))


def parsingCSVdata(str_input: str) -> list[list[str]]:
    rows = str_input.strip().split('\\n')
    data = []
    for row in rows:
        pattern = r","
        values = re.split(pattern, row)
        data.append(values)
    return data


def checkParsingCSVdata():
    str_input = "fsgdg,dfg\\nvbn ghf" # example
    print(parsingCSVdata(str_input))


def extractingURLs(str_input: str) -> list[str]:
    '''    
    pattern: 
        http -static text.
        s? -optional char.
        :// -static text.
        (?:www\.)? -(www.) is optional.
        [^\s]+ -any sequence of non-whitespace characters
    '''
    pattern = r"https?://(?:www\.)?[^\s]+"
    return re.findall(pattern, str_input)


def checkExtractingURLs():
    str_input = "dfsfhttps://www.example.com sdfshttps://www.example.com" # example
    print(extractingURLs(str_input))


def main():
    checkExtractingURLs()


if __name__ == '__main__':
    main()