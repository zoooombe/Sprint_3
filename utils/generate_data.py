import random
import string


def generate_email():
    name = "timur"
    last_name = "rakhmatullin"
    cohort = "29"
    random_digits = str(random.randint(100, 999))
    domain = "yandex.ru"

    return f"{name}_{last_name}_{cohort}_{random_digits}@{domain}"


def generate_password(length=6):

    if length < 8:
        length = 8

    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))

    return password


def generate_name():
    names = ["Иван", "Анна", "Петр", "Мария", "Алексей", "Елена", "Сергей", "Ольга", "Алексей", "Доздраперма"]
    return random.choice(names)
