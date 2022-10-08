class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = ['.com', '.bg', '.org', '.net']
email = input()

while email != 'End':
    try:
        if '@' not in email:
            raise MustContainAtSymbolError("Email must contain @")

        elif len(email.split('@')[0]) <= 4:
            raise NameTooShortError('Name must be more than 4 characters')

        elif '.' + email.split('.')[-1] not in domains:
            print(email.split('.')[-1])
            raise InvalidDomainError(f'Domain must be one of the following: {", ".join(domains)}')

        print(f'Email is valid')

    except IndexError:
        print(f'Invalid email')

    email = input()
