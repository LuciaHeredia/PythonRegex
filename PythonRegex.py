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


def main():
    email = "example@example.com"
    print(validateEmail(email))


if __name__ == '__main__':
    main()