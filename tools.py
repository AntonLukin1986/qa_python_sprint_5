'''Дополнительные инструменты для тестов.'''
import random
import string


def generate_password():
    '''Генератор паролей.'''
    length = random.randint(6, 10)
    chars = string.digits + string.ascii_letters + string.punctuation
    return ''.join(random.choices(chars, k=length))


def generate_login():
    '''Генератор логинов.'''
    prefix = {
        'chars': string.digits + string.ascii_lowercase,
        'min_max_len': (3, 10),
        'sep': '@'
    }
    domain = {
        'chars': string.ascii_lowercase,
        'min_max_len': (2, 7),
        'sep': '.'
    }
    zone = {
        'chars': string.ascii_lowercase,
        'min_max_len': (2, 3),
        'sep': ''
    }
    login = ''
    for segment in prefix, domain, zone:
        chars = segment['chars']
        length = random.randint(*segment['min_max_len'])
        login += ''.join(random.choices(chars, k=length)) + segment['sep']
    return login


if __name__ == '__main__':
    print('login:   ', generate_login())
    print('password:', generate_password())
